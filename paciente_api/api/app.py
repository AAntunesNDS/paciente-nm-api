
import os, sys
sys.path.insert(1, os.path.abspath(os.path.join(__file__ ,"../../..")))


from database import models, crud, schemas
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_prontuario", response_model=schemas.Prontuario)
async def create_prontuario(prontuario: schemas.ProntuarioCreate, db: Session = Depends(get_db)):
    return crud.create_prontuario(db=db, prontuario=prontuario)

@router.get("/get_prontuarios")
async def get_prontuarios(db: Session = Depends(get_db)):
    prontuarios = crud.get_prontuarios(db)
    if not prontuarios:
        raise HTTPException(status_code=404, detail="prontuario ou atendimento não encontrados")
    return prontuarios

@router.get("/get_diagnostico")
async def get_diagnostico(id_paciente: int, id_atendimento: int, db: Session = Depends(get_db)):
    diagnosticos = crud.get_diagnostico(db, id_paciente, id_atendimento)
    if not diagnosticos:
        raise HTTPException(status_code=404, detail="diagnostico não encontrado")

    return diagnosticos

