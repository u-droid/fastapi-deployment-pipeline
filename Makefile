install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint app.py

format:
	black *.py

test:
	python -m pytest test_app.py