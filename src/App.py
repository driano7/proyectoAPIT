from CliUI import CliUI
from ModelConjuntos import ModelConjuntos
from Model import Model
from ModelBayes import ModelBayes
from TextExtractor import TextExtractor
import sys

def clasify(filename):
    model=Model()
    file=TextExtractor(filename)
    text=file.getAllText()
    model.classify(text)


def clasify_conjuntos(filename):
    model=ModelConjuntos('glosario.csv')
    file=TextExtractor(filename)
    text=file.getAllText()
    model.classify(text)

def clasify_bayes(filename):
    model=ModelBayes()
    file=TextExtractor(filename)
    text=file.getAllText()
    model.classify(" ".join(text))

if __name__=="__main__":
    # ui=CliUI()
    # try:
    #     ui.loop()
    # except KeyboardInterrupt:
    #     print("Saliendo")
    file=sys.argv[1]
    clasify(file)
    # clasify_bayes(file)
    # clasify_conjuntos(file)
