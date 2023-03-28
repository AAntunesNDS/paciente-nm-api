from fastapi import FastAPI
from paciente_api.api.api import router

description = """
PacienteApp API. 🚀
"""

app = FastAPI(
    title="PacienteApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Arthur Antunes",
        "email": "arthur.antunes.aa@gmail.com",
    },
)


# Adiciona as rotas criadas no arquivo 'routes.py'
app.include_router(router)

# Configurações adicionais do FastAPI
# ...

# Inicializa o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)