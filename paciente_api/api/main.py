from fastapi import FastAPI
from app import router


app = FastAPI()

# Adiciona as rotas criadas no arquivo 'routes.py'
app.include_router(router)

# Configurações adicionais do FastAPI
# ...
# JWT Validation here?

# Inicializa o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)