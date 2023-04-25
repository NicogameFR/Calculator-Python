Création d’une Calculatrice Multifonctions en Python










**Baptiste Hustaix, Arthur Burugorri, Leonardo Amoretti de Stephanis, Enzo Bossian**

***Exercice 21 p 59***






Notre projet est de créer une calculatrice à quatre opérations sur Python.

Au début de notre projet, le but a été de créer un programme qui nous permet d’obtenir une calculatrice classique et fonctionnelle. Pour cela, dans un premier temps, nous avons écrit un programme permettant d’obtenir un affichage correct et les fonctionnalités d’une calculatrice à quatre opérations, puis, dans un second temps, nous avons ajouté le mode alpha, le mode second, les racines carrées, la possibilité de revenir sur des calculs précédents… Enfin, nous avons ajouté Python à notre calculatrice pour avoir comme résultat une calculatrice qui s’approche le plus possible à notre calculatrice lycée.

**Cahier des charge et structure du projet :**

Nous avons commencé par nous occuper de l’onglet calcul, dans celui-ci, nous voulions pouvoir avoir la possibilité d’avoir un affichage des calculs et l’affichage des résultats, de naviguer entre les sauvegardes (résultats et expressions précédentes) avec les flèches de la calculatrice, d’ajouter à l’option répétition d’un calcul ou l’option vérification d’un calcul et l’option avec des variables. On retrouve dans la calculatrice deux types d’affichages : le format classique des expressions que l'on retrouve sur l'affichage de l’onglet calcul et celui que l’on retrouve dans l’onglet Python, une traduction des expressions en langage naturel en langage Python. Nous avons créé une fonction qui va convertir le calcul de manière que ce soit compréhensible par Python (formatage(z)). L’ajout du mode second et alpha permet d’ajouter des touches supplémentaires. La calculatrice possède aussi la possibilité de convertir la notation décimale en notation fractionnaire et inversement. De plus, la possibilité de désactiver les touches inutiles en fonction du mode activé.

Pour l’onglet Python, nous avons donné la possibilité de changer les touches pour convenir en Python, et pour que la calculatrice soit “autonome”, c’est-à-dire, elle va pouvoir utiliser Python, soit avec le clavier, la souris, l'affichage de la console. 

**Étape 1 :** Le premier objectif est de créer les boutons et la zone de texte de l’interface de la calculatrice or sans définir les fonctions de rappel pour l’instant.

Dans un premier temps, on a utilisé la librairie nsi\_ui. Nous avons rencontré un problème par rapport à l'alignement des colonnes donc nous avons décidé d’utiliser la bibliothèque tkinter. Cependant, plus complexe, elle permet néanmoins un meilleur rendu.

**Etape 2** : Amélioration 

Dans un second temps, après avoir créé une interface convenable, nous avons pensé qu’il serait intéressant d’ajouter plus d'options de calcul pour ne pas avoir qu’une simple calculatrice à quatre opérations, car nous avions envie de nous dépasser, de ce fait vient l’ajout du mode alpha et second dans l’interface calcul qui permet une grande extension de la calculatrice. Pour finir, nous avons ajouté Python à la calculatrice, ce qui permet d'avoir la possibilité de programmer directement sur la calculatrice.



**Etape 3:** Brouillons et commencement de la programmation

Après avoir incorporé les améliorations que nous souhaitions ajouter, nous avons commencé l’étape des brouillons pour pouvoir être plus efficace lors de la programmation.

C’est ensuite, avec une vision claire de nos objectifs, que la programmation a commencé. Nous nous sommes résignés sur un grand nombre de pages web pour apprendre à utiliser les bibliothèques et de mettre en pratique leurs fonctionnalités essentielles à l'exécution du programme et donc à la réalisation du projet.

**Principales fonctions :**

Comme principale fonction, nous retrouvons par exemple :

**Config\_button():** qui sert à configurer chaque bouton en fonction des modes et options activés. Elle nous permet aussi de répéter le processus pour chaque possibilité de combinaison d'option et de mode, ainsi cette fonction agit sur l’ensemble des touches et suit la liste des numéros des boutons que vous pouvez trouver sur les brouillons qui vont être modifiés et dont le nom va changer. Cette fonction est primordiale pour la calculatrice, elle s’implique peu importe le mode ou l’option choisie.

**def config\_affichage():** qui permet de configurer l'affichage des fenêtres en fonction du mode. Fait appelle à la fonction config\_button() pour configurer ce que fait chaque bouton sauf ceux configurés au début.

**def executer():** sert à ce que la fonction python qui permet de récupérer le code entré par l'utilisateur, de l'exécuter et de remplir une zone de texte avec le résultat. C’est la seule commande du programme qui utilise la bibliothèque subprocess et sys.

