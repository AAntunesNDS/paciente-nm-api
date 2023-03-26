from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as EnumSQLAlchemy

Base = declarative_base()

class ProntuarioModel(Base):
    __tablename__ = "prontuario"

    id_prontuario = Column(Integer, primary_key=True, index=True)
    id_paciente = Column(Integer, nullable=False)
    data_nascimento = Column(DateTime, nullable=False)
    sexo = Column(String, nullable=False)
    texto_prontuario = Column(String, nullable=False)
    id_atendimento = Column(Integer, nullable=False)
    data_atendimento = Column(DateTime, nullable=False)