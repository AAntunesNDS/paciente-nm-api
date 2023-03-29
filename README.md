<h1 align="center">Paciente NM Backend</h1>

<p align="center">Backend de uma aplicação de classificação automática de diagnósticos</p>

## Descrição do projeto

Esse projeto é uma proposta de backend para uma aplicação que faz diagnósticos de prontuários médicos. 
Estruturalmente ele é dividido em 4 partes; 
- Uma API Rest (FastAPI) que vai servir de interface de dados dos prontuários e diagnósticos (Post e Get);
- Banco de Dados realcional (PostgresSQL) que salva os dados dos prontuários e diagnósticos como metadados;
- Um [modelo de classificação de linguagem (NLP)](https://huggingface.co/pucpr/clinicalnerpt-disorder/tree/main) que vai receber o texto de pronturário e classificar os tokens;
- E um servidor simples de mensageria (RabbitMQ) que vai ser utilizado para consumir os dados da api pelo modelo de classificação de dados.

![alt text](https://github.com/AAntunesNDS/paciente-nm-api/blob/main/documentation/arquitetura_desafio_neuralmed.jpg)

### Pré-requisitos

Para rodar o projeto é preciso ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python 3.8](https://www.python.org/downloads/release/python-380/), o gerenciador de dependencias [Poetry](https://python-poetry.org/) o [Docker](https://docs.docker.com/engine/install/) e o [Docker-Compose](https://www.digitalocean.com/community/tutorial_collections/how-to-install-docker-compose). 
Também será necessária a instalção global libpq-dev para as permissões necessárias do Postgres:

```bash
sudo apt install python3-dev libpq-dev
```

### Setup Inicial

```bash
# Clone este repositório
$ git clone https://github.com/AAntunesNDS/paciente-nm-api.git

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
# Além disso você precisa "bindar" a data_exchange na data_queue. Isso também deve ser feito pelo serviodor local do rabbitmq
$ make build_rabbitmq_server

# Instala as dependências do modelo de classificação de diagnõsticos
$ make build_model

# Abre um consumidor de mensagens da queue criada anteriormente no build_rabbitmq_server
$ make run_model_consumer

# Roda os testes unitários
$ make test

```

### Instruções adicionais

Nesse momento, você já tem tudo que é necessário para fazer um teste da aplicação. 
Entre no link de swagger da API: http://localhost:8000/docs e utilize a rota /create_prontuario para criar um prontuário.
Você deve editar o campo "texto_prontuario" com um texto real de prontuario como o passado no teste:

'Paciente com CA de mama, histórico de prontuarios mellitus'

Ao executar, o registro do pontuario foi criado na base Postgres. Além disso, o corpo da requisição foi enviada como mensagem para
a queue criada anteriormente do rabbitmq, deve ter sido processada, classificada, e salva no banco de dados Postgres novamente.
No terminal que foi executado o 'make run_model_consumer' aparece o log desse processo.

Voce pode voltar no swagger e bater na rota /get_diagnóstico, passando id do paciente e id do atendimento utilizadas na criação do prontuario.


### Observações finais

Alguns pontos de melhoria para o projeto atual:

- Criar mais testes unitários, desenvolvendo a prática de TDD
- Ao invés de requisitar o modelo de forma online, baixar os pesos para o ambiente local para fazer a predição de forma mais rápida
- Explorar mais a capacidade do RabbitMQ 
- Ajustar CI no github para validar testes uniarios em cada PR
- Admistrar melhor as envs de segurança, seja usando .env ou algum serviço gerenciado.

 Sugestões? Abre um PR e seja feliz =D