from sqlalchemy import Column, String, DateTime, Enum, Binary
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as EnumSQLAlchemy

Base = declarative_base()

class SexoEnum(EnumSQLAlchemy):
    masculino = "M"
    feminino = "F"

class PacienteModel(Base):
    __tablename__ = "paciente"

    id_paciente = Column(String, primary_key=True)
    data_nascimento = Column(DateTime, nullable=False)
    sexo = Column(Enum(SexoEnum), nullable=False)
    texto_prontuario = Column(Binary, nullable=False)
    id_atendimento = Column(String, nullable=False)
    data_atendimento = Column(DateTime, nullable=False)