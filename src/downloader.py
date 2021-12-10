import requests
from urllib3.exceptions import InsecureRequestWarning
from utils import checkCreate
import json
import os
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
try:
    with open('constantes.json','r') as file:
        ENV=json.loads(file.read())
except Exception as e:
    print(f"Hubo un error al leer el archivo de constantes {e}")
    exit(1)

TRAINING_FOLDER=ENV['training']
def downloadFile2folder(file,folder):
    ''' Descarga un pdf de internet en un folder '''
    with open(file,'r') as file:
        for line in file:
            line=line.replace('\n','')
            line=line.split(' ')
            link=line[-1:][0]
            name="".join(line[:-1])+".pdf"
            name=name.replace(':','')
            try:
                response=requests.get(link, verify=False)
                if response.status_code==200:
                    if response.content[:4]==b'%PDF':
                        with open(folder+'/'+name,'wb') as pdf:
                            pdf.write(response.content)
                    else:
                        print(f"Error: No PDF {name} {response.status_code}: {link}")
                else:
                    print(f"Algo saló mal con {name} {response.status_code}: {link}")
            except Exception as e:
                print(f"Algo saló mal con {name} {response.status_code}: {link} {e}")

def downloadArticles():
    ''' Descarga todos los pdf que se encuentren en los links de los archivos de texto '''
    checkCreate(TRAINING_FOLDER)
    for file in os.listdir('./links'):
        if file[-3:]=="txt":
            label_folder=TRAINING_FOLDER+os.sep+file[:len(file)-4].upper()
            checkCreate(label_folder)
            downloadFile2folder('./links'+os.sep+file,label_folder)
if __name__=="__main__":
    downloadArticles()
