# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
from TextExtractor import TextExtractor
from Model import Model

class CliUI:
    def __init__(self):
        print("Hola mundo")
        self.model=Model('glosario.csv')

    def loop(self):
        while True:
            print("PROGRAMA CLASIFICADOR DE TEMAS")
            file=input('Que archivo quieres leer? ')
            print(file)
            file=TextExtractor(file)
            a = input('Ingresa el inicio de las páginas a analizar: \n-->')
            b = input('Ingresa el fin de las páginas a analizar: \n-->')
            text=file.pageRangeText(int(a),int(b))
            self.model.classify(text)

if __name__=="__main__":
    ui=CliUI()
    ui.loop()
