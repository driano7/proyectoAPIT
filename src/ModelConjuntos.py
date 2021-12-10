# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
import pandas as pd

class ModelConjuntos:
    ''' Esta clase implementa el método 1
        En este método se creó un glosario con el campo semántico de cada etiqueta
        como modelo. Para representar a la entrada se cargaron todas la palabras
        en una lista de cadenas. Finalmente para la función de comparación se
        realizó la intersección de ambos conjuntos (model y entrada) y se contaron
        las coincidencias
    '''
    def __init__(self,file='glosario.csv'):
        self.areas=['Area1','Area2','Area3','Area4']
        self.words={area:None for area in self.areas}
        self.file=None
        if file:
            self.file=file
            glosario = pd.read_csv(file)
            for area in self.areas:
                   self.words[area]=glosario[area]

    def classify(self,text):
        results={area:-1 for area in self.areas}
        max=(self.areas[0],0)
        if self.file:
            for area in self.areas:
                results[area]=set(self.words[area]).intersection(text)

        for area in results.keys():
            num_matches=len(results[area])
            if num_matches>0:
                print(f"{area} Las coincidencias son: {num_matches}")
                if num_matches>max[1]:
                    max=(area,num_matches)
        print(f"El área predominante es {max[0]} con: {max[1]} elementos")

if __name__=="__main__":
    from TextExtractor import TextExtractor
    model=ModelConjuntos(file='../glosario.csv')
    file=TextExtractor('../test/wiki_java.pdf')
    text=file.getAllText()
    model.classify(text)
