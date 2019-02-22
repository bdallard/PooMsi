# POO &amp; MSI 

## Prérequis 
Ce document contient une liste de prérequis en terme de programmes informatiques ainsi que de petites références pour mieux appréhender les différents cours.
**Et bien sur les diapos de cours (venir en cours c'est mieux quand même)** 

### Installer Python 3.x (3.4, 3.5 ou 3.6) et pip (pip3)
**Pour Windows** : <https://www.python.org/downloads/windows/>

**Pour Mac** : <https://www.python.org/downloads/mac-osx/>

ou avec le terminal 
```
brew install python3
brew install python3-pip
```

<a href ="https://brew.sh/index_fr"> <img src="https://upload.wikimedia.org/wikipedia/commons/3/34/Homebrew_logo.png">
### Installer Homebrew sur votre Mac 
Si les commandes ci-dessus ne fonctionnent pas c'est que vous n'avez pas Homebrew ! 
Cliquer sur le logo ci-dessus et suivre le tutoriel d'installation. 

### Installer Jupyter 
Jupyter est une application web permettant de créer des notebooks, des fichiers mélangeant à la fois du texte (en syntaxe markdown), des images, des équations mathématiques et bien sur du code.

Lancer la commande suivante : 
```
 pip3 install jupyter
``` 

### Installer les dépendances usuelles 
Lancer la commande suivante : 
```
pip3 install numpy matplotlib scipy pandas
```

## Configurer son environnement de travail 
Ouvrez un terminal

### Rappel des commandes utiles sur terminal 

- pwd : ou je suis (dans quel dossier je suis) 
- cd *MonRepo* : changer de dossier (direcrtory)
- ls : lister les objets présents (fichier et dossier) dans le répertoire sélectionné
- mkdir *NewRepo* : créer un nouveau dossier de nom *NewRepo*  
- rm *UnFichier* : supprimer un fichier (attention avec cette commande!) 
- man *UneCommande* : afficher le manuel de la commande sélectionnée


### Créer son dossier de travail 

0 - Ouvrir un terminal 

1 - Créer un dossier (si non existant) *workspace* 

2 - Créer dans le dossier *workspace* un dossier *Cours* 

### Importer le repository de GitHub 

0 - Aller sur la page <https://github.com/bdallard/PooMsi/>

1 - Appuyer sur le boutton vert *clone and download* (pour copier le lien du repo) 

2 - Cloner le repository (dans votre dossier Cours) avec la commande suivante : 
```
git clone https://github.com/bdallard/PooMsi.git
```

### Lancer Jupyter

Pour lancer jupyter, assurez vous de bien être positioné dans votre repo de travail (*Cours*) et lancer la commande suivante :  

```
jupyter notebook 
```

## mini git no deep shit 

### créer un nouveau dépôt
Pour créez un nouveau dossier, ouvrez le et exécutez la commande :
```
git init
```

### cloner un dépôt
Pour créez une copie de votre dépôt local en exécutant la commande : 
```
git clone /path/to/repository
```
si vous utilisez un serveur distant, cette commande sera : 
```
git clone username@host:/path/to/repository
```

### ajouter & valider des fichiers 
Vous pouvez proposer un changement (l'ajouter à l'Index) en exécutant les commandes : 
```
git add <filename>
git add *
```
C'est la première étape dans un workflow git basique. Pour valider ces changements, utilisez
```
git commit -m "Message de validation"
```
Le fichier est donc ajouté au HEAD, mais pas encore dans votre dépôt distant. Pour cela il faut exécuter la commande : 
```
git push origin master
```

### mettre à jour & fusionner
pour mettre à jour votre dépôt local vers les dernières validations, exécutez la commande
```
git pull
```

Pour ceux qui n'arrivent pas à pull parce qu'ils ont fait des modif dans le repo (no worries), lancer la commande : 
```
git stash
git pull
git stash pop
```
