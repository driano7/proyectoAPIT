from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import json
import nltk
nltk.download('stopwords')
class Preprocess:
    ''' Esta clase se encarga de realizar el conteo de las palabras,
    realiza la radicalización (stemming) y filtra las stopwords
    a medida que cuenta las palabras.
    '''
    def __init__(self,file:str='global_count.json'):
        '''
        El constructor define un archivo en el que se almacenará el conteo de todalas
        las palabras que han pasado por el conteo.
        file (string): Archivo con el conteo absoluto de las palabras
        '''
        self.stemmer=SnowballStemmer("spanish")
        self.stopwords=stopwords.words("spanish")
        self.stopwords_en=stopwords.words("english")
        self.results=None
        self.filename=file
        self.total_word_counter=0
        self.loadWords()

    def loadWords(self):
        ''' Carga el conteo global almacenado en el archivo definido.
        Si no existe se creará (estando vacío al inicio)'''
        if self.filename:
            try:
                with open(self.filename,'r',encoding="utf-8") as file:
                    self.results=json.loads(file.read())
            except FileNotFoundError:
                print("No existe un archivo con las palabras")
                print("Se creará uno al iniciar el entrenamiento")
        else:
            print("Este archivo no es serialize porque no se definió el archivo")

    def countWords(self,words:list,**kwargs):
        ''' Se realiza el conteo de las palabras
        Params:
            word (lista[cadenas]): Una lista con la palabras a contar
        '''
        words_area=kwargs.get('words_area', False)
        if not self.results:
            self.results={}
        for word in words:
            if word not in self.stopwords and word not in self.stopwords_en and len(word)>2:
                # stem=word #Prueba
                stem=self.stemmer.stem(word)
                if stem not in self.results.keys():
                    self.results[stem]=1
                    self.total_word_counter+=1
                    if words_area:
                        if stem not in words_area.keys():
                            words_area[stem]=1
                            words_area['words_overall']+=1 #Ya no se usa, era un concepto erroneo
                        else:
                            words_area[stem]+=1
                    else:
                        pass
                        # print("Este no es un preprocesado de modelo")
                else:
                    self.results[stem]+=1
                    # print("Posterior palabra")
        self.results={
            k: v for k, v in
            sorted(self.results.items(), key=lambda item: item[1],reverse=True)
        }
        return self.results

    def normalize(self):
        ''' Se normaliza el número de apariciones de una palabra respecto al número
        de palabras que contaron'''
        self.results= { k: v/self.total_word_counter for k, v in
            sorted(self.results.items(), key=lambda item: item[1],reverse=True)
        }

    def serialize(self):
        ''' Se guarda un archivo con la forma
        {palabra_1:num_aparciones,palabra_1:num_aparciones ...} '''
        if self.filename:
            with open(self.filename,'w',encoding="utf-8") as file:
                file.write(json.dumps(self.results))
        else:
            print("No es serializable ya que no se definió el archivo para escribir")

if __name__=="__main__":
    from TextExtractor import TextExtractor
    file=TextExtractor('./papers/paper.pdf')
    text=file.pageRangeText(1,5)
    preproceser=Preprocess()
    preproceser.loadWords()
    preproceser.countWords(text)
