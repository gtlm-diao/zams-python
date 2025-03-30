.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")
USING_POETRY=$(shell grep "tool.poetry" pyproject.toml && echo "yes")

.PHONY: help
help:             ## Show the help.
	@echo "Makefile pour zãms python"
	@echo "Utilisation: make [cible]"
	@echo
	@echo "Cibles:"
	@echo "  clean              Nettoyer les fichiers temporaires"
	@echo "  virtualenv         Créer un environnement virtuel"
	@echo "  test               Tester l'exécution des notebooks"
	@echo "  lint               Vérifier la syntaxe des scripts Python"
	@echo "  fmt                Formater les scripts Python avec black"
	@echo "  jupyter            Lancer le serveur Jupyter Notebook"
	@echo "  check_dirs         Vérifier que tous les répertoires requis existent"
	@echo "  session            Créer une nouvelle session (voir aide avec make session-help)"
	@echo "  session-help       Afficher l'aide pour la création de session"
	@echo "  requirements       Générer requirements.txt"

.PHONY: show
show:             ## Show the current environment.
	@echo "Current environment:"
	@if [ "$(USING_POETRY)" ]; then poetry env info && exit; fi
	@echo "Running using $(ENV_PREFIX)"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site

.PHONY: install
install:          ## Install the project in dev mode.
	@if [ "$(USING_POETRY)" ]; then poetry install && exit; fi
	@echo "Don't forget to run 'make virtualenv' if you got errors."
	$(ENV_PREFIX)pip install -e .[test]

.PHONY: fmt
fmt:              ## Format code using black & isort.
	$(ENV_PREFIX)isort zams_python/
	$(ENV_PREFIX)black -l 79 zams_python/
	$(ENV_PREFIX)black -l 79 tests/

.PHONY: lint
lint:             ## Run pep8, black, mypy linters.
	$(ENV_PREFIX)flake8 zams_python/
	$(ENV_PREFIX)black -l 79 --check zams_python/
	$(ENV_PREFIX)black -l 79 --check tests/
	$(ENV_PREFIX)mypy --ignore-missing-imports zams_python/

.PHONY: test
test: lint        ## Run tests and generate coverage report.
	$(ENV_PREFIX)pytest -v --cov-config .coveragerc --cov=zams_python -l --tb=short --maxfail=1 tests/
	$(ENV_PREFIX)coverage xml
	$(ENV_PREFIX)coverage html

.PHONY: watch
watch:            ## Run tests on every change.
	ls **/**.py | entr $(ENV_PREFIX)pytest -s -vvv -l --tb=long --maxfail=1 tests/

.PHONY: clean
clean:            ## Clean unused files.
	@echo "Nettoyage des fichiers temporaires..."
	@find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.pyd" -delete
	@find . -type f -name ".DS_Store" -delete
	@find . -type f -name "*.bak" -delete
	@find . -type f -name "*.swp" -delete
	@echo "✅ Nettoyage terminé!"

.PHONY: virtualenv
virtualenv:       ## Create a virtual environment.
	@echo "Création de l'environnement virtuel..."
	@${ENV_PREFIX}pip install -U pip
	@${ENV_PREFIX}pip install -e .[test]
	@echo "✅ Environnement virtuel créé dans .venv/"
	@echo "Pour l'activer, exécutez:"
	@echo "  source .venv/bin/activate  # Linux/Mac"
	@echo "  .venv\\Scripts\\activate     # Windows"

.PHONY: release
release:          ## Create a new tag for release.
	@echo "WARNING: This operation will create s version tag and push to github"
	@read -p "Version? (provide the next x.y.z semver) : " TAG
	@echo "$${TAG}" > zams_python/VERSION
	@$(ENV_PREFIX)gitchangelog > HISTORY.md
	@git add zams_python/VERSION HISTORY.md
	@git commit -m "release: version $${TAG} 🚀"
	@echo "creating git tag : $${TAG}"
	@git tag $${TAG}
	@git push -u origin HEAD --tags
	@echo "Github Actions will detect the new tag and release the new version."

.PHONY: docs
docs:             ## Build the documentation.
	@echo "building documentation ..."
	@$(ENV_PREFIX)mkdocs build
	URL="site/index.html"; xdg-open $$URL || sensible-browser $$URL || x-www-browser $$URL || gnome-open $$URL || open $$URL

.PHONY: switch-to-poetry
switch-to-poetry: ## Switch to poetry package manager.
	@echo "Switching to poetry ..."
	@if ! poetry --version > /dev/null; then echo 'poetry is required, install from https://python-poetry.org/'; exit 1; fi
	@rm -rf .venv
	@poetry init --no-interaction --name=a_flask_test --author=rochacbruno
	@echo "" >> pyproject.toml
	@echo "[tool.poetry.scripts]" >> pyproject.toml
	@echo "zams_python = 'zams_python.__main__:main'" >> pyproject.toml
	@cat requirements.txt | while read in; do poetry add --no-interaction "$${in}"; done
	@cat requirements-test.txt | while read in; do poetry add --no-interaction "$${in}" --dev; done
	@poetry install --no-interaction
	@mkdir -p .github/backup
	@mv requirements* .github/backup
	@mv setup.py .github/backup
	@echo "You have switched to https://python-poetry.org/ package manager."
	@echo "Please run 'poetry shell' or 'poetry run zams_python'"

.PHONY: init
init:             ## Initialize the project based on an application template.
	@./.github/init.sh

.PHONY: jupyter
jupyter:
	@echo "Lancement de Jupyter Notebook..."
	@jupyter notebook

.PHONY: check_dirs
check_dirs:
	@echo "Vérification des répertoires requis..."
	@mkdir -p modules
	@mkdir -p ressources/{images,datasets,scripts}
	@mkdir -p projets
	@mkdir -p communaute
	@mkdir -p utils
	@echo "✅ Tous les répertoires sont présents!"

.PHONY: session-help
session-help:
	@echo "Aide pour la création d'une nouvelle session"
	@echo ""
	@echo "Usage: make session MODULE=XX NAME=nom TITLE='Titre' SESSION=YY DESC='Description'"
	@echo ""
	@echo "Paramètres:"
	@echo "  MODULE : Numéro du module (ex: 02)"
	@echo "  NAME   : Nom du module (ex: structures-de-donnees)"
	@echo "  TITLE  : Titre du module (ex: 'Structures de données')"
	@echo "  SESSION: Numéro de la session (ex: 01)"
	@echo "  DESC   : Description de la session"
	@echo ""
	@echo "Exemple:"
	@echo "  make session MODULE=02 NAME=structures-de-donnees TITLE='Structures de données' SESSION=01 DESC='Introduction aux listes'"

.PHONY: session
session:
	@if [ -z "$(MODULE)" ] || [ -z "$(NAME)" ] || [ -z "$(TITLE)" ]; then \
		echo "⚠️ Erreur: Les paramètres MODULE, NAME et TITLE sont obligatoires."; \
		echo "Utilisez make session-help pour plus d'informations."; \
		exit 1; \
	fi
	@bash utils/create_session.sh \
		--module $(MODULE) \
		--name $(NAME) \
		--title "$(TITLE)" \
		$(if $(SESSION),--session $(SESSION),) \
		$(if $(DESC),--desc "$(DESC)",)

# Ce projet est basé sur le template créé par rochacbruno/python-project-template
# Modifié par: Alban NYANTUDRE
# Dépôt original: https://github.com/rochacbruno/python-project-template
