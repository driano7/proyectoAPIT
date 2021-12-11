import os
import json
from Model import Model
from ModelBayes import ModelBayes
from ModelConjuntos import ModelConjuntos
from TextExtractor import TextExtractor

try:
    with open('constantes.json','r') as file:
        ENV=json.loads(file.read())
except Exception as e:
    print(f"Metrics.py: Hubo un error al leer el archivo de constantes {e}")
    exit(1)

TRAINING_FOLDER=ENV['training']
VALIDATION_FOLDER=ENV['validation']

model1=ModelConjuntos('glosario.csv')
model2=Model()
model3=ModelBayes()
etiquetas_correctas=[]
etiquetas_determinadas=[]
for area in os.listdir(VALIDATION_FOLDER):
    for file in os.listdir(VALIDATION_FOLDER+os.sep+area):
        if file[-3:]=='pdf':
            etiquetas_correctas.append(area)
            etiqueta_determinada=[-1,-1,-1]
            pdf=TextExtractor(VALIDATION_FOLDER+'/'+area+'/'+file)
            text=pdf.getAllText()
            etiqueta_determinada[0]=model1.classify(text)
            try:
                etiqueta_determinada[1]=model2.classify(text)
            except:
                print(f"Error: {text}")
                print(f"arcivo: {file}")
                exit()
            etiqueta_determinada[2]=model3.classify(" ".join(text))
            etiquetas_determinadas.append(etiqueta_determinada)
print(etiquetas_determinadas)
print(etiquetas_correctas)
