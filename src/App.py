from CliUI import CliUI
from Model import Model
import sys
def clasify(filename):
    from TextExtractor import TextExtractor
    model=Model()
    file=TextExtractor(filename)
    #file=TextExtractor('papers/paper.pdf')
    # file=TextExtractor('papers/Síndrome_de_Holmes.pdf')
    text=file.getAllText()
    model.classify(text)

if __name__=="__main__":
    # ui=CliUI()
    # try:
    #     ui.loop()
    # except KeyboardInterrupt:
    #     print("Saliendo")
    file=sys.argv[1]
    clasify(file)
