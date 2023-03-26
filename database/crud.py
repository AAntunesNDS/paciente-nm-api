
from database import models, schemas

from sqlalchemy.orm import Session

def get_prontuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProntuarioModel).offset(skip).limit(limit).all()

def create_prontuario(db: Session, prontuario: schemas.ProntuarioCreate):
    db_prontuario = models.ProntuarioModel(**prontuario.dict())
    db.add(db_prontuario)
    db.commit()
    db.refresh(db_prontuario)
    return db_prontuario