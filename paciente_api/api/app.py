from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from models import Pacientes


router = APIRouter()

# JWT config
#SECRET_KEY = "mysecretkey"
#ALGORITHM = "HS256"
#ACCESS_TOKEN_EXPIRE_MINUTES = 30
#security = HTTPBearer()

# fake database
db = {}


@router.post("/paciente_prontuario")
async def paciente_prontuario(pacientes: Pacientes):
    for paciente in pacientes.pacientes:
        db[paciente.id_paciente] = paciente
    return {"msg": "Dados salvos com sucesso!", "pacientes_ids" : f'{list(db)}'}


@router.get("/paciente_diagnostico")
async def paciente_diagnostico(id_paciente: str, id_atendimento: str):
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

    paciente = db.get(id_paciente)
    if not paciente or paciente.id_atendimento != id_atendimento:
        raise HTTPException(status_code=404, detail="Paciente ou atendimento não encontrados")

    return paciente

