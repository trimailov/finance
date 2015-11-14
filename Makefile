all: env pip-tools pip
dev: env pip-tools dev-pip

.PHONY: env
env:
	pyvenv-3.5 env

.PHONY: pip-tools
pip-tools:
	env/bin/pip install pip-tools

.PHONY: pip
pip:
	env/bin/pip-compile requirements.in
	env/bin/pip-sync requirements.txt

.PHONY: dev-pip
dev-pip:
	env/bin/pip-compile requirements.in
	env/bin/pip-compile dev-requirements.in
	env/bin/pip-sync requirements.txt dev-requirements.txt

.PHONY: run
run:
	env/bin/python manage.py runserver 0.0.0.0:8080

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
	env/bin/python manage.py test

.PHONY: coverage
coverage:
	env/bin/coverage run --source=finance,accounts,books --omit=finance/wsgi.py manage.py test
	env/bin/coverage report
	env/bin/coverage html

.PHONY: clean
clean: clean_cache
	rm -rf env tags

.PHONY: static
static:
	env/bin/python manage.py collectstatic --noinput

.PHONY: shell
shell:
	env/bin/python manage.py shell
