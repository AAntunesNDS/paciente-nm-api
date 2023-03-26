
from database import models, schemas

from sqlalchemy.orm import Session

def get_prontuarios(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(models.ProntuarioModel).offset(skip).limit(limit).all()
    except:
        print('Morreu aqui')


def create_prontuario(db: Session, prontuario: schemas.ProntuarioCreate):
    db_prontuario = models.ProntuarioModel(**prontuario.dict())
    db.add(db_prontuario)
    db.commit()
    db.refresh(db_prontuario)
    return db_prontuario

def get_diagnostico(db: Session, id_paciente, id_atendimento, skip: int = 0, limit: int = 100):
    return db.query(models.DiagnosticoModel).filter_by(id_paciente=id_paciente, id_atendimento=id_atendimento).offset(skip).limit(limit).all()

def create_diagnostico(db: Session, prontuario: schemas.DiagnosticoCreate):
    db_diagnostico = models.DiagnosticoModel(**prontuario.dict())
    db.add(db_diagnostico)
    db.commit()
    db.refresh(db_diagnostico)
    return db_diagnostico