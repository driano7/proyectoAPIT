# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
import pandas as pd
import os
from Preprocess import Preprocess
from TextExtractor import TextExtractor

TRAINING='./training'
DATA='./data'
class Model:
    def __init__(self,file='glosario.csv'):
        self.areas=['Area1','Area2','Area3','Area4']
        self.words={area:None for area in self.areas}
        self.file=None
        if file:
            self.file=file
            glosario = pd.read_csv('glosario.csv')
            for area in self.areas:
                   self.words[area]=glosario[area]

    def train(self):
        try:
            for area in os.listdir(TRAINING):
                print(f"Area: {area}")
                procesador=Preprocess(f"{DATA}/{area}.json")
                procesador.loadWords()
                for file in os.listdir(TRAINING+'/'+area):
                    if file[-3:]=='pdf':
                        file=TextExtractor(TRAINING+'/'+area+'/'+file)
                        # text=file.pageRangeText(1,1)
                        text=file.getAllText()
                        procesador.countWords(text)
                procesador.serialize()


        except FileNotFoundError:
            print(f"No se encontró el folder de entrenamiento: {TRAINING}")

    def classify(self,text):
        results={area:-1 for area in self.areas}
        max=('',0)
        if self.file:
            for area in self.areas:
                results[area]=set(self.words[area]).intersection(text)

        for area in results.keys():
            num_matches=len(results[area])
            # if num_matches>0:
            print(f"{area} Las coincidencias son: {num_matches} {list(results[area])}")
            if num_matches>max[1]:
                max=(area,num_matches)
        if max[0]!='':
            print(f"El área predominante es {max[0]} con: {max[1]} elementos")
        else:
            print("No se pudo reconocer")
        return results

if __name__=="__main__":
    from TextExtractor import TextExtractor
    model=Model('glosario.csv')
    model.train()
    # file=TextExtractor('java.pdf')
    # text=file.pageRangeText(1,5)
    # model.classify(text)
