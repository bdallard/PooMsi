# Introduction à la librairie Scikit-learn

Petit rappel générique de ce qu'est `scikit-learn`. 

- Cette librairie manipule des objets de classe `array` de `numpy` *chargés en mémoire* et donc de taille limitée par la RAM de l'ordinateur; de façon analogue R charge en RAM des objets de type `data.frame`.
- `Scikit-learn` reconnaît quelque fois la classe `DataFrame` de `pandas`. Une variable binaire est simplement remplacée par un codage *(0,1)* mais, en présence de plusieurs modalités, traiter celles-ci comme des entiers n'a pas de sens statistique et remplacer une variable qualitative par l'ensemble des indicatrices (*dummy variables (0,1)*) de ses modalités  complique les stratégies de sélection de modèle tout en rendant inexploitable l'interprétation statistique. 
- Les implémentations en Python de certains algorithmes dans `scikit-learn` sont souvent rapide et utilisent implicitement les capacités de parallélisation.


## Les fonctions d'apprentissage de Scikit-learn
La communauté qui développe cette librairie est très active et la fait évoluer très rapidement.  Ne pas hésiter à consulter la [documentation](http://scikit-learn.org/stable/user_guide.html) pour des compléments. Voici une sélection de ses principales fonctionnalités en lien avec la modélisation : 

- Transformations (standardisation, discrétisation binaire, regroupement de modalités, imputations rudimentaires de données manquantes) , "vectorisation" de corpus de textes (encodage, catalogue, Tf-idf), images;
- Modéle linéaire général avec pénalisation (ridge, lasso, elastic net...), analyse discriminante linéaire et quadratique,  $k$ plus proches voisins,  processus gaussiens, classifieur bayésien naïf, arbres de régression et classification (CART), agrégation de modèles (bagging, random forest, adaboost, gradient tree boosting), perceptron multicouche (réseau de neurones), SVM (classification, régression, détection d'atypiques...);
- Algorithmes de validation croisée (loo, k-fold, VC stratifiée...) et sélection de modèles, optimisation sur une grille de paramètres, séparation aléatoire apprentissage et test, courbe ROC;
- Enchaînement (*pipeline*) de traitements.

En résumé, cette librairie est focalisée sur les aspects "machine" de l'apprentissage de données quantitatives (séries, signaux, images) volumineuses. 

## L'objectif de cette séance  
Illustrer la mise en oeuvre de quelques fonctionnalités ainsi que apprendre à consulter la [documentation](http://scikit-learn.org/stable/user_guide.html) et ses nombreux [exemples](http://scikit-learn.org/stable/auto_examples/index.html) pour plus de détails sur les possibilités d'utilisation de `scikit-learn`. 

Des jeux de données "template" sont utilisés, qui regroupe des variables qualitatives et quantitatives (généralement dans un objet de la classe `DataFrame`). Pour être utilisé dans `scikit-learn` les données doivent souvent être transformées en un objet de classe `Array` de `numpy` par le  remplacement des variables qualitatives par les indicatrices de leurs modalités.

## Tips 
Il est recommandé de prendre son temps pour bien lire les scripts et ne pas hésiter à consulter [la documentation en ligne](https://scikit-learn.org/stable/documentation.html)


