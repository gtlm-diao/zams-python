#!/usr/bin/env python3
"""
Script d'initialisation pour les contributeurs au cours zãms python.
Ce script configure un nouvel environnement de développement pour les contributeurs.
"""

import os
import sys
import subprocess
import platform
import argparse

# Définir les couleurs pour les messages (si le terminal supporte les couleurs)
if platform.system() == "Windows":
    # Windows n'a pas de support natif pour les couleurs ANSI
    try:
        import colorama
        colorama.init()
        USE_COLORS = True
    except ImportError:
        USE_COLORS = False
else:
    USE_COLORS = True

# Définir les codes de couleur
if USE_COLORS:
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    RED = "\033[0;31m"
    YELLOW = "\033[0;33m"
    RESET = "\033[0m"
else:
    GREEN = BLUE = RED = YELLOW = RESET = ""

def print_colored(message, color):
    """Imprime un message coloré"""
    print(color + message + RESET)

def run_command(command, description=None, check=True):
    """Exécute une commande shell et gère les erreurs"""
    if description:
        print_colored(f"🔄 {description}...", BLUE)
    
    try:
        result = subprocess.run(command, shell=True, check=check, text=True, capture_output=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print_colored(f"❌ Erreur: {e}", RED)
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False

def setup_git():
    """Configure Git pour le projet"""
    print_colored("\n== Configuration de Git ==", BLUE)
    
    # Vérifier si Git est installé
    if not run_command("git --version", "Vérification de la version de Git", check=False):
        print_colored("❌ Git n'est pas installé. Veuillez l'installer depuis: https://git-scm.com/downloads", RED)
        return False
    
    # Configurer le nom et l'email si nécessaire
    git_user = subprocess.run("git config user.name", shell=True, capture_output=True, text=True).stdout.strip()
    git_email = subprocess.run("git config user.email", shell=True, capture_output=True, text=True).stdout.strip()
    
    if not git_user or not git_email:
        print_colored("⚠️ La configuration Git n'est pas complète.", YELLOW)
        if not git_user:
            name = input("Entrez votre nom pour Git: ")
            run_command(f'git config --global user.name "{name}"')
        if not git_email:
            email = input("Entrez votre email pour Git: ")
            run_command(f'git config --global user.email "{email}"')
    
    print_colored("✅ Git est correctement configuré!", GREEN)
    return True

def setup_virtual_env():
    """Configure l'environnement virtuel Python"""
    print_colored("\n== Configuration de l'environnement virtuel ==", BLUE)
    
    # Vérifier si virtual env existe déjà
    if os.path.exists(".venv"):
        activate = input("⚠️ Un environnement virtuel existe déjà. Voulez-vous le recréer? (o/n): ")
        if activate.lower() != 'o':
            print_colored("✅ Utilisation de l'environnement virtuel existant.", GREEN)
            return True

    # Créer l'environnement virtuel
    if platform.system() == "Windows":
        success = run_command("python -m venv .venv", "Création de l'environnement virtuel")
    else:
        success = run_command("python3 -m venv .venv", "Création de l'environnement virtuel")
    
    if not success:
        return False
    
    # Activer l'environnement virtuel et installer les dépendances
    if platform.system() == "Windows":
        print_colored("\n⚠️ Veuillez activer manuellement l'environnement virtuel avec:", YELLOW)
        print_colored("   .venv\\Scripts\\activate", BLUE)
        wait = input("Appuyez sur Entrée une fois l'environnement activé...")
    else:
        print_colored("\n⚠️ Veuillez activer manuellement l'environnement virtuel avec:", YELLOW)
        print_colored("   source .venv/bin/activate", BLUE)
        wait = input("Appuyez sur Entrée une fois l'environnement activé...")
    
    # Installer les dépendances
    success = run_command("pip install -r requirements.txt", "Installation des dépendances")
    
    if success:
        print_colored("✅ Environnement virtuel configuré et dépendances installées!", GREEN)
    
    return success

def fork_repo():
    """Guide pour forker le repo"""
    print_colored("\n== Fork du dépôt ==", BLUE)
    print_colored("Pour contribuer au projet, vous devez:", BLUE)
    print_colored("1. Forker le dépôt sur GitHub à l'adresse:", BLUE)
    print_colored("   https://github.com/anyantudre/zams-python", YELLOW)
    print_colored("2. Cloner votre fork localement:", BLUE)
    print_colored("   git clone https://github.com/VOTRE_NOM_UTILISATEUR/zams-python", YELLOW)
    print_colored("3. Ajouter le dépôt upstream:", BLUE)
    print_colored("   git remote add upstream https://github.com/anyantudre/zams-python", YELLOW)
    
    repo_name = input("\nAvez-vous déjà forké et cloné le dépôt? (o/n): ")
    
    if repo_name.lower() == 'n':
        print_colored("\n⚠️ Veuillez forker et cloner le dépôt avant de continuer.", YELLOW)
        return False
    
    print_colored("✅ Parfait! Continuons avec la configuration.", GREEN)
    return True

def setup_dev_tools():
    """Configure les outils de développement"""
    print_colored("\n== Configuration des outils de développement ==", BLUE)
    
    # Installer les outils de développement supplémentaires
    success = run_command("pip install black flake8 pytest jupyter", "Installation des outils de développement")
    
    if success:
        print_colored("✅ Outils de développement installés!", GREEN)
    
    return success

def main():
    """Fonction principale"""
    print_colored("\n=== INITIALISATION POUR LES CONTRIBUTEURS DE ZÃMS PYTHON ===", BLUE)
    print_colored("Ce script va vous aider à configurer votre environnement pour contribuer au cours.\n", BLUE)
    
    # Vérifier si on est dans le bon répertoire
    if not (os.path.exists("requirements.txt") and os.path.exists("README.md")):
        print_colored("❌ Erreur: Ce script doit être exécuté depuis le répertoire racine du projet.", RED)
        print_colored("   Assurez-vous d'être dans le répertoire contenant le fichier README.md", RED)
        return False
    
    steps = [
        fork_repo,
        setup_git,
        setup_virtual_env,
        setup_dev_tools,
    ]
    
    for step in steps:
        if not step():
            print_colored("\n⚠️ Configuration interrompue. Veuillez résoudre les problèmes ci-dessus et réessayer.", YELLOW)
            return False
    
    print_colored("\n✅ CONFIGURATION TERMINÉE AVEC SUCCÈS!", GREEN)
    print_colored("\nVous êtes maintenant prêt à contribuer au projet zãms python!", GREEN)
    print_colored("Pour commencer, créez une nouvelle branche pour votre contribution:", BLUE)
    print_colored("   git checkout -b ma-contribution", YELLOW)
    print_colored("\nBon codage! 🚀", BLUE)
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 