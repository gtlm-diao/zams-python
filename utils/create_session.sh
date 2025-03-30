#!/bin/bash
# Script pour créer une nouvelle session de formation

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Fonction d'aide
function show_help {
    echo -e "${BLUE}Création d'une nouvelle session pour le cours zãms python${NC}"
    echo ""
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  -m, --module NUMBER   Numéro du module (ex: 02)"
    echo "  -n, --name NAME       Nom du module (ex: 'structures-de-donnees')"
    echo "  -t, --title TITLE     Titre du module (ex: 'Structures de données')"
    echo "  -s, --session NUMBER  Numéro de la session (ex: 01)"
    echo "  -d, --desc DESC       Description de la session"
    echo "  -h, --help            Afficher cette aide"
    echo ""
    echo "Exemple:"
    echo "  $0 -m 02 -n structures-de-donnees -t 'Structures de données' -s 01 -d 'Introduction aux listes'"
    exit 0
}

# Vérifier que le script est exécuté à partir du répertoire racine
if [[ ! -d "modules" ]]; then
    echo -e "${RED}Erreur: Ce script doit être exécuté depuis le répertoire racine du projet.${NC}"
    echo -e "${YELLOW}Exemple: bash utils/create_session.sh [options]${NC}"
    exit 1
fi

# Valeurs par défaut
MODULE_NUM=""
MODULE_NAME=""
MODULE_TITLE=""
SESSION_NUM=""
SESSION_DESC=""

# Analyser les arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -m|--module) MODULE_NUM="$2"; shift ;;
        -n|--name) MODULE_NAME="$2"; shift ;;
        -t|--title) MODULE_TITLE="$2"; shift ;;
        -s|--session) SESSION_NUM="$2"; shift ;;
        -d|--desc) SESSION_DESC="$2"; shift ;;
        -h|--help) show_help ;;
        *) echo -e "${RED}Option inconnue: $1${NC}"; show_help ;;
    esac
    shift
done

# Validation des entrées
if [[ -z "$MODULE_NUM" || -z "$MODULE_NAME" || -z "$MODULE_TITLE" ]]; then
    echo -e "${RED}Erreur: Les paramètres module, name et title sont obligatoires.${NC}"
    show_help
fi

# Créer le module s'il n'existe pas
MODULE_PATH="modules/${MODULE_NUM}-${MODULE_NAME}"
if [[ ! -d "$MODULE_PATH" ]]; then
    echo -e "${BLUE}Création du module ${MODULE_NUM}: ${MODULE_TITLE}...${NC}"
    mkdir -p "${MODULE_PATH}/exercices/solutions"
    mkdir -p "${MODULE_PATH}/ressources"
    
    # Créer le README du module
    cat << EOF > "${MODULE_PATH}/README.md"
# Module ${MODULE_NUM} : ${MODULE_TITLE}

Ce module du cours zãms python couvre ${MODULE_TITLE}.

## Objectifs d'apprentissage

À la fin de ce module, vous serez capable de :
- [À remplir]
- [À remplir]
- [À remplir]

## Contenu du module

1. [À remplir]
2. [À remplir]
3. [À remplir]

## Exercices

Dans le dossier [exercices](exercices), vous trouverez des exercices pratiques pour mettre en application ce que vous avez appris dans ce module.

## Ressources supplémentaires

Le dossier [ressources](ressources) contient des documents, liens et outils supplémentaires pour approfondir les sujets abordés dans ce module.

## Prérequis

- [À remplir]
- [À remplir]

---

Bon apprentissage !
EOF
    
    echo -e "${GREEN}✅ Module ${MODULE_NUM} créé avec succès !${NC}"
else
    echo -e "${YELLOW}Le module ${MODULE_NUM} existe déjà.${NC}"
fi

# Création de la session si demandée
if [[ ! -z "$SESSION_NUM" ]]; then
    SESSION_FILE="${MODULE_PATH}/${SESSION_NUM}-session.ipynb"
    
    if [[ ! -f "$SESSION_FILE" ]]; then
        echo -e "${BLUE}Création de la session ${SESSION_NUM} pour le module ${MODULE_NUM}...${NC}"
        
        # Titre par défaut si non fourni
        if [[ -z "$SESSION_DESC" ]]; then
            SESSION_DESC="Session ${SESSION_NUM} du module ${MODULE_NUM}"
        fi
        
        # Création du template de notebook Jupyter
        cat << EOF > "$SESSION_FILE"
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ${MODULE_TITLE} - ${SESSION_DESC}\\n",
    "\\n",
    "Bienvenue dans cette session du cours **zãms python** !\\n",
    "\\n",
    "${SESSION_DESC}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objectifs de cette session\\n",
    "\\n",
    "- Objectif 1\\n",
    "- Objectif 2\\n",
    "- Objectif 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import des modules nécessaires"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import des modules standard de Python\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Import des fonctions utilitaires du cours\n",
    "# En local:\n",
    "try:\n",
    "    from utils.notebook_config import *\n",
    "    afficher_info()\n",
    "except ImportError:\n",
    "    print(\"Modules utilitaires non disponibles.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Introduction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Contenu de l'introduction..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Votre premier exercice"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exercice 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Description de l'exercice..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Votre code ici"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# SOLUTION\n",
    "# Votre solution ici"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conclusion\\n",
    "\\n",
    "Dans cette session, nous avons appris ...\\n",
    "\\n",
    "Dans la prochaine session, nous verrons ..."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
EOF
        
        echo -e "${GREEN}✅ Session ${SESSION_NUM} créée avec succès !${NC}"
        echo -e "${BLUE}Fichier notebook créé : ${SESSION_FILE}${NC}"
        
        # Générer automatiquement l'exercice à partir du notebook
        echo -e "${BLUE}Génération des fichiers d'exercice...${NC}"
        python utils/generate_exercise.py "$SESSION_FILE"
    else
        echo -e "${YELLOW}La session ${SESSION_NUM} existe déjà pour le module ${MODULE_NUM}.${NC}"
    fi
fi

echo -e "${GREEN}✅ Opération terminée !${NC}" 