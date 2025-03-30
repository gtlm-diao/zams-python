.ONESHELL:
.PHONY: clean virtualenv jupyter lint fmt help session requirements check_dirs

SHELL := /usr/bin/env bash
PYTHON := python

help:
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

clean:
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

virtualenv:
	@echo "Création de l'environnement virtuel..."
	@$(PYTHON) -m venv .venv
	@echo "✅ Environnement virtuel créé dans .venv/"
	@echo "Pour l'activer, exécutez:"
	@echo "  source .venv/bin/activate  # Linux/Mac"
	@echo "  .venv\\Scripts\\activate     # Windows"

requirements:
	@echo "Génération de requirements.txt à partir de l'environnement actuel..."
	@$(PYTHON) -m pip freeze > requirements.txt
	@echo "✅ requirements.txt généré!"

jupyter:
	@echo "Lancement de Jupyter Notebook..."
	@jupyter notebook

test:
	@echo "Test de l'exécution des notebooks..."
	@for notebook in $$(find modules -name "*.ipynb"); do \
		echo "📓 Test de $${notebook}..."; \
		jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 --inplace "$${notebook}" || echo "⚠️ Avertissement: Le notebook $${notebook} contient des erreurs."; \
	done
	@echo "✅ Tests terminés!"

lint:
	@echo "Lint du code Python..."
	@flake8 utils/ ressources/scripts/
	@echo "✅ Lint terminé!"

fmt:
	@echo "Formatage du code Python..."
	@black utils/ ressources/scripts/
	@echo "✅ Formatage terminé!"

check_dirs:
	@echo "Vérification des répertoires requis..."
	@mkdir -p modules
	@mkdir -p ressources/{images,datasets,scripts}
	@mkdir -p projets
	@mkdir -p communaute
	@mkdir -p utils
	@echo "✅ Tous les répertoires sont présents!"

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
