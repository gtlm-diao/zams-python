#!/usr/bin/env python3
"""
Script de vérification de l'environnement pour le cours zãms python.
Permet de vérifier que toutes les dépendances sont correctement installées
et que l'environnement Python est correctement configuré.
"""

import sys
import pkg_resources
import platform
import subprocess
import os
from colorama import init, Fore, Style

# Initialiser colorama pour le support des couleurs dans le terminal
init()

def print_success(message):
    """Affiche un message de succès en vert"""
    print(Fore.GREEN + "✅ " + message + Style.RESET_ALL)

def print_error(message):
    """Affiche un message d'erreur en rouge"""
    print(Fore.RED + "❌ " + message + Style.RESET_ALL)

def print_warning(message):
    """Affiche un avertissement en jaune"""
    print(Fore.YELLOW + "⚠️ " + message + Style.RESET_ALL)

def print_info(message):
    """Affiche une information en bleu"""
    print(Fore.BLUE + "ℹ️ " + message + Style.RESET_ALL)

def print_header(message):
    """Affiche un titre de section"""
    print("\n" + Fore.CYAN + "== " + message + " ==" + Style.RESET_ALL)

def check_python_version():
    """Vérifie la version de Python"""
    print_header("Vérification de la version de Python")
    
    major, minor, micro = sys.version_info[:3]
    version = f"{major}.{minor}.{micro}"
    if major >= 3 and minor >= 6:
        print_success(f"Python version {version} détectée (compatible)")
    else:
        print_error(f"Python version {version} détectée (incompatible)")
        print_info("Ce cours nécessite Python 3.6 ou supérieur.")
        print_info("Veuillez mettre à jour votre version de Python: https://www.python.org/downloads/")

def check_packages():
    """Vérifie que les packages requis sont installés"""
    print_header("Vérification des packages requis")
    
    required_packages = {
        'jupyter': '1.0.0',
        'notebook': '6.0.0',
        'numpy': '1.16.0',
        'pandas': '1.0.0',
        'matplotlib': '3.0.0',
        'seaborn': '0.9.0',
        'pytest': '5.0.0'
    }
    
    missing_packages = []
    outdated_packages = []
    
    for package, min_version in required_packages.items():
        try:
            installed_version = pkg_resources.get_distribution(package).version
            if pkg_resources.parse_version(installed_version) < pkg_resources.parse_version(min_version):
                outdated_packages.append((package, installed_version, min_version))
            else:
                print_success(f"{package} version {installed_version} installée")
        except pkg_resources.DistributionNotFound:
            missing_packages.append(package)
    
    if missing_packages:
        print_error("Packages manquants: " + ", ".join(missing_packages))
        print_info("Exécutez la commande: pip install " + " ".join(missing_packages))
    
    if outdated_packages:
        print_warning("Packages obsolètes:")
        for package, installed_version, min_version in outdated_packages:
            print_warning(f"  {package}: installé ({installed_version}), requis ({min_version})")
        package_list = " ".join([p[0] for p in outdated_packages])
        print_info(f"Exécutez la commande: pip install --upgrade {package_list}")

def check_jupyter():
    """Vérifie que Jupyter est correctement installé"""
    print_header("Vérification de Jupyter")
    
    try:
        # Vérifier si la commande jupyter est disponible
        subprocess.run(["jupyter", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print_success("Jupyter est correctement installé")
        
        # Vérifier si Jupyter peut trouver le kernel Python
        kernels = subprocess.run(["jupyter", "kernelspec", "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "python" in kernels.stdout.lower():
            print_success("Le kernel Python est disponible dans Jupyter")
        else:
            print_warning("Kernel Python non trouvé dans Jupyter")
            print_info("Exécutez: python -m ipykernel install --user")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_error("Jupyter n'est pas correctement installé ou n'est pas dans le PATH")
        print_info("Installez Jupyter avec: pip install jupyter notebook")

def check_git():
    """Vérifie que Git est installé"""
    print_header("Vérification de Git")
    
    try:
        git_version = subprocess.run(["git", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        print_success(f"Git est installé: {git_version.stdout.strip()}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_warning("Git n'est pas installé ou n'est pas dans le PATH")
        print_info("Git est recommandé pour collaborer et soumettre des exercices.")
        print_info("Téléchargez Git: https://git-scm.com/downloads")

def main():
    """Fonction principale"""
    print("\n" + Fore.CYAN + Style.BRIGHT + "VÉRIFICATION DE L'ENVIRONNEMENT POUR LE COURS ZÃMS PYTHON" + Style.RESET_ALL + "\n")
    
    print_info(f"Système d'exploitation: {platform.system()} {platform.release()}")
    print_info(f"Répertoire de travail: {os.getcwd()}")
    
    check_python_version()
    check_packages()
    check_jupyter()
    check_git()
    
    print("\n" + Fore.CYAN + Style.BRIGHT + "RÉSUMÉ" + Style.RESET_ALL)
    print_info("Si vous voyez des erreurs ou avertissements ci-dessus, veuillez les résoudre avant de continuer.")
    print_info("Pour toute aide supplémentaire, consultez le fichier communaute/faq.md")
    print_info("Ou posez vos questions dans les discussions GitHub du projet")

if __name__ == "__main__":
    main() 