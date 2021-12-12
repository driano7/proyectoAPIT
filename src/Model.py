# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
import pandas as pd
import os
from Preprocess import Preprocess
from TextExtractor import TextExtractor
from utils import checkCreate
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
        checkCreate(MODEL)

    def train(self):
        checkCreate(DATA)
        words_filepath=f"./{GLOBAL_COUNT}.json"
        labels_keys={} #{area:[palabras],area..}
        word_areas={} #Dict holding {word:num_areas_in_which_appears}
        try:
            with open(words_filepath,"r",encoding="utf-8") as file:
                word_areas=json.loads(file.read())
        except FileNotFoundError:
            print("No existía el archivos de palabras que cuenta todas las etiquetas")
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
                models[model[:-5]]=json.loads(file.read())
                results[model[:-5]]=0

        max=('',0)
        preproceser=Preprocess()
        input_representation=preproceser.countWords(text)
        for model in models.keys():
            # Se toman todas las palabras
            for key in list(input_representation.keys()):
                try:
                    results[model]+=models[model][key]
                except Exception:
                    # print(f"Llave no encontrada {key}")
                    pass
            results[model]=results[model]/preproceser.total_word_counter

        for area in results.keys():
            num_matches=results[area]
            print(f"{area} Las coincidencias son: {num_matches}")
            if num_matches>max[1]:
                max=(area,num_matches)
        if max[0]!='':
            print(f"El área predominante es {max[0]} con la suma: {max[1]}")
            return max[0]
        else:
            print("No se pudo reconocer")

if __name__=="__main__":
    from TextExtractor import TextExtractor
    model=Model()
    model.train()
