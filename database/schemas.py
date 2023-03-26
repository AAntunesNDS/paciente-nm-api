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


class DiagnosticoBase(BaseModel):
    id_paciente: int
    id_atendimento: int
    disorder: str
    flag_ca: bool
    created_at: datetime


class DiagnosticoCreate(DiagnosticoBase):
    pass


class Diagnostico(DiagnosticoBase):
    id_diagnostico: int

    class Config:
        orm_mode = True
