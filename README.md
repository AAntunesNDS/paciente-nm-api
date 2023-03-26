# prontuario-nm-api
Web Api desafio NeuralMed

# Clone project

# Add poetry
    Para rodar a aplicação e, ambiente de desenvolvimento, de forma local, é necessário ter a o gerenciador de dependências Poetry instalado.
    * necessario estar dentro da pasta de algum serviço
    /prontuario_api
    /prontuario_model
    
    - poetry env use 3.8 indica versao do python utilizada para virtal env
    - poetry install cria env e instalar as dependencias
    - poetry shell (para ativar a env ja existente)

# DockerFiles
    Docker para subir banco postgres local dentro da pasta /docker_postgres é nécessário que a porta 5432 esteja livre para subir essa imagem!
    

###to do\/
# Create Makefile
    make build
    make test
    make deploy
