# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
from fitz import open as open_pdf #Biblioteca para extraer texto de un PDF
import re #Bib de expresiones regulares

def clean_text(text:str)->str:
    ''' Se reemplazan caracteres no alfa numéricos por espacios
        y luego se reemplazan los espacios múltiples por uno solo
    '''
    text=text.lower()
    text = re.sub('[0-9]',' ',text)
    text=re.sub("[(),\.¿?\[\]=\-\+\*/:\\\_;%©>~\t&]",' ',text)
    text = re.sub('\n+',' ',text)
    text = re.sub(' +',' ',text)
    return text

class TextExtractor:
    ''' Esta clase extrae el texto de un pdf'''
    def __init__(self,filePath:str):
        ''' Constructor que recibe la ruta del pdf a leer'''
        self.file=filePath
        try:
            self.pdf = open_pdf(self.file)
        except RuntimeError:
            print(f"No se pudo leer el archivo {self.file}")

    def pageRangeText(self,page_a:int,page_b:int)->list:
        ''' regresa en una lista las palabras entre las páginas a y b'''
        text=''
        for i in range (page_a-1,page_b):
            page = self.pdf.loadPage(i)
            text+= page.getText("text")
        text=clean_text(text)
        return text.split()

    def getAllText(self,splited=True):
        ''' Se extrae todo el texto en el archivo (con el filtro de caracateres
        alfanuméricos)'''
        text=''
        for i in range (0,len(self.pdf)):
            page = self.pdf.loadPage(i)
            text+= page.getText("text")
        text=clean_text(text)
        if splited:
            return text.split(' ')
        else:
            return text

    def getFullText(self,splited=True):
        '''Se extrae todo el texto de archivo sin ninguna modificación '''
        text=''
        for i in range (0,len(self.pdf)):
            page = self.pdf.loadPage(i)
            text+= page.getText("text")
        return text

if __name__=="__main__":
    import sys
    c1=TextExtractor(sys.argv[1])
    print(c1.getAllText())
    with open('flitz_test.txt','w') as file:
        file.write(" ".join(c1.getAllText()))
