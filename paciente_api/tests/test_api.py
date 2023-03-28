from fastapi.testclient import TestClient
from unittest import mock
from api import __version__
from api.main import app
from database import schemas
import ast

client = TestClient(app)

def test_version():
    assert __version__ == '0.1.0'

def test_create_prontuario_success():
    body = {
        "id_paciente": 4,
        "data_nascimento": "2023-03-27T22:13:33.532Z",
        "sexo": "M",
        "texto_prontuario": "Paciente com CA de mama, histórico de diabetes mellitus",
        "id_atendimento": 5,
        "data_atendimento": "2023-03-27T22:13:33.532Z"
    }
    response = client.post("/create_prontuario", json=body)
    assert response.status_code == 200

def test_create_prontuario_wrong_field():
    body = {
        "id": 4, # worng field
        "data_nascimento": "2023-03-27T22:13:33.532Z",
        "sexo": "M",
        "texto_prontuario": "Paciente com CA de mama, histórico de diabetes mellitus",
        "id_atendimento": 5,
        "data_atendimento": "2023-03-27T22:13:33.532Z"
    }
    response = client.post("/create_prontuario", json=body)
    assert response.status_code == 422

@mock.patch("database.crud.create_prontuario")
@mock.patch("rabbitmq.publisher.RabbitmqPublisher.send_message")
def test_create_prontuario(mock_send_message, mock_create_prontuario):
    prontuario_data = {
        "id_paciente":1,
        "data_nascimento":"2023-03-27T22:13:33.532Z",
        "sexo":"F",
        "texto_prontuario":"teste",
        "id_atendimento":1,
        "data_atendimento":"2023-03-27T22:13:33.532Z",
        "id_prontuario":1
    }
    prontuario = schemas.Prontuario(**prontuario_data)

    mock_create_prontuario.return_value = schemas.Prontuario(**prontuario_data)
    mock_send_message.return_value = None

    response = client.post("/create_prontuario", json=prontuario_data)
    assert response.status_code == 200
    assert ast.literal_eval(response.text)["id_paciente"] == ast.literal_eval(mock_create_prontuario.return_value.json())["id_paciente"]

    