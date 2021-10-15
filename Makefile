run:
	python -B src/App.py
test:
	python -B src/Model.py
test2:
	python -B src/Preprocess.py 
clean:
	rm -f ./model/*
	rm -f ./data/*
	rm words.json
