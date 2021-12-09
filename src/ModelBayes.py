# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
import pandas as pd
import os
from Preprocess import Preprocess
from TextExtractor import TextExtractor
import json
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import numpy as np
TRAINING='./training'
DATA='./data'
MODEL="./model"
GLOBAL_COUNT='words'
class ModelBayes:
    def __init__(self,file=None):
        self.areas=['Area1','Area2','Area3','Area4']
        self.translate_label=['AREA-I','AREA-II','AREA-III','AREA-IV']
        self.words={area:None for area in self.areas}
        self.file=None
        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        if file:
            self.file=file
        self.train()

    def train(self):
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
        print(labels)
        labels=np.array(labels)
        self.model.fit(archivos, labels)

    def classify(self,text):
        text=[text]
        labels = self.model.predict(text)
        print(labels)
        result=self.translate_label[labels[0]]
        print(result)

if __name__=="__main__":
    from TextExtractor import TextExtractor
    model=Model()
    model.train()
