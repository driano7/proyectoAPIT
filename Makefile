run:
	python -B src/App.py
train:
	python -B src/Model.py
test2:
	python -B src/Preprocess.py
download_articles:
	python -B src/downloader.py
clean:
	rm -fr training_documents
	rm -fr validation_documents
	rm -f ./model/*
	rm -f ./data/*
	rm -f words.json
