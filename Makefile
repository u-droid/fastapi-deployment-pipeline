install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint app/

format:
	black *.py

test:
	python -m pytest test_app.py