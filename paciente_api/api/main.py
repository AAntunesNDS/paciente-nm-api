from fastapi import FastAPI
from app import router
import sys

#sys.path.insert(1, '/home/aantunesnds/Desktop/desafio_neural_med/paciente-nm-api')

sys.path.append('../')

app = FastAPI()

# Adiciona as rotas criadas no arquivo 'routes.py'
app.include_router(router)

# Configurações adicionais do FastAPI
# ...

# Inicializa o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)