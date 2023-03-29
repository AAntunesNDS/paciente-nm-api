<h1 align="center">Paciente NM Backend</h1>

<p align="center">Backend de uma aplicação de classificação automática de diagnósticos</p>

## Descrição do projeto

Esse projeto é uma proposta de backend para uma aplicação que faz diagnósticos de prontuários médicos. 
Estruturalmente ele é dividido em 4 partes; 
- Uma API Rest (FastAPI) que vai servir de interface de dados dos prontuários e diagnósticos (Post e Get);
- Banco de Dados realcional (PostgresSQL) que salva os dados dos prontuários e diagnósticos como metadados;
- Um [modelo de classificação de linguagem (NLP)](https://huggingface.co/pucpr/clinicalnerpt-disorder/tree/main) que vai receber o texto de pronturário e classificar os tokens;
- E um servidor simples de mensageria (RabbitMQ) que vai ser utilizado para consumir os dados da api pelo modelo de classificação de dados.


### Pré-requisitos

Para rodar o projeto é preciso ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python 3.8](https://www.python.org/downloads/release/python-380/) e o gerenciador de dependencias [Poetry](https://python-poetry.org/). 
Também será necessária a instalção global libpq-dev para as permissões necessárias do Postgres:

```bash
sudo apt install python3-dev libpq-dev
```

### Setup Inicial

```bash
# Clone este repositório
$ git clone https://github.com/AAntunesNDS/file_system_api.git

# Crie uma instância postgres com docker-compose (se você já tiver um postgres na porta 5432 pode dar conflito. Se certifique que não tem)
$ make build_database

# Agora rode essa instancia
$ make run_database

# Instala as dependências da API 
$ make build_api

# Suba o servidor da API local. Interagir com os endpoint no link: http://localhost:8000/docs
$ make run_api

# Cria e sobe uma imagem docker de um servidor de rabbitmq na porta 15672.]
# Nesse ponto você deve entrar no link http://localhost:15672/ e criar uma exchange e uma queue chamadas data_exchange, data_queue
$ make build_rabbitmq_server

# Instala as dependências do modelo de classificação de diagnõsticos
$ make build_model

# Abre um consumidor de mensagens da queue criada anteriormente no build_rabbitmq_server
$ make run_model_consumer

# Roda os testes unitários
$ make test

```


![alt text](https://github.com/AAntunesNDS/paciente-nm-api/blob/main/documentation/arquitetura_desafio_neuralmed.jpg)