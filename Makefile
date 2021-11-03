run:
	python -B src/App.py
train:
	python -B src/Model.py
test2:
	python -B src/Preprocess.py
clean:
	rm -f ./model/*
	rm -f ./data/*
	rm -f words.json
