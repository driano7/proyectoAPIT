# proyectoAPIT

En este proyecto de intentó realizar un clasificador de textos en 4 áreas del conocimiento.

## Instalación
### Para descargar los artículos
python -B src/downloader.py
### Para realizar el entregamiento del segundo modelo
python -B src/Model.py


## Ejecución

./app -<i|c|b> <pdf_file_path> <br>
o alternativamente <nr>
python -B src/App.py -<i|c|b> <pdf_file_path> <br>
  -h, --help  muestra la ayuda <br>
  -i          Clasifica utilizando la intersección de conjuntos <br>
  -c          Clasifica utilizando el conteo <br>
  -b          Clasifica utilizando el clasificador bayesiano <br>
### Ejecución de las métricas
python -B src/metrics.py


# capturas
## Intersección de conjuntos (campos semánticos)
![Screenshot](screenshots/modelo_conjuntos.png?raw=true "Modelo de conjutos")
## Conteo
![Screenshot](screenshots/modelo_propio.png?raw=true "Modelo utilizando conteo")
## Clasificador bayesiano
![Screenshot](screenshots/modelo_bayes.png?raw=true "Modelo de bayes ingenuo")

# Métricas
## Métricas generales
![Screenshot](screenshots/metricas/Figure_0.png?raw=true "Generales")
## Intersección de conjuntos (campos semánticos)
![Screenshot](screenshots/metricas/Figure_1.png?raw=true "Modelo de conjuntos")
## Conteo
![Screenshot](screenshots/metricas/Figure_2.png?raw=true "Modelo utilizando conteo")
## Clasificador bayesiano
![Screenshot](screenshots/metricas/Figure_3.png?raw=true "Modelo de bayes ingenuo")
