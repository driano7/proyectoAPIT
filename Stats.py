from matplotlib import pyplot as plt
from matplotlib.pyplot import *
class Stats:
    def __init__(self):
        pass
    def plot(self,resultados:dict):
        plt.bar(resultados.keys(),
            [len(palabras) for palabras in resultados.values()],
            color=['blue','orange','green','purple'])
        plt.ylabel("Palabras", fontsize=12)
        plt.legend()
        plt.grid(True)
        plt.show()
