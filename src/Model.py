# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
import pandas as pd
import os
from Preprocess import Preprocess
from TextExtractor import TextExtractor
import json
TRAINING='./training'
DATA='./data'
MODEL="./model"
GLOBAL_COUNT='words'
class Model:
    def __init__(self,file=None):
        self.areas=['Area1','Area2','Area3','Area4']
        self.words={area:None for area in self.areas}
        self.file=None
        if file:
            self.file=file
            glosario = pd.read_csv('glosario.csv')
            for area in self.areas:
                   self.words[area]=glosario[area]

    def train(self):
        words_filepath=f"./{GLOBAL_COUNT}.json"
        labels_keys={} #{area:[palabras],area..}
        word_areas={} #Dict holding {word:num_areas_in_which_appears}
        try:
            with open(words_filepath,"r",encoding="utf-8") as file:
                word_areas=json.loads(file.read())
            pass
        except FileNotFoundError:
            word_areas={'words_overall':0}
        for area in os.listdir(TRAINING):
            print(f"Area: {area}")
            procesador=Preprocess(f"{DATA}/{area}.json")
            procesador.loadWords()
            for file in os.listdir(TRAINING+'/'+area):
                if file[-3:]=='pdf':
                    file=TextExtractor(TRAINING+'/'+area+'/'+file)
                    text=file.getAllText()
                    procesador.countWords(text,words_area=word_areas)
            procesador.normalize()
            labels_keys[area]=procesador.results.keys()
            procesador.serialize()

        with open(words_filepath,"w") as file:
            file.write(json.dumps(word_areas))
        for area in labels_keys.keys():
            model={}
            clean_model={}
            with open(f"{DATA}/{area}.json",'r',encoding="utf-8") as file:
                model=json.loads(file.read())
            for key in labels_keys[area]:
                # weight=(model[key]/word_areas['words_overall'])*(1/word_areas[key])
                weight=model[key]*(1/word_areas[key])
                clean_model[key]=weight
            # Sorting
            # clean_model={
            #     k: v for k, v in
            #     sorted(clean_model.items(), key=lambda item: item[1],reverse=True)
            # }
            with open(f"{MODEL}/{area}.json",'w',encoding="utf-8") as file:
                file.write(json.dumps(clean_model))

    def classify(self,text):
        results={}
        models={}
        for model in os.listdir(MODEL):
            with open(f'{MODEL}/{model}','r',encoding="utf-8") as file:
                models[model]=json.loads(file.read())
                results[model]=0

        max=('',0)
        preproceser=Preprocess()
        input_representation=preproceser.countWords(text)
        for model in models.keys():
            for key in list(input_representation.keys())[:25]:
                try:
                    results[model]+=models[model][key]
                except Exception:
                    # print(f"Llave no encontrada {key}")
                    pass

        for area in results.keys():
            num_matches=results[area]
            print(f"{area} Las coincidencias son: {num_matches}")
            if num_matches>max[1]:
                max=(area,num_matches)
        if max[0]!='':
            print(f"El área predominante es {max[0]} con: {max[1]} elementos")
        else:
            print("No se pudo reconocer")
        return results

if __name__=="__main__":
    from TextExtractor import TextExtractor
    model=Model()
    model.train()
