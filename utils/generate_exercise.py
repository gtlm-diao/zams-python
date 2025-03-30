#!/usr/bin/env python3
"""
Script pour générer des exercices à partir des notebooks.
Ce script prend un notebook et crée une version "exercice" (sans les solutions)
et une version "solution" (avec les solutions).
"""

import sys
import json
import os
import re
import argparse
from pathlib import Path
import shutil

def parse_args():
    """Parse les arguments de la ligne de commande"""
    parser = argparse.ArgumentParser(description="Générer des exercices à partir des notebooks")
    parser.add_argument("notebook", help="Chemin vers le notebook source")
    parser.add_argument("--output-dir", "-o", help="Répertoire de sortie (par défaut: même que le notebook)")
    parser.add_argument("--keep-solutions", "-k", action="store_true", help="Garder les blocs de solution dans le notebook d'exercice")
    return parser.parse_args()

def load_notebook(notebook_path):
    """Charge un notebook JSON"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Erreur lors du chargement du notebook: {str(e)}")
        sys.exit(1)

def save_notebook(notebook, output_path):
    """Sauvegarde un notebook JSON"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        print(f"✅ Notebook sauvegardé: {output_path}")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde du notebook: {str(e)}")
        sys.exit(1)

def is_solution_cell(cell):
    """Vérifie si une cellule contient une solution"""
    if cell['cell_type'] == 'markdown':
        return '## Solution' in cell['source'] or '#Solution' in cell['source']
    elif cell['cell_type'] == 'code':
        # Recherche d'un commentaire indiquant une solution
        source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        return '# SOLUTION' in source or '#SOLUTION' in source
    return False

def is_exercise_cell(cell):
    """Vérifie si une cellule contient un exercice"""
    if cell['cell_type'] == 'markdown':
        return '## Exercice' in cell['source'] or '#Exercice' in cell['source']
    return False

def create_exercise_notebook(notebook, keep_solutions=False):
    """Crée une version exercice du notebook"""
    exercise_notebook = notebook.copy()
    
    # Filtrer les cellules
    new_cells = []
    skip_next = False
    
    for i, cell in enumerate(notebook['cells']):
        if skip_next:
            skip_next = False
            continue
            
        if is_solution_cell(cell):
            if not keep_solutions:
                # Si c'est une cellule de solution et qu'on ne veut pas les garder
                if cell['cell_type'] == 'markdown':
                    # On garde la cellule markdown mais on ajoute un message
                    solution_cell = cell.copy()
                    solution_cell['source'] = "## Solution\n\n*Complétez cet exercice puis vérifiez votre solution.*"
                    new_cells.append(solution_cell)
                elif cell['cell_type'] == 'code':
                    # On remplace le code par un placeholder
                    code_cell = cell.copy()
                    code_cell['source'] = "# Écrivez votre solution ici\n\n"
                    new_cells.append(code_cell)
                
                # On saute la cellule suivante si c'est une cellule de code après une cellule markdown de solution
                if i < len(notebook['cells']) - 1 and cell['cell_type'] == 'markdown' and notebook['cells'][i+1]['cell_type'] == 'code':
                    skip_next = True
            else:
                # On garde la solution avec un marqueur
                if cell['cell_type'] == 'markdown':
                    cell_copy = cell.copy()
                    cell_copy['source'] = cell_copy['source'] + "\n\n**(Cette solution est fournie à titre indicatif, essayez de résoudre l'exercice par vous-même d'abord!)**"
                    new_cells.append(cell_copy)
                else:
                    new_cells.append(cell)
        else:
            new_cells.append(cell)
    
    exercise_notebook['cells'] = new_cells
    return exercise_notebook

def create_solution_notebook(notebook):
    """Crée une version solution du notebook"""
    # Pour le moment, on retourne simplement le notebook original
    return notebook

def main():
    """Fonction principale"""
    args = parse_args()
    
    notebook_path = Path(args.notebook)
    if not notebook_path.exists():
        print(f"❌ Le fichier {notebook_path} n'existe pas.")
        sys.exit(1)
    
    # Déterminer les chemins de sortie
    output_dir = args.output_dir if args.output_dir else notebook_path.parent
    output_dir = Path(output_dir)
    
    # Créer le répertoire de sortie si nécessaire
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Créer le sous-répertoire 'exercices' et 'solutions'
    exercices_dir = output_dir / 'exercices'
    solutions_dir = output_dir / 'exercices' / 'solutions'
    exercices_dir.mkdir(exist_ok=True)
    solutions_dir.mkdir(exist_ok=True)
    
    # Charger le notebook
    notebook = load_notebook(notebook_path)
    
    # Générer les noms de fichiers
    base_name = notebook_path.stem
    exercise_path = exercices_dir / f"{base_name}.ipynb"
    solution_path = solutions_dir / f"{base_name}_solution.ipynb"
    
    # Créer les notebooks d'exercice et de solution
    exercise_notebook = create_exercise_notebook(notebook, args.keep_solutions)
    solution_notebook = create_solution_notebook(notebook)
    
    # Sauvegarder les notebooks
    save_notebook(exercise_notebook, exercise_path)
    save_notebook(solution_notebook, solution_path)
    
    print(f"\n✅ Génération terminée !")
    print(f"   - Exercice: {exercise_path}")
    print(f"   - Solution: {solution_path}")

if __name__ == "__main__":
    main() 