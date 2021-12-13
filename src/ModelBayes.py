import pandas as pd
import os
from Preprocess import Preprocess
from TextExtractor import TextExtractor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import numpy as np
import json

try:
    with open('constantes.json','r') as file:
        ENV=json.loads(file.read())
except Exception as e:
    print(f"Hubo un error al leer el archivo de constantes {e}")
    exit(1)

TRAINING=ENV['training']
DATA=ENV['data']
MODEL=ENV['model']
GLOBAL_COUNT=ENV['global_count']
class ModelBayes:
    ''' Esta clase utiliza un clasificador bayesiano implementada por la
    bilbioteca scikitlearn'''
    def __init__(self,file=None):
        ''' El constructor hace una codificación a números de la etiquetas
        y comienza el entrenamiento con los archivos que se encuentran en las
        carpetas de entrenamiento
        '''
        self.translate_label=[]
        for area in os.listdir(TRAINING):
            self.translate_label.append(area)
        self.file=None
        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        if file:
            self.file=file
        self.train()

    def train(self):
        ''' En esta clase de realiza el entrenamiento tomando los archivos
        de la carpeta de entrenamiento, separa las etiquetas las traduce
        y realiza el ajuste del modelo.
        '''
        archivos=[]
        labels=[]
        text=""
        # Lectura de datos
        for area in os.listdir(TRAINING):
            # print(f"Area: {area}")
            for file in os.listdir(TRAINING+'/'+area):
                if file[-3:]=='pdf':
                    file=TextExtractor(TRAINING+'/'+area+'/'+file)
                    text=file.getAllText()
                    archivos.append(" ".join(text))
                    labels.append(area)
        # Adaptación para scikitlearn
        labels=[self.translate_label.index(label) for label in labels]
        labels=np.array(labels)
        self.model.fit(archivos, labels)

    def classify(self,text:str)->int:
        ''' Se realiza la predicción de un documento
        Parámetros
        text(string): Es el texto completo de un archivo pdf
        Regresa
        label(integer): La etiqueta que se determinó (codificada a entero)
        '''
        text=[text]
        labels = self.model.predict(text)
        result=self.translate_label[labels[0]]
        print(f"El área predominante es {result}")
        return result.upper()

if __name__=="__main__":
    from TextExtractor import TextExtractor
    model=ModelBayes()

    # model.train()