**def formatage(z):** Sert de manière que lorsque la fonction formater la saisie, Python puisse le comprendre en tant que calcul. On retrouve dans la fonction, une partie qui remplace les caractères utilisés à l'écrit en caractères compréhensibles par python, une partie qui supprime les caractères sto →, la variable entrée reçoit le résultat de l'opération pour pouvoir le sauvegarder (dans la calculatrice, l'ajout de sto permet d'assigner une valeur à une variable) et une partie qui remplace l'inconnue par sa valeur dans une opération.

**Interaction homme/machine et test :**

L’interaction homme machine sur notre calculatrice se veut être le plus pratique possible et le plus simple possible d’utilisation, de ce fait, nous avons essayé d’avoir la calculatrice la plus claire et précise possible pour l’utilisateur. Grâce à la bibliothèque tkinter, nous avons un rendu très clair et une utilisation complète.




Pour le premier modèle, on y retrouve des calculs avec de simples priorités de calcul.












Dans ce second modèle, on y retrouve aussi les priorités de calcul avec parenthèses, la racine carrée, les puissances et les vérifications.








Dans le troisième modèle, on retrouve lorsqu'on donne une valeur à x et lorsqu’on donne une valeur à y puis lorsqu’on multiplie x et y et une vérification de 6 supérieurs ou égal à 2


Dans le quatrième modèle, on retrouve le mode second lorsqu’il est activé et l’affichage qu’il propose avec ces touches associées. Dans le cinquième modèle, on retrouve le mode alpha lorsqu’il est activé et son affichage, de même pour le sixième modèle, c’est le mode alpha et second qui est activé en même temps.









Pour le septième modèle, on retrouve le mode python avec un programme écrit que l’on applique et dans le huitième modèle, toujours dans le mode, le résultat du programme écrit dans le modèle précéda

**Les bibliothèques :** Les bibliothèques que nous avons utilisées sont la bibliothèque nsi\_ui et la bibliothèque tkinter, mais pour notre programme final, nous n’avons utilisé que la bibliothèque tkinter, car suite à des erreurs d’affichage et un manque de fonctionnalités de la bibliothèque nsi\_ui, nous avons utilisé la bibliothèque tkinter qui nous permettait, par exemple, de pouvoir modifier la taille des touches de la calculatrice à notre guise, et c’est aussi ce que nous a permis de proposer une calculatrice aussi complète. Nous avons aussi utilisé les bibliothèques maths, tkinter.font, fractions, subprocess et sys qui permettent le bon fonctionnement de la calculatrice. 

**Répartition des tâches et outils de travail et horaires :** Pour la répartition des tâches, nous diviser le travail en quatre Baptiste s’est occupé de toute la partie codage, pour Arthur, il s’est occupé de voir s'il n’y avait des bugs ou des erreurs de frappes, pour Leonardo s'est occupé du PowerPoint et pour ma part, j'ai fait le Word (le dossier). Pour les outils de travail, Baptiste et Arthur ont utilisé Visual studio code et Replit pour le code, Leonardo a utilisé PowerPoint, PowerPoint slide et pour ma part, je me suis servi de Google docs. Pour ce qui est des présentations et pour le partage de fichiers et des informations, nous avons utilisé Google drive. Et pour les horaires, cela a été aux alentours de 20 à 25 heures soit 2 à 3 heures par jours pendant les vacances pour la partie codage, pour ma part pour le dossier, cela était aux alentours de 7 heures, le temps de tout tester, la rédaction et de la mise en page et pour Leonardo.

Ce que nous a apporté ce projet est de réellement voir ce qu’est un travail de groupe, avec les bons, mais aussi les mauvais côtés. Il était assez compliqué de se coordonner malgré un certain nombre d'échecs. Comme Baptiste, c'est avancé très vite sur le codage et que dans notre groupe, nous n’avons pas tous le même niveau en codage, Baptiste s’est vite retrouvé tout seul sur la partie codage pure, mais malgré cela chacun a su trouver comment participer et s’est renseigné sur comment comprendre le programme. Ce projet nous a demandé beaucoup de travail personnel (en particulier Baptiste qui a dû énormément naviguer pour pouvoir comprendre un maximum la bibliothèque, mais cela s’applique aussi pour Leonardo qui a fait le PowerPoint de son côté chez lui ou pour moi pour faire le Word). À la fin du projet, le groupe a su communiquer, mais malheureusement tardivement. Nous avons appris de nos erreurs. Globalement, tout le monde a su se trouver une place dans le groupe et nous a permis de progresser.
