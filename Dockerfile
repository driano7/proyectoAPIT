FROM python:3.8-slim-buster
ADD ./links /links
ADD ./src /src
ADD ./test /test
ADD ./app /app
ADD ./glosario.csv /glosario.csv
ADD ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN python -B ./links/downloader.py
CMD [ "bash", "app" ,"test/wiki_java.pdf" ]
