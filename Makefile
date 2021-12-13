.PHONY: docs test

REPORTS := $(if $(REPORTS),yes,$(if $(CI),yes,no))
SHELL := /bin/bash

ifeq ($(strip $(shell git branch --show-current)),master)
	DEPLOY_ENVIRONMENT=common
else
	DEPLOY_ENVIRONMENT=dev
endif

help: ## show this message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%-30s %s\n" "target" "help" ; \
	printf "%-30s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-30s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done

docs: ## removes the currentli built docs, builds HTML docs, then opens the docs
	@pushd docs && \
	make docs && \
	popd

docs-clean: ## removes the currentli built docs
	@pushd docs && \
	make clean && \
	popd

docs-html: ## builds HTML docs,
	@pushd docs && \
	make html && \
	popd

docs-open: ## opens the docs
	@pushd docs && \
	make open && \
	popd

fix-black: ## automatically fix all black errors
	@poetry run black .

fix-isort: ## automatically fix all isort errors
	@poetry run isort .

lint: lint-isort lint-black lint-flake8 lint-pyright lint-pylint  ## run all linters

lint-black: ## run black
	@echo "Running black... If this fails, run 'make fix-black' to resolve."
	@poetry run black . --check
	@echo ""

lint-cfn:  ## run cfn-lint
	@echo "Running cfn-lint..."
	@poetry run cfn-lint
	@echo ""

lint-flake8: ## run flake8
	@echo "Running flake8..."
	@poetry run flake8
	@echo ""

lint-isort: ## run isort
	@echo "Running isort... If this fails, run 'make fix-isort' to resolve."
	@poetry run isort . --check-only
	@echo ""

lint-pylint: ## run pylint
	@echo "Running pylint..."
	@poetry run pylint --rcfile=pyproject.toml ssm_dox tests --reports=${REPORTS}
	@echo ""

lint-pyright: ## run pyright
	@echo "Running pyright..."
	@npx pyright --venv-path ./
	@echo ""

run-pre-commit:
	@poetry run pre-commit run -a

setup: setup-poetry setup-pre-commit  ## setup development environment

setup-poetry: ## setup poetry environment
	@poetry install \
		--extras docs \
		--remove-untracked

setup-pre-commit: ## setup pre-commit
	@poetry run pre-commit install

test: ## run tests
	@poetry run pytest --cov=ssm_dox --cov-report term-missing:skip-covered
