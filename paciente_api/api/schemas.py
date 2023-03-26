from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel


class Sexo(str, Enum):
    masculino = "M"
    feminino = "F"


class ProntuarioBase(BaseModel):
    id_paciente : int
    data_nascimento: datetime
    sexo: Sexo
    texto_prontuario: str
    id_atendimento: int
    data_atendimento: datetime


class ProntuarioCreate(ProntuarioBase):
    pass


class Prontuario(ProntuarioBase):
    id_prontuario: int

    class Config:
        orm_mode = True

