install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv test_application.py

lint:
	pylint --disable=R,C app.py

deploy:
	echo "Deploying app"
	eb deploy cryptoapp-continuous-delivery-env

all: install lint test 