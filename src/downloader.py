import requests
from urllib3.exceptions import InsecureRequestWarning
from utils import checkCreate
import json
import random
import os

random.seed(1)
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
try:
    with open('constantes.json','r') as file:
        ENV=json.loads(file.read())
except Exception as e:
    print(f"Hubo un error al leer el archivo de constantes {e}")
    exit(1)

TRAINING_FOLDER=ENV['training']
VALIDATION_FOLDER=ENV['validation']

def downloadFile2folder(name_link_list,folder):
    ''' Descarga un pdf de internet en un folder '''
    for item in name_link_list:
        name=item[0]
        link=item[1]
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
            print(f"Algo saló mal con {name}: {link} {e}")

def getLinks(file):
    links=[]
    with open(file,'r') as file:
        for line in file:
            line=line.replace('\n','')
            line=line.split(' ')
            link=line[-1:][0]
            name="".join(line[:-1])+".pdf"
            name=name.replace(':','')
            links.append((name,link))
    return links

def downloadArticles():
    ''' Descarga todos los pdf que se encuentren en los links de los archivos de texto '''
    checkCreate(TRAINING_FOLDER)
    checkCreate(VALIDATION_FOLDER)
    for file in os.listdir('./links'):
        if file[-3:]=="txt":
            links=[]
            links=getLinks('./links'+os.sep+file)
            label_folder_training=TRAINING_FOLDER+os.sep+file[:len(file)-4].upper()
            label_folder_validation=VALIDATION_FOLDER+os.sep+file[:len(file)-4].upper()
            checkCreate(label_folder_training)
            checkCreate(label_folder_validation)
            validation=random.sample(links,int(len(links)*.2))
            training=[link for link in links if link not in validation]
            with open('links_validacion.txt','a') as file:
                for link in validation:
                    file.write(f'{link[0]}'+link[1]+'\n')
            downloadFile2folder(training,label_folder_training)
            downloadFile2folder(validation,label_folder_validation)

if __name__=="__main__":
    downloadArticles()
