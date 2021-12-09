from CliUI import CliUI
from Model import Model
from ModelBayes import ModelBayes
import sys
def clasify(filename):
    from TextExtractor import TextExtractor
    model=Model()
    file=TextExtractor(filename)
    #file=TextExtractor('papers/paper.pdf')
    # file=TextExtractor('papers/Síndrome_de_Holmes.pdf')
    text=file.getAllText()
    model.classify(text)
def clasify_bayes(filename):
    from TextExtractor import TextExtractor
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
