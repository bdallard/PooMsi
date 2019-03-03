# MongoDB Quickstart 

## Installation 
Ce README s'applique uniquement sur Mac OS. 


### Installer MongoDB avec [homebrew](https://brew.sh/)
Si vous n'avez pas homebrew installez le en cliquant sur le titre ci-dessus. 

Une fois homebrew installé lancer les commandes suivantes : 
```
brew update 
brew install mongodb
```


### Installer PyMongo 
Installer via la commande [pip3](https://pypi.org/project/pip/) ou bien `pip` si vous êtes en python2 
```
pip3 install pymongo 
```


### Avant de lancer votre script 
Pour ne pas avoir d'erreur de type : *Connection refused (Errno 61)*
Lancer un terminal dans votre dossier et taper la commande suivante : 
```
brew services start mongodb
```

Normalement si tout ce passe bien, brew vous renvoie : 
```
==> Successfully started `mongodb` (label: homebrew.mxcl.mongodb)
```
À ce moment la vous pouvez commencer sereinement votre script. 


### Objectif de la séance 
Cette séance à pour objectif de vous montrer le fonctionnement de base de PyMongo ainsi que de couvrir **les opérations CRUD (create, read, update, delete)**. 
La technologie PyMongo étant assez récente, je vous conseil de jeter un oeil à [la documentation officielle](https://api.mongodb.com/python/current/). 

