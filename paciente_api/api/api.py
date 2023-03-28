from database import models, crud, schemas
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from rabbitmq.publisher import RabbitmqPublisher
from paciente_api.exceptions import RabbitmqException, DatabaseException, BadRequestException

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
    # Handle any bad request errors
    if not prontuario:
        raise BadRequestException()
    
    try:
        # Publish message to RabbitMQ
        RabbitmqPublisher().send_message(body = prontuario.json())
    except Exception as e:
        raise RabbitmqException()

    try:
        # Create prontuario in database
        return crud.create_prontuario(db=db, prontuario=prontuario)
    except Exception as e:
        raise DatabaseException()

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

