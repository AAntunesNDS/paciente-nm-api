from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch


# Load model
tokenizer = AutoTokenizer.from_pretrained("pucpr/clinicalnerpt-disorder")
model = AutoModelForTokenClassification.from_pretrained("pucpr/clinicalnerpt-disorder")


# Receive and preprocess input
input_text = "Paciente com CA de mama, histórico de diabetes mellitus"

# tokenization
inputs = tokenizer(input_text, max_length=512, truncation=True, return_tensors="pt")
tokens = inputs.tokens()

# get predictions
outputs = model(**inputs).logits
predictions = torch.argmax(outputs, dim=2)

# print predictions
for token, prediction in zip(tokens, predictions[0].numpy()):
    print((token, model.config.id2label[prediction]))