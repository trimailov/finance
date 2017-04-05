ENV = env
BIN = $(ENV)/bin
PIP = $(BIN)/pip
PIP_COMPILE = $(BIN)/pip-compile
PIP_SYNC = $(BIN)/pip-sync
SIGNSPACE = $(BIN)/signspace
PYTEST = $(BIN)/pytest
DONEFILE = $(ENV)/.done
TESTDIR = test

.PHONY: env
env: $(DONEFILE) bin

.PHONY: help
help:
	@echo "make              # install dev environment"
	@echo "make tags         # build ctags for server and client"
	@echo "make run          # run the backend dev server"
	@echo "make test         # run tests"
	@echo "make static       # runs collectstatic"
	@echo "make clean        # removes everything created by make"
	@echo "make clean_cache  # removes python's __pycache__ dirs"

.PHONY: run
run: env
	env/bin/python -Wall manage.py runserver 0.0.0.0:8080 --settings=finance.settings.dev

$(PIP):
	pyvenv-3.5 $(ENV)

$(PIP_COMPILE) $(PIP_SYNC): $(PIP)
	$(PIP) install pip-tools

$(DONEFILE): $(PIP) $(PIP_SYNC) requirements.txt requirements-dev.txt
	$(PIP_SYNC) requirements-dev.txt
	touch $@

requirements.txt: requirements/prod.in
	$(PIP_COMPILE) requirements/prod.in -o requirements.txt

requirements-dev.txt: requirements/prod.in requirements/dev.in
	$(PIP_COMPILE) requirements/prod.in requirements/dev.in -o requirements-dev.txt

# Convenience shortcut
bin: $(BIN)
	ln -sf $(BIN) bin

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
	$(PYTEST)

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
