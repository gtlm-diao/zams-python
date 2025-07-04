# Cheatsheet de Pathlib

## 1. Import et objet de base

```python
from pathlib import Path
```

* **Path(…)** : crée un objet chemin (POSIXPath ou WindowsPath selon OS).
* **Path.cwd()** : chemin du répertoire courant.
* **Path.home()** : chemin du répertoire personnel.

---

## 2. Création et combinaison de chemins

```python
p1 = Path("data")                       # depuis chaîne
p2 = Path("/etc") / "nginx" / "sites"   # opérateur `/` pour concaténer
p3 = p2 / "default.conf"
```

---

## 3. Composants de chemin

Pour un `p = Path("/home/user/docs/report.txt")` :

* `p.parts` → `('/', 'home', 'user', 'docs', 'report.txt')`
* `p.parent` → `Path('/home/user/docs')`
* `p.parents[0]`, `p.parents[1]`, … → niveaux supérieurs
* `p.name` → `'report.txt'`
* `p.stem` → `'report'`
* `p.suffix` → `'.txt'`
* `p.drive` (Windows) → `'C:'`
* `p.root` → `'/'`

---

## 4. Test d’existence et type

```python
p.exists()    # True si fichier/répertoire existe
p.is_file()   # True si c’est un fichier
p.is_dir()    # True si c’est un répertoire
```

---

## 5. Itération et recherche

```python
for entry in Path('.').iterdir():
    print(entry)           # liste non-récursive

pngs = list(Path('images').glob('*.png'))        # fichiers .png
all_txt = list(Path('docs').rglob('*.txt'))      # récursif
```

* **glob(…)** : motifs simples (`*`, `?`, `[a-z]`)
* **rglob(…)** : même, mais dans sous‑répertoires

---

## 6. Création et suppression

```python
d = Path("new_folder")
d.mkdir()                     # crée un dossier
d2 = Path("a/b/c")
d2.mkdir(parents=True)        # crée toute l’arborescence

f = Path("data.csv")
f.touch()                     # crée (ou met à jour) le fichier
if f.exists(): f.unlink()     # supprime un fichier
d.rmdir()                     # supprime dossier vide
```

---

## 7. Lecture et écriture de fichiers

```python
p = Path("notes.txt")
text = p.read_text(encoding="utf-8")   # lecture texte
data = p.read_bytes()                  # lecture binaire

p.write_text("Hello\n")                # écrase et écrit texte
p.write_bytes(b"\x00\x01")             # écrase et écrit octets
```

---

## 8. Renommage & déplacement

```python
src = Path("old.txt")
dst = Path("new.txt")
src.rename(dst)                        # renomme

# déplacer
dest_dir = Path("archive")
dest_dir.mkdir(exist_ok=True)
dst.replace(dest_dir / dst.name)
```

---

## 9. Chemins relatifs vs. absolus

```python
rel = Path("images/pic.png")      # relatif
abs = rel.resolve()               # absolu

# passer d’absolu à relatif
reference = Path.cwd()
rel2 = abs.relative_to(reference)
```

---

## 10. Informations système

```python
stat = Path("file.bin").stat()
size = stat.st_size                # taille en octets
mtime = stat.st_mtime              # timestamp de dernière modif
```

---

> **Tips**
>
> * Toujours utiliser `/` plutôt que des chaînes pour assembler des chemins.
> * Tester l’existence avant création/suppression pour éviter les exceptions.
> * Préférer `glob`/`rglob` à `os.walk` pour filtrer directement les fichiers.
> * `Path` ne touche pas au système : c’est un simple objet. Les méthodes (`exists()`, `read_text()`, …) font l’action réelle.