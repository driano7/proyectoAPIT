# Autor original Donovan Riaño Enriquez, APIT 2021-2
# Modificado por Ángel Santander
import fitz #para leer pdf

class TextExtractor:
    def __init__(self,filePath:str):
        self.file=filePath
        self.pdf = fitz.open(self.file)
    def pageRangeText(self,page_a:int,page_b:int):
        text=''
        for i in range (page_a-1,page_b):
            page = self.pdf.loadPage(i)
            text+= page.getText("text")
        return text.split()
if __name__=="__main__":
    c1=TextExtractor('paper.pdf')
    print(c1.pageRangeText(1,5).split())
