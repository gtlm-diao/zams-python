#!/usr/bin/env python3
"""
Script de préparation pour Google Colab pour le cours zãms python.
Ce script installe les packages nécessaires et configure l'environnement Colab
pour fonctionner correctement avec les notebooks du cours.

Pour l'utiliser dans Colab, ajoutez cette cellule au début du notebook:
```
!pip install -q gdown
!gdown https://raw.githubusercontent.com/anyantudre/zams-python/main/ressources/scripts/prepare_colab.py
%run prepare_colab.py
```
"""

import sys
import subprocess
import os
from IPython.display import display, HTML, Markdown
import warnings
warnings.filterwarnings('ignore')

# Vérifier si nous sommes dans Colab
def is_colab():
    try:
        import google.colab
        return True
    except ImportError:
        return False

def install_dependencies():
    """Installe les dépendances nécessaires pour le cours"""
    print("Installation des packages nécessaires...")
    packages = [
        "numpy==1.24.3",
        "pandas==2.0.0",
        "matplotlib==3.7.1",
        "seaborn==0.12.2",
        "pytest==7.3.1",
        "colorama",
        "ipywidgets"
    ]
    
    for package in packages:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", package])
    
    print("✅ Packages installés avec succès!")

def download_utils():
    """Télécharge les fichiers utilitaires depuis le dépôt GitHub"""
    print("Téléchargement des fichiers utilitaires...")
    
    # Créer le répertoire utils si nécessaire
    if not os.path.exists('utils'):
        os.makedirs('utils')
    
    # Liste des fichiers à télécharger
    files = {
        "notebook_config.py": "https://raw.githubusercontent.com/anyantudre/zams-python/main/utils/notebook_config.py"
    }
    
    for filename, url in files.items():
        subprocess.run(["wget", "-q", "-O", f"utils/{filename}", url])
    
    print("✅ Fichiers utilitaires téléchargés!")

def setup_google_drive():
    """Configure l'accès à Google Drive pour sauvegarder le travail"""
    from google.colab import drive
    
    print("Configuration de l'accès à Google Drive...")
    try:
        drive.mount('/content/drive')
        
        # Créer un dossier pour le cours si nécessaire
        zams_folder = '/content/drive/MyDrive/zams_python'
        if not os.path.exists(zams_folder):
            os.makedirs(zams_folder)
            os.makedirs(f"{zams_folder}/exercices")
            
        print(f"✅ Google Drive monté avec succès! Vos travaux seront sauvegardés dans: {zams_folder}")
    except Exception as e:
        print(f"❌ Erreur lors du montage de Google Drive: {str(e)}")
        print("Vous pouvez continuer à utiliser ce notebook, mais vos travaux ne seront pas sauvegardés automatiquement.")

def apply_styling():
    """Applique un style visuel pour les notebooks"""
    style = """
    <style>
        .zams-header {
            background-color: #4169E1;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .zams-footer {
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
            border-radius: 5px;
            margin-top: 30px;
            font-size: 0.8em;
        }
        h1 {
            color: #4169E1;
            border-bottom: 2px solid #4169E1;
            padding-bottom: 5px;
        }
        h2 {
            color: #6A5ACD;
            border-bottom: 1px solid #6A5ACD;
            padding-bottom: 3px;
        }
        h3 {
            color: #708090;
        }
        .note {
            background-color: #F0F8FF;
            padding: 10px;
            border-left: 5px solid #4169E1;
            margin: 10px 0;
        }
        .warning {
            background-color: #FFF0F5;
            padding: 10px;
            border-left: 5px solid #FF6347;
            margin: 10px 0;
        }
        .tip {
            background-color: #F0FFF0;
            padding: 10px;
            border-left: 5px solid #3CB371;
            margin: 10px 0;
        }
    </style>
    """
    display(HTML(style))
    
    # Afficher l'en-tête
    header = """
    <div class="zams-header">
        <h1 style="color: white;">zãms python</h1>
        <p>Apprendre Python à la Burkinabè</p>
    </div>
    """
    display(HTML(header))

def display_footer():
    """Affiche un pied de page pour le notebook"""
    footer = """
    <div class="zams-footer">
        <p>© zãms python | <a href="https://github.com/anyantudre/zams-python" target="_blank">GitHub</a> | <a href="#" target="_blank">YouTube</a></p>
    </div>
    """
    display(HTML(footer))

def main():
    """Fonction principale"""
    # Vérifier si nous sommes dans Google Colab
    if not is_colab():
        print("⚠️ Ce script est conçu pour être exécuté dans Google Colab.")
        return
    
    print("🚀 Préparation de l'environnement zãms python dans Google Colab...\n")
    
    # Installer les dépendances
    install_dependencies()
    
    # Télécharger les fichiers utilitaires
    download_utils()
    
    # Configurer Google Drive
    setup_google_drive()
    
    # Appliquer le style
    apply_styling()
    
    # Message de succès
    print("\n✅ Tout est prêt! Vous pouvez maintenant suivre le cours zãms python dans Colab.")
    print("📚 Importez les fonctions utilitaires avec: from utils.notebook_config import *")
    
    # Ajouter un pied de page
    display_footer()

if __name__ == "__main__":
    main() 