all: env pip-tools pip
dev: env pip-tools dev-pip

.PHONY: env
env:
	pyvenv-3.5 env

.PHONY: pip-tools
pip-tools:
	env/bin/pip install -U pip-tools

.PHONY: pip
pip: update-pip
	env/bin/pip-sync requirements.txt

.PHONY: dev-pip
dev-pip: update-pip
	env/bin/pip-sync requirements.txt dev-requirements.txt

.PHONY: update-pip
update-pip:
	env/bin/pip install -U setuptools
	env/bin/pip install -U pip==8.1.1

.PHONY: pip-compile
pip-compile:
	env/bin/pip-compile requirements.in
	env/bin/pip-compile dev-requirements.in

.PHONY: run
run:
	env/bin/python manage.py runserver 0.0.0.0:8080 --settings=finance.settings.dev

.PHONY: migrate
migrate:
	env/bin/python manage.py migrate

.PHONY: clean_cache
clean_cache:
	find **/__pycache__ -delete

.PHONY: tags
tags:
	ctags -R

.PHONY: test
test:
	env/bin/py.test

.PHONY: coverage
coverage:
	env/bin/py.test --cov --cov-report=html --cov-config=.coveragerc

.PHONY: clean
clean: clean_cache
	rm -rf env tags tmp var htmlcov

.PHONY: static
static:
	env/bin/python manage.py collectstatic --noinput

.PHONY: shell
shell:
	env/bin/python manage.py shell
