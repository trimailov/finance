all: env pip

.PHONY: env
env:
	pyvenv-3.5 env

.PHONY: pip
pip:
	env/bin/pip install -r requirements.txt

.PHONY: run
run:
	env/bin/python manage.py runserver 0.0.0.0:8080

.PHONY: migrate
migrate:
	env/bin/python manage.py migrate

.PHONY: clean_cache
clean_cache:
	find **/__pycache__ -delete
