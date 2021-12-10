from os import path
import os
def checkCreate(folder):
    ''' Comprueba si existe una carpeta sino la crea '''
    if(not path.exists(folder)):
        os.mkdir(folder)
