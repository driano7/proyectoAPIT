from ModelConjuntos import ModelConjuntos
from Model import Model
from ModelBayes import ModelBayes
from TextExtractor import TextExtractor
import argparse
import sys

def clasify(filename:str):
    model=Model()
    file=TextExtractor(filename)
    text=file.getAllText()
    model.classify(text)

def clasify_conjuntos(filename:str):
    model=ModelConjuntos('glosario.csv')
    file=TextExtractor(filename)
    text=file.getAllText()
    model.classify(text)

def clasify_bayes(filename:str):
    model=ModelBayes()
    file=TextExtractor(filename)
    text=file.getAllText()
    model.classify(" ".join(text))

if __name__=="__main__":
    ''' Se definen banderas para que el usuario pueda seleccionar el algoritmo a utilizar al clasificar '''
    parser = argparse.ArgumentParser(description='Este programa ejecuta los tres intentos de clasificador de textos realizados en este proyecto.')
    parser.add_argument('-i', dest='interseccion', action='store_const',const=True,
                        help='Clasifica utilizando la intersección de conjuntos')
    parser.add_argument('-c', dest='conteo', action='store_const',const=True,
                        help='Clasifica utilizando el conteo')
    parser.add_argument('-b', dest='bayes', action='store_const',const=True,
                        help='Clasifica utilizando el clasificador bayesiano')
    parser.add_argument('file', type=str,
                    help='Archvio a clasificar')

    args = parser.parse_args()
    file=args.file
    if args.interseccion:
        clasify_conjuntos(file)
    elif args.conteo:
        clasify(file)
    elif args.bayes:
        clasify_bayes(file)
