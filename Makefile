# Arthur Antunes (c) Makefile for Paciente NM Backend
# Version: 0.1
# Language: Python
# Descrição dos comandos no README.md

.PHONY: build_api build_model

build_database:
	cd database; sudo docker-compose up -d

run_database:
	cd database; sudo docker-compose up

build_api:
	cd paciente_api/api/; poetry install; poetry shell; cd ..; cd ..;

run_api:
	export PYTHONPATH=${PWD}; cd paciente_api/api/; uvicorn main:app --reload;

build_rabbitmq_server:
	cd rabbitmq; docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management ;printf "Seu rabbitmq server já foi criado e está rodando! \nAgora entre no seu painel com o usuário:guest pswd:guest \nCrie uma exchange padrão chamada data_exchange\nCrie uma queue padrão chamada data_queue\n"

build_model:
	export PYTHONPATH=${PWD} && cd prontuario_classify/prontuario_classify/ && poetry install && poetry shell;  cd ..; cd ..;

run_model_consumer:
	export PYTHONPATH=${PWD}; cd prontuario_classify/prontuario_classify/; python3.8 classify.py

test:
	export PYTHONPATH=${PWD}; cd paciente_api; poetry run pytest;
