"""
Configuration pour les notebooks Jupyter de zãms python.
Ce script contient des fonctions utilitaires qui peuvent être importées
dans les notebooks pour faciliter l'apprentissage.
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, HTML, Markdown

# Configuration de l'affichage des graphiques
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
plt.style.use('seaborn-v0_8-whitegrid')

def afficher_info():
    """Affiche des informations sur l'environnement Python."""
    print(f"Python version: {sys.version}")
    print(f"Exécuté depuis: {os.getcwd()}")
    
def titre(texte, niveau=1):
    """Affiche un titre formaté de manière élégante."""
    if niveau == 1:
        display(HTML(f"<h1 style='color:#4169E1'>{texte}</h1>"))
    elif niveau == 2:
        display(HTML(f"<h2 style='color:#6A5ACD'>{texte}</h2>"))
    else:
        display(HTML(f"<h3 style='color:#708090'>{texte}</h3>"))
        
def note(texte):
    """Affiche une note avec une mise en forme spéciale."""
    display(HTML(f"<div style='background-color:#F0F8FF;padding:10px;border-left:5px solid #4169E1'><strong>Note:</strong> {texte}</div>"))
    
def avertissement(texte):
    """Affiche un avertissement avec une mise en forme spéciale."""
    display(HTML(f"<div style='background-color:#FFF0F5;padding:10px;border-left:5px solid #FF6347'><strong>Attention:</strong> {texte}</div>"))
    
def astuce(texte):
    """Affiche une astuce avec une mise en forme spéciale."""
    display(HTML(f"<div style='background-color:#F0FFF0;padding:10px;border-left:5px solid #3CB371'><strong>Astuce:</strong> {texte}</div>"))
    
def terme_technique(terme, definition, moore=None):
    """Affiche un terme technique avec sa définition."""
    moore_text = f"<br><strong>Mooré:</strong> {moore}" if moore else ""
    display(HTML(f"<div style='background-color:#FFFAF0;padding:10px;border:1px solid #DEB887'><strong>{terme}</strong><br>{definition}{moore_text}</div>"))
    
def check_exercice(fonction, tests, messages=None):
    """Vérifie si la réponse à un exercice est correcte."""
    if messages is None:
        messages = ["Test réussi!", "Test échoué. Essayez encore."]
    
    all_passed = True
    for i, test in enumerate(tests):
        try:
            result = fonction(*test[0])
            expected = test[1]
            if result == expected:
                print(f"Test {i+1}: ✅ {messages[0]}")
            else:
                all_passed = False
                print(f"Test {i+1}: ❌ {messages[1]}")
                print(f"  Votre résultat: {result}")
                print(f"  Résultat attendu: {expected}")
        except Exception as e:
            all_passed = False
            print(f"Test {i+1}: ❌ Erreur: {str(e)}")
    
    if all_passed:
        display(HTML("<div style='background-color:#F0FFF0;padding:10px;text-align:center'><h3>Bravo! Tous les tests sont passés! 🎉</h3></div>"))
    else:
        display(HTML("<div style='background-color:#FFF0F5;padding:10px;text-align:center'><h3>Certains tests ont échoué. Continuez à essayer! 💪</h3></div>"))
        
# Style pour les notebooks
def appliquer_style():
    """Applique un style personnalisé au notebook."""
    style = """
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
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
        .rendered_html table {
            border: 1px solid #ddd;
            border-collapse: collapse;
        }
        .rendered_html th {
            background-color: #f2f2f2;
            font-weight: bold;
            border: 1px solid #ddd;
            padding: 8px;
        }
        .rendered_html td {
            border: 1px solid #ddd;
            padding: 8px;
        }
    </style>
    """
    display(HTML(style)) 