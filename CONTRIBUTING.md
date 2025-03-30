# Comment contribuer à zãms python

Nous sommes ravis que vous souhaitiez contribuer à zãms python ! Voici quelques lignes directrices pour vous aider.

## Prérequis

- Vous avez besoin de Python 3.6 ou supérieur
- Ces instructions sont principalement pour les systèmes Linux, MacOS, Windows (avec Git Bash)

## Installation de votre propre fork de ce dépôt

1. Sur l'interface GitHub, cliquez sur le bouton `Fork`
2. Clonez votre fork de ce dépôt : `git clone git@github.com:VOTRE_NOM_UTILISATEUR_GIT/zams-python.git`
3. Entrez dans le répertoire : `cd zams-python`
4. Ajoutez le dépôt upstream : `git remote add upstream https://github.com/anyantudre/zams-python`

## Configuration de votre environnement virtuel

Exécutez `make virtualenv` pour créer un environnement virtuel,
puis activez-le avec `source .venv/bin/activate` (Linux/Mac) ou `.venv\Scripts\activate` (Windows).

## Installation du projet en mode développement

Exécutez `make install` pour installer le projet en mode développement.

## Types de contributions

Vous pouvez contribuer de plusieurs façons :

1. **Amélioration des notebooks existants** : correction de bugs, clarification des explications, amélioration des exemples
2. **Création de nouveaux contenus** : nouveaux modules, exercices, projets
3. **Traduction** : aider à traduire des termes techniques en mooré pour le glossaire
4. **Documentation** : améliorer la documentation, ajouter des ressources
5. **Correction** : signaler et corriger des erreurs

## Processus de contribution

1. Créez une nouvelle branche pour votre contribution :
   ```
   git checkout -b ma_contribution
   ```

2. Faites vos modifications

3. Testez vos modifications :
   - Pour les notebooks : assurez-vous qu'ils s'exécutent sans erreur
   - Pour le code Python : exécutez `make test` pour lancer les tests

4. Formatez le code :
   - Exécutez `make fmt` pour formater le code

5. Soumettez vos modifications :
   ```
   git add .
   git commit -m "Description de vos modifications"
   git push origin ma_contribution
   ```

6. Créez une Pull Request sur GitHub

## Directives spécifiques pour les notebooks

- Chaque notebook doit commencer par un titre et une introduction claire
- Utilisez des markdown cells pour expliquer les concepts
- Fournissez des exemples exécutables
- Ajoutez des exercices à la fin de chaque notebook
- Pensez à inclure des explications culturellement pertinentes quand c'est possible

## Directives pour le glossaire

Pour ajouter des termes au glossaire, suivez ce format :
```markdown
### Terme technique

**Français** : Explication en français
**Mooré** : Traduction en mooré (si disponible)
**Explication** : Description détaillée du concept
```

## Aide

Si vous avez des questions ou besoin d'aide, n'hésitez pas à :
- Ouvrir une issue sur GitHub
- Contacter les responsables du projet via les discussions GitHub

Merci de contribuer à rendre l'apprentissage de Python accessible à tous !

## Makefile utilities

This project comes with a `Makefile` that contains a number of useful utility.

```bash 
❯ make
Usage: make <target>

Targets:
help:             ## Show the help.
install:          ## Install the project in dev mode.
fmt:              ## Format code using black & isort.
lint:             ## Run pep8, black, mypy linters.
test: lint        ## Run tests and generate coverage report.
watch:            ## Run tests on every change.
clean:            ## Clean unused files.
virtualenv:       ## Create a virtual environment.
release:          ## Create a new tag for release.
docs:             ## Build the documentation.
switch-to-poetry: ## Switch to poetry package manager.
init:             ## Initialize the project based on an application template.
```

## Making a new release

This project uses [semantic versioning](https://semver.org/) and tags releases with `X.Y.Z`
Every time a new tag is created and pushed to the remote repo, github actions will
automatically create a new release on github and trigger a release on PyPI.

For this to work you need to setup a secret called `PIPY_API_TOKEN` on the project settings>secrets, 
this token can be generated on [pypi.org](https://pypi.org/account/).

To trigger a new release all you need to do is.

1. If you have changes to add to the repo
    * Make your changes following the steps described above.
    * Commit your changes following the [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0/).
2. Run the tests to ensure everything is working.
4. Run `make release` to create a new tag and push it to the remote repo.

the `make release` will ask you the version number to create the tag, ex: type `0.1.1` when you are asked.

> **CAUTION**:  The make release will change local changelog files and commit all the unstaged changes you have.
