# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
from TextExtractor import TextExtractor
from Model import Model
from Stats import Stats
class CliUI:
    def __init__(self):
        self.model=Model('glosario.csv')
        self.default_files={
            '1':('Área I','./papers/paper.pdf'),
            '2':('Área II','./papers/Síndrome_de_Holmes.pdf'),
            '3':('Área III','./papers/Derecho_empresarial.pdf')
        }

    def loop(self):
        while True:
            print("PROGRAMA CLASIFICADOR DE TEMAS")
            for opt in self.default_files.keys():
                print(f"[{opt}]",self.default_files[opt][0],self.default_files[opt][1])
            print('[4]',"Salir")
            opt=input('Que archivo quieres leer? ')
            if opt !='4':
                try:
                    file=TextExtractor(self.default_files[opt][1])
                except RuntimeError:
                    print("No se encontró el archivo")
                    return
                a = input('Ingresa el inicio de las páginas a analizar: \n-->')
                b = input('Ingresa el fin de las páginas a analizar: \n-->')
                try:
                    text=file.pageRangeText(int(a),int(b))
                    results=self.model.classify(text)
                    stats=Stats()
                    stats.plot(results)
                except ValueError:
                    print("ERROR: El rango de páginas supera al número de páginas")

            else:
                exit()

if __name__=="__main__":
    ui=CliUI()
    try:
        ui.loop()
    except KeyboardInterrupt:
        print("Saliendo")
