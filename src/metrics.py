import os
import json
from Model import Model
from ModelBayes import ModelBayes
from ModelConjuntos import ModelConjuntos
from TextExtractor import TextExtractor

try:
    with open('constantes.json','r') as file:
        ENV=json.loads(file.read())
except Exception as e:
    print(f"Metrics.py: Hubo un error al leer el archivo de constantes {e}")
    exit(1)

TRAINING_FOLDER=ENV['training']
VALIDATION_FOLDER=ENV['validation']

# model1=ModelConjuntos('glosario.csv')
# model2=Model()
# model3=ModelBayes()
# resultados={}
# etiquetas_determinadas=[]
# for area in os.listdir(VALIDATION_FOLDER):
#     resultados[area]=[]
#     for file in os.listdir(VALIDATION_FOLDER+os.sep+area):
#         if file[-3:]=='pdf':
#             etiqueta_determinada=[-1,-1,-1]
#             pdf=TextExtractor(VALIDATION_FOLDER+'/'+area+'/'+file)
#             text=pdf.getAllText()
#             etiqueta_determinada[0]=model1.classify(text)
#             etiqueta_determinada[1]=model2.classify(text)
#             etiqueta_determinada[2]=model3.classify(" ".join(text))
#             resultados[area].append(etiqueta_determinada)
# print(etiquetas_determinadas)
resultados={}
with open('datos_metricas.json','r') as file:
    resultados=json.loads(file.read())
def calcularMetricas(num_modelo):
    etiquetados_incorrectos={area:0 for area in resultados.keys()}
    etiquetados_correctos={area:0 for area in resultados.keys()}
    total=0
    correctos=0
    for area in resultados.keys():
        for etiqueta in resultados[area]:
            total+=1
            if etiqueta[num_modelo]==area:
                etiquetados_correctos[area]+=1
                correctos+=1
            else:
                etiquetados_incorrectos[etiqueta[num_modelo]]+=1
    print(f"correctos: {correctos} incorrectos: {total-correctos}")
    print(f"Exactitud {correctos/(total-correctos)}")
    for area in resultados.keys():
        # NUMERO DE DOCUMENTOS REALES DE ESA ETIQUETA
        num_docs=len(resultados[area])
        # NUMERO DE DOCUMENTOS ETIQUETADOS CON ESTA ETIQUETA
        num_etiquetados=etiquetados_correctos[area]+etiquetados_incorrectos[area]
        # NÚMERO DE DOCUMENTOS DE OTRA ETIQETA NO ETIQUETADOS
        no_etiquetados_correctos=total-num_docs-etiquetados_incorrectos[area]
        # Métricas
        exactitud=(etiquetados_correctos[area]+no_etiquetados_correctos)/(total)
        precision=(etiquetados_correctos[area]/num_docs)
        if num_etiquetados>0:
            recall=(etiquetados_correctos[area]/num_etiquetados)
            f1=2*(precision*recall)/(precision+recall)
        else:
            recall=0.0
            f1=0.0
        print(area)
        print(f"Exactitud:{exactitud}")
        print(f"Precisión:{precision}")
        print(f"Recall:{recall}")
        print(f"F1:{f1}")
print("Métricas método 1")
calcularMetricas(0)
print("Métricas método 2")
calcularMetricas(1)
print("Métricas método 3")
calcularMetricas(2)
