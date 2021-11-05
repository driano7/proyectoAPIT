# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
from fitz import open as open_pdf
import re
def clean_text(text:str)->str:
    text=text.lower()
    text = re.sub('[0-9]',' ',text)
    text=re.sub("[(),\.¿?\[\]=\-\+\*/:\\\_;%©>~\t&]",' ',text)
    text = re.sub('\n+',' ',text)
    text = re.sub(' +',' ',text)
    return text

class TextExtractor:
    def __init__(self,filePath:str):
        self.file=filePath
        try:
            self.pdf = open_pdf(self.file)
        except RuntimeError:
            print(f"No se pudo leer el archivo {self.file}")

    def pageRangeText(self,page_a:int,page_b:int)->list:
        text=''
        for i in range (page_a-1,page_b):
            page = self.pdf.loadPage(i)
            text+= page.getText("text")
        text=clean_text(text)
        return text.split()

    def getAllText(self,splited=True):
        text=''
        for i in range (0,len(self.pdf)):
            page = self.pdf.loadPage(i)
            text+= page.getText("text")
        text=clean_text(text)
        if splited:
            return text.split(' ')
        else:
            return text

if __name__=="__main__":
    import sys
    c1=TextExtractor(sys.argv[1])
    print(c1.getAllText())
    with open('flitz_test.txt','w') as file:
        file.write(" ".join(c1.getAllText()))
