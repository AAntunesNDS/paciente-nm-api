import os, sys
sys.path.insert(1, os.path.abspath(os.path.join(__file__ ,"../../..")))

from transformers import AutoModelForTokenClassification, AutoTokenizer
from database.crud import create_diagnostico
from database.database import SessionLocal
from database.schemas import Diagnostico, DiagnosticoCreate
from rabbitmq import consumer, publisher
import torch

Session = SessionLocal()

class Model():
    tokenizer = AutoTokenizer.from_pretrained("pucpr/clinicalnerpt-disorder")
    model = AutoModelForTokenClassification.from_pretrained("pucpr/clinicalnerpt-disorder")
    disorders = []

    def classify_disorder(self, input_text = None):
        if not input_text:
            input_text = "Paciente com CA de mama, histórico de diabetes mellitus"

        # tokenization
        inputs = self.tokenizer(input_text, max_length=512, truncation=True, return_tensors="pt")
        tokens = inputs.tokens()

        # get predictions
        outputs = self.model(**inputs).logits
        predictions = torch.argmax(outputs, dim=2)

        # print predictions
        for token, prediction in zip(tokens, predictions[0].numpy()):
            classificado = self.model.config.id2label[prediction]
            if classificado[0] == 'B':
                print((token, classificado))
                self.disorders.append(token)
        
        return self

import json
import random

def classify_callback(ch, method, properties, body):
    #try:
    prontuario = json.loads(body.decode('utf-8'))
    print(prontuario)
    classify = Model().classify_disorder(prontuario["texto_prontuario"])
    
    for disorder in classify.disorders:
        new_diagnostico = Diagnostico(
            id_paciente = prontuario["id_paciente"], 
            id_atendimento = prontuario["id_atendimento"],
            disorder = disorder,
            flag_ca = True if disorder == 'ca' else False
        )
        create_diagnostico(Session, new_diagnostico)
    #except:
    #    print("Callback exception")
    #    pass

def main():
    '''
    {"id_paciente": 2, "data_nascimento": "2023-03-26T22:01:19.457Z","sexo": "M","texto_prontuario": "Paciente com CA de mama, histórico de diabetes mellitus","id_atendimento": 3,"data_atendimento": "2023-03-26T22:01:19.457Z"}
    '''

    rabitmq_consumer = consumer.RabbitmqConsumer(classify_callback)
    rabitmq_consumer.start()


main()