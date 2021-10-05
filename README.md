# Chess Tournament management project

Ce projet est un programme développé pour la gestion de tournois d'échecs, à partir d'un terminal.

## Téléchargements

Rendez vous [ici](https://github.com/Chreno972/P4_chess_tournament), pour télécharger le dossier du programme

- Pour les connaisseurs de gitbash:
  - clickez sur le bouton "Code" de couleur verte.
  - Copiez et collez le lien présenté dans la fenêtre nouvellement ouverte.
  - faites un git clone dans le gitbash. Gitbash ouvert bien sûr dans un dossier neutre destiné à récupérer le programme cloné.
- Pour les novices:
  - Clickez sur le bouton "Code" de couleur verte.
  - Cliquez ensuite sur "download ZIP".
  - Rendez-vous ensuite dans votre dossier "téléchargements".
  - Copiez ou coupez ce dossier
  - Collez le dans un dossier neutre destiné à contenir celui-ci

## Installations

**Ouvrez le dossier du programme** dans votre éditeur de code favoris
à la racine du projet vous trouvez:

- le dossier "app" qui contient tout le code du programme
- le fichier "main.py" qui représente le fichier de lancement du programme
- le fichier "readme.md" qui contient ce texte que vous lisez
- le fichier "requirements.txt" qui contient toutes les librairies utilisées pour créer ce programme.

**Installez pip**
Afin d'installer "pip" qui permet d'installer des librairies python, rendez-vous [ici](https://pip.pypa.io/en/stable/installation/)

**Installez votre environnement virtuel:**
dans votre terminal ou celui de votre éditeur de code, entrez

```Python
python3 -m venv "nom de l'environnement"
```

> Par convention le nom de l'environnement est "env"

Une fois votre environnement virtuel installé, **activez le**

- Sur Windows:

```Python
cd "nom de l'environnement virtuel"/Scripts => Entrée
ensuite activate.bat
```

Maintenant que votre environnement virtuel est installé, tapez `cd ../../`, pour revenir à la racine du dossier

**Installez les bibliothèques utilisées dans le programme**
Tout d'abord, vérifiez si rien n'est installé dans votre environnement virtuel en tapant dans le terminal `pip freeze`, si rien ne s'affiche en retour, on peut commencer à installer les dépendances présentes dans notre fichier "requirements.txt".
Tapez dans votre terminal `pip freeze > requirements.txt`, ainsi, toutes les dépendances seront automatiquement installées, peu importe leur nombre.

## Lancement du programme

Pour lancer le programme dans votre terminal, tapez "python3 main.py"
Vous n'avez plus qu'a suivre les instructions.
