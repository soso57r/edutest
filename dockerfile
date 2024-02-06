FORM python:3.11
WORKDIR /master/edutest 

pip install -r requirements.txt
pip install -e .
pytest # to run tests
pylint src && flake8 # to lint
bandit -r src # to run security tests
