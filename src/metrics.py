import os
import json
from Model import Model
from ModelBayes import ModelBayes
from ModelConjuntos import ModelConjuntos
from TextExtractor import TextExtractor
from matplotlib import pyplot as plt
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
def graficar(metricas,titulo):
    '''Gráfica las métricas un modelo '''
    figure=plt.figure(figsize=(12,4))
    ax_exactitud=figure.add_subplot(1,4,1)
    ax_presicion=figure.add_subplot(1,4,2)
    ax_recall=figure.add_subplot(1,4,3)
    ax_f1=figure.add_subplot(1,4,4)
    ax_exactitud.set_title("Exactitud")
    ax_presicion.set_title("Precisión")
    ax_recall.set_title("Recall")
    ax_f1.set_title("F1")

    for i,area in enumerate(metricas.keys(),start=1):
        ax_exactitud.bar(i,metricas[area][0])#Grafica los datos de exactitud
        ax_presicion.bar(i,metricas[area][1])#Grafica los datos de presición
        ax_recall.bar(i,metricas[area][2])#Grafica los datos de recall
        ax_f1.bar(i,metricas[area][3])#Grafica los datos de f1

    labels=metricas.keys()
    for ax in [ax_exactitud,ax_presicion,ax_recall,ax_f1]:
        ax.set_xticks(range(1,len(labels)+1))
        ax.set_xticklabels(labels)
        ax.legend()
    figure.suptitle(titulo, fontsize=16)
    figure.show()

def graficar_modelos(metricas,titulo):
    '''Gráfica las métricas generales de los modelos '''
    figure=plt.figure(figsize=(12,4))
    ax=figure.add_subplot(1,1,1)

    ax.bar(1,metricas['0'])
    ax.bar(2,metricas['1'])
    ax.bar(3,metricas['2'])

    labels=['Modelo 1','Modelo 2','Modelo 3']
    ax.set_xticks(range(1,len(labels)+1))
    ax.set_xticklabels(labels)
    ax.legend()
    figure.suptitle(titulo, fontsize=16)
    figure.show()
    input()

resultados={}
with open('datos_metricas.json','r') as file:
    resultados=json.loads(file.read())

def calcularMetricas(num_modelo,metricas_modelo):
    ''' Regresa un diccionario de la forma
    {etiqueta1:(exactitud,precisión,recall,f1),
    etiqueta2:(exactitud,precisión,...),
    ...}
    '''
    metricas={area:None for area in resultados.keys()}
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
    metricas_modelo[str(num_modelo)]=correctos/(total-correctos)
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
        metricas[area]=(exactitud,precision,recall,f1)
        print(area)
        print(f"Exactitud:{exactitud}")
        print(f"Precisión:{precision}")
        print(f"Recall:{recall}")
        print(f"F1:{f1}")
    return metricas

metricas_modelos={}
print("Métricas método 1")
graficar(calcularMetricas(0,metricas_modelos),"Método 1")
print("Métricas método 2")
graficar(calcularMetricas(1,metricas_modelos),"Método 2")
print("Métricas método 3")
graficar(calcularMetricas(2,metricas_modelos),"Método 3")
graficar_modelos(metricas_modelos,'Métricas generales de los modelos')
