from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel


class Sexo(str, Enum):
    masculino = "M"
    feminino = "F"


class PacienteModel(BaseModel):
    id_paciente: str
    data_nascimento: datetime
    sexo: Sexo
    texto_prontuario: bytes
    id_atendimento: str
    data_atendimento: datetime

    class Config:
        orm_mode = True


class Pacientes(BaseModel):
    pacientes: List[PacienteModel]
