import models, schemas, crud

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#from jose import JWTError, jwt
# JWT config
#SECRET_KEY = "mysecretkey"
#ALGORITHM = "HS256"
#ACCESS_TOKEN_EXPIRE_MINUTES = 30
#security = HTTPBearer()

@router.post("/create_prontuario", response_model=schemas.Prontuario)
async def prontuario_prontuario(prontuario: schemas.ProntuarioCreate, db: Session = Depends(get_db)):
    return crud.create_prontuario(db=db, prontuario=prontuario)


@router.get("/paciente_diagnostico")
async def prontuario_diagnostico(id_prontuario: str, id_atendimento: str):
    #TODO JWT VALIDATION
    '''
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username != "admin":
            raise HTTPException(status_code=403, detail="Não autorizado")
    except JWTError:
        raise HTTPException(status_code=403, detail="Não autorizado")
    '''

    prontuario = db.get(id_prontuario)
    if not prontuario or prontuario.id_atendimento != id_atendimento:
        raise HTTPException(status_code=404, detail="prontuario ou atendimento não encontrados")

    return prontuario

