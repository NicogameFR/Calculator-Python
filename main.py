# -*- coding: utf-8 -*-
# importe les bibliothèques utilisées

# tkinter pour l'affichage des fenêtres et des boutons l'importe et la nomme tk pour plus de simplicité
import tkinter as tk
# math pour pouvoir utiliser les opérations plus complexes
from math import *
# tkinter.font pour la pouvoir modifier la police et le soulignage des caractères
import tkinter.font as font
# fraction pour pouvoir convertir les résultats en fraction
from fractions import *
# subprocess pour l'affichage de la console dans la fenêtre tkinter
import subprocess
# sys pour connaître le chemin d’accès vers l'interpréteur Python utilisé
import sys


# Les touches

# défini les touches affichées sur la calculatrice en mode calcul de base
touches = [
    "   2nde   ", " Calcul ", " Python ", "     ↑     ", "     ↓     ", "Alpha", "OFF", "Rep", "←", '→', "x", "y", "√(", "^", "◀ ▶", "=", "(", ")",
    "/", "²", '7', "8", "9", "*", "suppr", "4", "5", "6", "-", "annul", "1", "2", "3", "+", 'C', '.', "0", " sto → ", "exe", "enter"
]

# défini les touches affichées sur la calculatrice en option seconde et mode calcul
touches_mode_seconde = [
    "   2nde   ", " Calcul ", " Python ", "     ↑     ", "     ↓     ", "Alpha", "OFF", "Rep", "←", '→', ":", "#", "<", ">", "≠", "⩽",
    "⩾", "{", '}', "[", "]", "%", "'", '"', "suppr", "&", "|", "-", "~", "annul", "!", "?", "_", "\\\\", 'C', ',', "◡", "π", "Indent", "enter"
]

# défini les touches affichées sur la calculatrice en option alpha (mode python et calcul)
touches_mode_alpha = [
    "   2nde   ", " Calcul ", " Python ", "     ↑     ", "     ↓     ", "Alpha", "OFF", "Rep", "←", '→', "a", "b", "c", "d", "e", "f", "g", "h",
    "i", "j", 'k', "l", "m", "n", "suppr", "o", "p", "q", "r", "annul", "s", "t", "u", "v", 'C', 'w', "x", "y", "z", "enter"
]

# défini les touches affichées sur la calculatrice en option alpha et seconde activées simultanément (mode python et calcul)
touches_seconde_alpha = [
    "   2nde   ", " Calcul ", " Python ", "     ↑     ", "     ↓     ", "Alpha", "OFF", "Rep", "←", '→', "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", 'K', "L", "M", "N", "suppr", "O", "P", "Q", "R", "annul", "S", "T", "U", "V", 'C', 'W', "X", "Y", "Z", "enter"
]

# défini les touches affichées sur la calculatrice en mode python de base
touches_python = [
    "   2nde   ", " Calcul ", " Python ", "     ↑     ", "     ↓     ", "Alpha", "OFF", "Rep", "←", '→', "x", "y", "sqrt(", "**", "◀ ▶", "=", "(", ")",
    "/", "**2", '7', "8", "9", "*", "suppr", "4", "5", "6", "-", "annul", "1", "2", "3", "+", 'C', '.', "0", " sto → ", "exe", "enter"
]

# défini les touches affichées sur la calculatrice en option seconde et mode python
touches_mode_seconde_python = [
    "   2nde   ", " Calcul ", " Python ", "     ↑     ", "     ↓     ", "Alpha", "OFF", "Rep", "←", '→', ":", "#", "<", ">", "!=", "<=",
    ">=", "{", '}', "[", "]", "%", "'", '"', "suppr", "&", "|", "-", "~", "annul", "!", "?", "_", "\\\\", 'C', ',', "◡", "pi", "Indent", "enter"
]


# Les non-fonctions (configurations de base)


# crée la fenêtre principale et la nomme "Calculatrice"
Calculatrice = tk.Tk()

# change le titre affiché sur la fenêtre en "Calculatrice"
Calculatrice.title("Calculatrice")

# donne une taille minimale à la fenêtre
Calculatrice.minsize(width=550, height=900)

# défini une sous fenêtre de Calculatrice nommée carre_affichage dans laquelle sera affiché les calculs en mode calcul
carre_affichage = tk.Frame(Calculatrice)

# affiche cette sous fenêtre, l'autorise à s’étendre dans toute la fenêtre parente et l'autorise à s'agrandir si celle-ci s'agrandit
carre_affichage.pack(expand='true', fill="both")

# défini une sous fenêtre de Calculatrice nommée carre_affichage dans laquelle on affichera les boutons
button_affichage = tk.Frame(Calculatrice)

# affiche cette sous fenêtre, l'autorise à s’étendre dans toute la fenêtre parente et l'autorise à s'agrandir si celle-ci s'agrandit
button_affichage.pack(side='bottom', fill="both", expand='true')

# on crée les 8 zone d'affichage/espaces alloués pour afficher les sauvegardes/widget Label.
# va de 7 à 0 compris. Donc Le premier Label s'appelle Resultat7 et le dernier Resultat0
for i in range(7, -1, -1):
    if i == 0 or i % 2 == 0:  # si le numéro du bouton est pair ou est égal a 0
        exec(
            f'Resultat{i} = tk.Label(carre_affichage, justify = "center",padx=10, anchor = "e")')
        # on définit le parent comme étant carre_affichage
        # on le configure de manière que chaque résultat d'opération s'affiche sur la droite 'e' pour 'est'(la direction) (anchor = "e")
        # on le justifie au centre de sa zone de texte (justify = "center")
        # on laisse un espace 10 pixels sur les côtés grâce à padx=10 pour que ce soit plus clair
    else:
        exec(
            f'Resultat{i} = tk.Label(carre_affichage, justify = "center",padx=10, anchor = "w")')
        # on le configure de manière que chaque résultat d'opération s'affiche sur la droite, 'w' pour 'ouest' ou 'west'  en anglais
        # on le justifie au centre de sa zone de text
        # on laisse un espace 10 pixels sur les côtés grâce à padx=10 pour que ce soit plus clair
    # on affiche les 8 labels et on leur donne comme propriétés de s’agrandir avec la fenêtre parente (expand = "true") et de remplir tout l'espace qui lui est alloué (fill = "both").
    exec(f'Resultat{i}.pack(expand = "true",fill = "both")')
    # on donne une police de 15 aux caractères qui sont dans ces zones d'affichages
    exec(f'Resultat{i}["font"] = font.Font(size = 15)')


# on crée 2 polices :
# font_normal qui n'est pas souligné et qui a une taille de 15
# font_souligne qui est souligné et qui a une taille de 15
font_normal = font.Font(underline=False, size=15)
font_souligne = font.Font(underline=True, size=15)


# on crée une zone d'insertion de texte qui servira à entrer le code python et qui a pour propriétés de :
# être dans carre_affichage
# que si le texte va dépasser la limite des bordures de la fenêtre, on revient à la ligne (le programme considère que le texte est sur la même ligne tout de même)
# avoir une hauteur de 20 lignes (height=20)
# avoir une largeur de 50 caractères (width=50)
Python = tk.Text(carre_affichage, wrap='word', height=20, width=50)
Python.forget()  # on la cache


# on crée une 2ᵉ zone d'insertion de texte qui servira à afficher la console python sur le mème modèle que précédemment
Console = tk.Text(carre_affichage, wrap='word', height=20, width=50)
Console.forget()  # on la cache


# on crée une 3ᵉ zone d'insertion de texte qui servira à récupérer le texte entré par l'utilisateur dans le mode calculatrice
# on justifie le texte au centre
Entree_operation = tk.Entry(justify="center")
# on l'affiche ce widget
Entree_operation.pack(expand="true", fill="both")
# on met le curseur d’insertion à l’intérieur
Entree_operation.focus()
# on met une police de 20 comme taille
Entree_operation["font"] = font.Font(size=20)


# on crée une grille dans laquelle on va afficher les boutons
for i in range(5):  # 5 boutons par ligne
    # on configure donc une grille qui comprend 5 colonnes (column en anglais) qui occupent toutes le même espace de 1 (weight=1)
    button_affichage.grid_columnconfigure(i, weight=1)
for i in range(8):  # 8 lignes
    # on configure donc une grille qui comprend 8 lignes (row en anglais) qui occupent toutes le même espace de 1 (weight=1)
    button_affichage.grid_rowconfigure(i, weight=1)


# dans l'affichage il y a 5 boutons par ligne et 8 lignes donc 8×5=40 boutons
for i in range(8):  # représente les lignes
    for j in range(5):  # représente les colonnes
        # p = le numéro du bouton en fonction de sa ligne et de son rang sur la ligne (sa colonne)
        p = (5*i)+j
        # on attribue a chaque bouton un texte qui va être affiché dessus. Celui-ci dépend de {p}
        exec(f'button{p} = tk.Button(button_affichage, text="{touches[p]}")')
        exec(
            f'button{p}.grid(rowspan=1 ,column={j}, row={i}, sticky="nswe",padx=10, pady=10)')
        # on place le bouton sur la grille en spécifiant qu'il doit :
        # rowspan=1: occuper une seule casse
        # column={j} aller a la colonne {j}
        # row={i}: aller a la ligne {i}
        # sticky="nswe": s’étendre dans toutes les directions (nord, sud, est et "west"en anglais)
        exec(f'button{p}["font"] = font.Font(size = 15)')
        # on met la police de chaque bouton à une taille de 15
        # en suite, on configure les boutons qui font appel à une fonction
        if p == 0:  # si le numéro du bouton est 0 alors
            # quand on appuiera dessus (lambda:) on exécutera la fonction (mode_seconde())
            button0.config(command=lambda: mode_seconde())
        if p == 1:
            # ce bouton est désactivé de base, car il active le mode calcul, mais il est par défaut activé, donc on le bloque
            button1.config(stat='disabled', command=lambda: mode_calcul())
        if p == 2:
            button2.config(command=lambda: mode_python())
        if p == 3:
            # on ajoute une en argument pour ne pas provoquer d'erreur (il est vide et n'existe pas vraiment). La fonction haut() possède un argument nommé event qui permet d'activer la fonction lors de l’appui d'une touche du clavier.
            button3.config(command=lambda: haut(e))
        if p == 4:
            button4.config(command=lambda: bas(e))  # idem que pour button3
        if p == 5:
            button5.config(command=lambda: mode_alpha())
        if p == 6:
            button6.config(command=lambda: exit())
        if p == 7:
            # la touche rep utilise la fonction operation en donnant comme argument la variable Rep
            button7.config(command=lambda: operation(str(Rep)))
        if p == 8:
            button8.config(command=lambda: gauche())
        if p == 9:
            button9.config(command=lambda: droite())
        if p == 14:
            button14.config(command=lambda: ecriture())
        if p == 24:
            button24.config(command=lambda: effacer())
        if p == 29:
            button29.config(command=lambda: annulation())
        if p == 34:
            button34.config(command=lambda: reset())
        if p == 38:
            button38.config(command=lambda: executer())
        if p == 39:
            button39.config(command=lambda: egal(e))  # idem que pour button3


# Variables globales
var_ecriture = 0  # variable binaire, active et désactive le mode fraction
var_seconde = 0  # variable binaire, active et désactive le mode seconde
var_alpha = 0  # variable binaire, active et désactive le mode alpha
# variable binaire qui active et désactive le mode calcul (par défaut activé)
var_calcul = 1
var_python = 0  # variable binaire qui active et désactive le mode python

# La sélection est la valeur qui est soulignée lors que l'utilisateur appuis sur la touche haut ou bas en mode calcul
# nombre d'opérations sauvegardées. Compris dans [0;+ထ[. save_max-1 correspond au numéro de la dernière sauvegarde.
save_max = 0
# Si hauteur = 0: pas de sélection. Si hauteur ∈ [1;8], hauteur correspond à la hauteur de la sélection par rapport aux espaces alloué pour afficher les sauvegardes.
hauteur = 0
# nombre de sauvegardes entre la sauvegarde qui est sélectionnée et la sauvegarde la plus récente. affichage ∈ [0;+ထ[. Si affichage = 0 il n'y a pas de sélection
affichage = 0
ligne = 0  # nombre de lignes qui se sont affichés en plus au-dessus des espaces alloués pour afficher les sauvegardes afin d'afficher les sauvegardes plus anciennes lorsque la sélection le demande.
# lorsque affichage⩽8 il n'y a pas besoin d'afficher les sauvegardes plus anciennes donc ligne reste à 0. Sinon lors de la première exécution de haut() ligne ∈ [1;+ထ[

x = 0  # variable x qui peut être modifier dans la calculatrice
y = 0  # variable y qui peut être modifier dans la calculatrice
Rep = ""  # variable qui va contenir la répétition de la sélection.

# Fonctions principales

# Fonction egal()
# version calcul: permet d'effectuer le calcul saisit par l'utilisateur et de le stocker dans une variable de sauvegarde qui sera affichée. egal() stocke également le calcul pour qu'il soit affiché au-dessus du résultat
# version python: permet de faire un saut de ligne dans l'interface python


def egal(event):  # l'argument "event" permet de lier la fonction à l'appui de la touche 'enter' du calvier. Nous reverrons ça à la fin du programme
    if var_calcul == 1:  # si le mode calcul est avivé
        if Entree_operation.get() == '':
            return
        global Rep  # j'appelle 6 variable globales que je vais modifier lors de l'execution
        global save_max
        global hauteur
        global ligne
        global affichage
        global var_ecriture
        # je mets le contenu entré par l'utilisateur et je le mets dans une variable globale que je nomme save{le nombre de sauvegardes précédentes} pour obtenir un nom unique
        # exec() permet d’exécuter une commande dans un espace fermé ( comme si elle était dans une fonction). Si on veut modifier une variable à l’intérieur, il faut la globaliser.
        exec(f'globals()["save{save_max}"]=Entree_operation.get()')
        # j'ajoute 1 à save_max pour que la prochaine valeur ne s’enregistre pas dans une variable déjà remplie
        save_max = save_max + 1
        # j'essaie d’exécuter 2 commande
        try:  # en premier lieu, je formate en langage python grâce à formatage() le contenu entré par l'utilisateur, ensuite le l’évalue (cette fonction considère que le résultat de formatage() est une opération et la calcule) enfin, je transforme le résultat en caractère. Je mets le tout dans la dernière sauvegarde
            # exemple : str(eval(formatage(4²))) = str(eval(4**2)) = str(8) = '8'
            exec(
                f'globals()["save{save_max}"]=str(eval(formatage(Entree_operation.get())))')
        except:  # si ce processus échoue (l'utilisateur a entré des caractères qui ne peuvent pas être évalués) je mets un message d'erreur dans la dernière sauvegarde
            exec(
                f'globals()["save{save_max}"]="Erreur !!! Vérifiez la syntaxe"')
        # je crée une variable temporaire qui va me permette de garder en mémoire le contenu de save_max et de le modifier sans modifier le contenu de la variable globale. save_max-1 correspond donc au numéro de la véritable dernière sauvegarde.
        temp = save_max
        if save_max < 8:  # s'il existe moins de 8 sauvegardes, je configure chaque espace alloué pour afficher les sauvegardes avec les x dernières sauvegardes.
            # répète le processus autant de fois qu'il y a de sauvegarde
            for i in range(save_max+1):
                # Resultat{i} est le nom donné à chacun des 8 espaces alloué pour afficher les sauvegardes. premier espace = Resultat0 dernier espace Resultat7. D'où une hauteur max de 8. Il n'y a pas de 9ᵉ espace d’écriture
                exec(f'Resultat{i}.config(text = save{temp})')
                temp = temp-1  # je retranche 1 pour assigner une sauvegarde différente pour chaque espace
        else:  # s'il existe plus que 8 sauvegardes, je configure uniquement avec les 8 dernières sauvegardes.
            for i in range(8):
                exec(f'Resultat{i}.config(text = save{temp})')
                temp = temp-1
        save_max = save_max + 1  # j'ajoute 1 à save_max pour préparer le prochain passage dans la fonction égal et configurer la prochaine sauvegarde avec un nom différent de la précédant
        # je remets tous les compteurs de la sélection à 0
        hauteur = 0
        ligne = 0
        affichage = 0
        var_ecriture = 0  # je remets l'écriture décimale en écriture pas défaut
        Rep = ""  # je vide la variable qui contient la répétition de la sélection, car la sélection disparaît
        # je mets en mode non souligné tous les affichages
        for i in range(8):
            exec(f'Resultat{i}.config(font=font_normal)')
        # je supprime le contenu entré par l'utilisateur
        Entree_operation.delete(0, 'end')
    if var_python == 1:  # si python est activé
        # insérer un retour à la ligne à l'endroit du curseur d’insertion
        Python.insert('insert', '\n')


# Fonction formatage()
# Fonction qui formate la saisie pour que python puisse le comprendre en tant que calcul
def formatage(z):
    global x  # on appelle 3 fonctions globales
    global y
    global Rep
    # cette partie remplace les caractères utilisés à l’écrit en caractères compréhensibles par python
    # remplace '=' par un double égal "==" pour déclencher la vérification par python lors du passage dans la fonction eval() (le résultat sera soit 'TRUE' soit 'FALSE')
    if '=' in z:
        z = z.replace("=", "==")
    # idem pour ≠
    if '≠' in z:
        z = z.replace("≠", "!=")
    # idem pour ⩽
    if '⩽' in z:
        z = z.replace("⩽", "<=")
    # idem pour ⩾
    if '⩾' in z:
        z = z.replace("⩾", ">=")

    # remplace ² par **2 et ainsi de suite
    if '²' in z:
        z = z.replace("²", "**2")
    if '^' in z:
        z = z.replace("^", "**")
    if '√' in z:
        z = z.replace("√", "sqrt")
    if "π" in z:
        z = z.replace("π", "pi")

    # ajoute des signes multipliés entre chaque symbole pour pouvoir faire comprendre à python l'écriture simplifiée
    # exemple: x(15-5) devient x*(15-5)
    if 'pix' in z:
        z = z.replace("pix", "pi*x")
    if 'yx' in z:
        z = z.replace("yx", "y*x")
    if 'piy' in z:
        z = z.replace("piy", "pi*y")
    if 'xy' in z:
        z = z.replace("xy", "x*y")
    if 'xpi' in z:
        z = z.replace("xpi", "x*pi")
    if 'ypi' in z:
        z = z.replace("ypi", "y*pi")
    if 'x(' in z:
        z = z.replace("x(", "x*(")
    if 'y(' in z:
        z = z.replace("y(", "y*(")
    if 'pi(' in z:
        z = z.replace("pi(", "pi*(")
    if 'xsqrt' in z:
        z = z.replace("xsqrt", "x*sqrt")
    if 'ysqrt' in z:
        z = z.replace("ysqrt", "y*sqrt")
    if 'pisqrt' in z:
        z = z.replace("pisqrt", "pi*sqrt")
    # fait la même chose, mais avec des nombres devant à la place des opérations ou des caractères
    # exemple : 3(15-10) devient 3*(15-5)
    for i in range(10):
        temp = str(i)+"sqrt"
        if temp in z:
            z = z.replace(temp, str(i)+"*sqrt")
        temp = str(i)+"("
        if temp in z:
            z = z.replace(temp, str(i)+"*(")
        temp = str(i)+"pi"
        if temp in z:
            z = z.replace(temp, str(i)+"*pi")
        temp = str(i)+"x"
        if temp in z:
            z = z.replace(temp, str(i)+"*x")
        temp = str(i)+"y"
        if temp in z:
            z = z.replace(temp, str(i)+"*y")
    # cette partie supprime les caractères sto →, la variable entrée reçoit le résultat de l'opération pour pouvoir le sauvegarder
    # dans la calculatrice l'ajout de sto permet d'assigner une valeur à une variable
    if '%' in z:
        z = z.replace("%", "/100")
    if ' sto → y' in z:  # exemple : '80 sto → y'
        z = z.replace(" sto → y", "")  # je supprime ' sto → y' #exemple : '80'
        y = z  # je remplis la variable globale y avec le reste #exemple : y = '80'
    if ' sto → x' in z:
        z = z.replace(" sto → x", "")
        x = z
    # cette partie remplace l’inconnue par sa valeur dans une opération
    if 'x' in z:
        z = z.replace('x', x)
    if 'y' in z:  # exemple : y*2
        z = z.replace('y', y)  # exemple 80*2
    return z


# Fonction haut()
# version calcul : permet de faire descendre les sauvegardes sur les espaces alloués pour afficher les sauvegardes pour afficher des sauvegardes plus anciennes
# version python : permet de déparer le curseur d’insertion vers le haut dans l'interface python
def haut(event):  # l'argument "event" permet de lier la fonction à l'appui de la touche 'flèche vers le haut' sur le clavier. Nous reverrons ça à la fin du programme
    if var_calcul == 1:  # si calcul est activé :
        global ligne  # appelle 3 valables globales
        global hauteur
        global affichage
        # sélection montre de 1 donc la distance entre la dernière sauvegarde et la sélection augmente de 1
        affichage = affichage + 1
        # la hauteur de la sélection sur les espaces augmente de 1 donc la sélection sera positionnée sur l'espace du dessus.
        hauteur = hauteur + 1
        temp = save_max-1  # je crée une variable temporaire qui va me permette de garder en mémoire le contenu de la véritable save_max et de le modifier sans modifier le contenu de la variable globale. Voir fonction egal() pour comprendre pourquoi save_max-1
        # affichage est une variable qui est comprise dans [1;+ထ[ à partir de sa première exécution alors que temp ∈ [0;+ထ[, on enlève 1 pour qu'il soit sur une même base et connaître quelle valeur de save correspond à quelle valeur d'affichage.
        if affichage-1 >= temp:
            # On vérifie ensuite si affichage déplace le nombre maximum de sauvegardes, que la sélection monte plus qu'il n'y a de sauvegardes. On ne peut pas sélectionner une sauvegarde qui n'existe pas donc on ajuste les valeurs
            # si la vraie sauvegarde maximum est inférieure à 8 (c'est-à-dire qu'il n'y a pas assez de sauvegarde pour remplir tous les espaces)
            if temp < 8:
                # hauteur est une variable qui est comprise dans [1;8] à partir de sa première exécution alors que temp va de 0 à 7, on ajoute 1 à temp pour qu'ils soient sur une même base et mettre hauteur sur le numéro maximum de save.
                hauteur = temp+1
                ligne = 0  # s'il y a moins de 8 sauvegarde, il n'y a pas de lignes supérieures donc on met ligne à 0
                # en dessous de 8 affichages, affichage = hauteur, car les 2 distances sont les mêmes
                affichage = hauteur
                # on met le contenu de la sauvegarde sur laquelle on a la sélection dans la variable globale Rep
                exec(f'global Rep\nRep = save{temp-affichage+1}')
                # on configure le soulignage pour que l'utilisateur sache sur quelle sélection il se trouve
                # décalage de 1 entre hauteur et les espace de Resultat{x}  donc on les met sur la même base.
                # on configure l'espace sur laquelle la sélection est soulignée
                exec(f'Resultat{hauteur-1}.config(font=font_souligne)')
                # on configure l'espace précédent en normal (sans soulignage)
                exec(f'Resultat{hauteur-2}.config(font=font_normal)')
            else:  # s'il y a plus que 8 sauvegardes la sélection doit se bloquer sur l'espace le plus haut
                # je mets la hauteur à 8 (valeur maximum pour hauteur)
                hauteur = 8
                # augmente affichage de 1 pour configurer la sélection sur la première sauvegarde
                affichage = temp + 1
                # la variable Rep prend la valeur de la première sauvegarde
                exec(f'global Rep\nRep = save0')
                # on configure les espaces pour que seul le dernier espace soit souligné
                Resultat7.config(font=font_souligne)
                Resultat6.config(font=font_normal)
            return  # stoppe la fonction
        # si la hauteur déplace 8. La sélection vaut monter plus haut qu'il n'y a d'espace.
        elif hauteur > 8:
            ligne = ligne + 1  # j'ajoute une ligne. chaque ajout de ligne comprend en fait 2 espace, un pour le calcul et un pour le résultat
            for i in range(8):
                # je configure chaque espace pour qu'il reçoive les bonnes valeurs de sauvegardes.  {temp-2*ligne-i} indique le numéro de la sauvegarde sur lequel il doit être affiché.
                exec(f'Resultat{i}.config(text = save{temp-2*ligne-i})')
                # il correspond à  (la sauvegarde max - le nombre d'espaces ajoutés - i) pour qu'il soit différent pour chaque espace.
            # exemple si vrai save_max = 9 et si ligne= 1. Donc, il faut descendre les valeurs affichées de 2. 'i' correspond au numéro de l'espace (Resultat{x}).
            Resultat6.config(font=font_souligne)
            # on a ainsi pour le premier espace (Resultat0): save{9-2*1-0} soit save7. L'espace le plus en bas de l'affichage va de ce fait prendre la valeur de save7. On répète le processus pour les 7 autres espaces.
            Resultat7.config(font=font_normal)
            hauteur = 7  # la hauteur prend la valeur 7, car la sélection se met sur l'espace résultat et non l'espace calcul
            # on met le contenu de la sauvegarde sur laquelle on a la sélection dans la variable globale Rep
            exec(f'global Rep\nRep = save{temp-affichage+1}')
            return  # met fin a la fonction
        else:  # pour le reste, si hauteur⩽8
            # cette partie s'active pour les 8 premières utilisations de la fonction haut()
            # on souligne l'espace sur lequel se situe la sélection
            exec(f'Resultat{hauteur-1}.config(font=font_souligne)')
            if hauteur > 1:
                # s'il y a un espace en dessous, on enlève le soulignage. Ne s'active pas pour la première utilisation de la fonction haut()
                exec(f'Resultat{hauteur-2}.config(font=font_normal)')
            # on met le contenu de la sauvegarde sur laquelle on a la sélection dans la variable globale Rep
            exec(f'global Rep\nRep = save{temp-affichage+1}')
            return  # on met fin à la fonction
    if var_python == 1:  # si le mode python est activé
        # exemple dans : Bonjo|ur!
        # '|' correspond au curseur d’insertion dans l'exemple
        # 'insert' correspond au nom du curseur d’insertion pour python
        # on stocke la position du curseur d’insertion (en réalité, c'est la valeur pour le caractère positionné juste après le curseur d’insertion) sous la forme X.Y correspond à la Xeme ligne et au Y+1eme caractère. X varie de 1 à +ꝏ et Y de 0 à +ꝏ d'où le Y+1
        position = Python.index('insert')
        #exemple : position = 1.5
        # je localise la position du point dans X.Y pour savoir où se situe la frontière entre la valeur des lignes et la valeur des caractères
        pos = position.find('.')
        # exemple : pos = 1 donc le 2ᵉ caractère
        # extrait de position les caractères compris entre le début et le '.'
        line = int(position[:pos])
        #exemple : line = 1
        # extrait de position, les caractères compris entre le '.' et la fin (la longueur totale de position)
        column = int(position[pos+1:len(position)])
        #exemple : column = 5
        # on positionne le curseur d’insertion sur la ligne du haut. S'il n'y a pas de ligne au-dessus, le curseur d’insertion est placé au début de la ligne.
        Python.mark_set('insert', "%d.%d" % (line-1, column))
        # exemple : |Bonjour!
        # dans cette notation, on a le premier %d qui correspond à line-1 et le second à column. Cela revient au même que de rentrer f'{line-1}.{column}'. J'ai trouvé intéressant de présenter une autre notation que celle utilisée and le reste du programme


# Fonction bas()
# version calcul : permet de faire descendre les sauvegardes sur les espaces alloués pour afficher les sauvegardes pour afficher des sauvegardes plus anciennes
# version python : permet de déparer le curseur d’insertion vers le haut dans l'interface python
def bas(event):  # l'argument "event" permet de lier la fonction à l'appui de la touche 'flèche vers le bas' sur le clavier. Nous reverrons ça à la fin du programme
    if var_calcul == 1:  # si le mode calcul est activé
        global hauteur  # on appelle 3 valables globales
        global ligne
        global affichage
        hauteur = hauteur - 1  # la sélection doit descendre de 1 étage donc on enlève 1 à hauteur
        temp = save_max-1  # temp est identique à la fonction haut()
        if hauteur >= 1:  # la hauteur obtenue est supérieure ou égale à 1, c'est-à-dire qu'elle est comprise dans un des espaces d'affichage
            # on souligne l’espace sur lequel est positionnée la sélection
            exec(f'Resultat{hauteur-1}.config(font=font_souligne)')
            # on enlève le soulignage
            exec(f'Resultat{hauteur}.config(font=font_normal)')
            # on enlève 1 à affichage, car la distance entre la sauvegarde sélectionnée et la dernière save est réduite de 1
            affichage = affichage - 1
        else:  # si la hauteur obtenue est en dessous de 1 (elle est de 0), c'est que la sélection passe sur une sauvegarde qui n'est pas affichée dans les espaces donc on monde l'affichage
            try:  # on essaie de :
                ligne = ligne - 1  # supprimer une ligne pour monter les sauvegardes
                for i in range(8):
                    # configurer chaque espace pour qu'il reçoive les bonnes valeurs des sauvegardes.
                    exec(f'Resultat{i}.config(text = save{temp-2*ligne-i})')
                # on souligne l'espace sur lequel se trouve la sélection et on enlève le soulignage le précédent
                Resultat1.config(font=font_souligne)
                Resultat0.config(font=font_normal)
                # la hauteur passe de 0 à 2, car la sélection passe sur l'espace numéro 2.
                hauteur = 2
                # on enlève 1 à affichage parce que la distance entre la sauvegarde sélectionnée et la dernière save est réduite de 1
                affichage = affichage - 1
            except:  # si ça provoque une erreur, c'est que la sélection veut descendre plus bas qu'il n'y a de sauvegarde. La dernière sauvegarde est déjà affichée sur l'espace le plus bas
                # on bloque donc la hauteur sur le premier espace et on supprime toutes les lignes.
                hauteur = 1
                ligne = 0
        # dans tous les cas en fin de fonction, Rep prend la valeur de la sauvegarde sur laquelle est positionnée la sélection
        exec(f'global Rep\nRep = save{temp-affichage+1}')
    if var_python == 1:  # on fait exactement pareil à la fonction haut
        position = Python.index('insert')
        pos = position.find('.')
        line = int(position[:pos])
        column = int(position[pos+1:len(position)])
        # seule cette ligne change. On ajoute 1 à ligne pour que le curseur d’insertion aille sur la ligne du dessous
        Python.mark_set('insert', "%d.%d" % (line+1, column))


# Fonction droite():
# version calcul : permet de déplacer le curseur d’insertion de 1 cran vers la droite dans l'espace ou l'utilisateur entre les calculs
# version python : permet de déplacer le curseur d’insertion de 1 cran vers la droite dans l'espace ou l'utilisateur entre le code python
def droite():
    if var_calcul == 1:  # mode calcul activé
        # on prend la position du curseur d’insertion et on lui ajoute 1 pour qu'il se déplace de 1 vers la droite.
        position = Entree_operation.index('insert')+1
        Entree_operation.icursor(position)  # déplace le curseur d’insertion
    if var_python == 1:  # mode python activé
        # même principe que pour la fonction haut() en mode python, mais on ajoute 1 à column pour que le curseur d’insertion se déplace de 1 vers la droite.
        position = Python.index('insert')
        pos = position.find('.')
        line = int(position[:pos])
        column = int(position[pos+1:len(position)])
        Python.mark_set('insert', "%d.%d" % (line, column+1))


# Fonction gauche():
# version calcul : permet de déplacer le curseur d’insertion de 1 cran vers la gauche dans l'espace ou l'utilisateur entre les calculs
# version python : permet de déplacer le curseur d’insertion de 1 cran vers la gauche dans l'espace ou l'utilisateur entre le code python
def gauche():
    if var_calcul == 1:  # mode calcul activé
        # même principe que pour la fonction droite() en mode calcul, mais on enlève 1 au lieu d'ajouter pour que le curseur d’insertion se déplace de 1 vers la gauche
        position = Entree_operation.index('insert')-1
        Entree_operation.icursor(position)
    if var_python == 1:  # mode python activé
        # même principe que pour la fonction haut() en mode python, mais on enlève 1 à column pour que le curseur d’insertion se déplace de 1 vers la gauche
        position = Python.index('insert')
        pos = position.find('.')
        line = int(position[:pos])
        column = int(position[pos+1:len(position)])
        Python.mark_set('insert', "%d.%d" % (line, column-1))


# Fonction executer():
# fonction python qui permet de récupérer le code entré par l'utilisateur, de l’exécuter et de remplir une zone de texte avec le résultat
def executer():
    try:  # on essaye
        Python.forget()  # on cache le code
        # on active la console (on peut maintenant entrer du texte à l’intérieur)
        Console.config(state='normal')
        # on affiche la console (pour l'instant, elle est vide)
        Console.pack(expand="true", fill="both")
        # seule commande du programme qui utilise la bibliothèque subprocess et sys
        resultat = subprocess.run(
            [sys.executable, "-c", Python.get("1.0", "end")], capture_output=True, text=True)
        # on met dans la variable résultat de l'exécution des caractères présent dans l'espace python.
        # sys.executable: argument qui donne le chemin d’accès vers l'exécutable python qui va être utilisé pour exécuter le code.
        # -c: argument qui signifie que le code à exécuter sera sous forme de texte.
        # Python.get("1.0","end") : argument qui donne la chaîne de caractère qui va être exécutée sous forme de code
        # capture_output=True: argument qui demande d'enregistrer le résultat de l'exécution. exemple : print('Bonjour'), le résultat va être 'Bonjour'
        # text=True: argument qui demande à Python de décoder les octets qui sont retournés en chaînes de caractère.
        # résultat va contenir alors plusieurs informations et pour extraire celles qui nous intéresse on utilise résultat.stdout pour le résultat si le code s'est exécuté correctement et resultat.stdout s'il y a eu une erreur
        # on supprime le contenu de la console. Elle peut être remplie si un code avait été exécuté précédemment
        Console.delete('1.0', 'end')
        # on remplit console par le résultat si s'est correctement exécute et par l'erreur s'il y en a une sinon resultat.stderr sera vide.
        Console.insert('1.0', resultat.stdout+resultat.stderr)
        # on désactive la fenêtre pour que l'utilisateur ne puisse pas en modifier le contenu
        Console.config(state='disabled')
    except:  # si cela a provoqué une erreur
        # on fait la même chose, mais avec une autre commande qui ne retourne pas de résultat dans la console.
        exec(Python.get("1.0", "end"))


# Fonction annulation
# Uniquement en mode calcul.(désactivée en mode python):permet de retourner dans l'interface python pour modifier le code
def annulation():
    Console.forget()  # cache la console python
    # affiche l'interface python pour modifier le code
    Python.pack(expand="true", fill="both")


# Fonction reset
# Uniquement en mode calcul.(désactivée en mode python): supprime les caractères insérés par l'utilisateur
def reset():
    # supprime tous les caractères compris entre le caractère de rang 0 et la fin (tous les caractères)
    Entree_operation.delete(0, "end")


# Fonction ecriture():
# permet de supprimer le caractère précédant le curseur d’insertion dans les 2 modes
def effacer():
    if var_calcul == 1:
        # position du curseur d’insertion
        position = Entree_operation.index('insert')
        # on supprime le caractère précédant
        Entree_operation.delete(position-1, position)
    if var_python == 1:
        # idem que pour la fonction haut() pour séparer les 2 valeurs.
        position = Python.index('insert')
        pos = position.find('.')
        line = int(position[:pos])
        column = int(position[pos+1:len(position)])
        if column == 0:  # si on arrive il n'y a plus de caractères sur la ligne :
            # on passe à la fin de la ligne du dessus
            Python.delete(f'{line-1}.end', 'insert')
        else:  # sinon
            # on supprime le caractère précédant le curseur d’insertion.
            Python.delete("%d.%d" % (line, column-1), 'insert')


# Fonction ecriture():
# permet de changer l’écriture du dernier résultat affiché dans calcul.(décimal en fraction et l'inverse) ne fonctionne que pour les nombres rationnels
def ecriture():
    if save_max == 0:
        return
    else:
        global var_ecriture  # appelle la variable var_ecriture
        if var_ecriture == 0:  # si elle est sur 0 ( désactivée)
            var_ecriture = 1  # on la met sur 1 pour l'activer
            # on change le résultat affiché grâce à la fonction Fraction() qui transforme : 4.5 en 9/2 par exemple et on le met dans la sauvegarde qui a été modifiée
            exec(
                f'global save{save_max-1}\nsave{save_max-1}=str(Fraction(save{save_max-1}))')
            # s'il n'y a pas de modification de hauteur (pas de ligne ajoutée) c'est que la dernière sauvegarde est visible par l'utilisateur.
            if ligne == 0:
                # on lui modifie donc l'affichage
                exec(f'Resultat0.config(text=save{save_max-1})')
        else:  # si elle est déjà activée
            var_ecriture = 0  # on la désactive
            # on configure le résultat affiché pour qu'il soit sous sa forme initiale (forme décimale) save_max -2 étant la sauvegarde qui contient le calcul qui a donné la dernière sauvegarde.
            exec(
                f'global save{save_max-1}\nsave{save_max-1}=str(eval(formatage(save{save_max-2})))')
            # s'il n'y a pas de modification de hauteur (pas de ligne ajoutée) c'est que la dernière sauvegarde est visible par l'utilisateur.
            if ligne == 0:
                # on lui modifie donc l'affichage
                exec(f'Resultat0.config(text=save{save_max-1})')


# Fonction operation():
# insert le caractère x dans la chaîne de caractère à l'emplacement du curseur d’insertion
def operation(x):
    if var_calcul == 1:
        # dans Entree_operation pour calcul
        Entree_operation.insert(Entree_operation.index('insert'), x)
    if var_python == 1:
        Python.insert(Python.index('insert'), x)  # dans Python pour python


# Les fonctions d'activation de modes et options


# Fonction mode_calcul():
# active et désactive le mode calcul
# permet de passer du mode python au mode calcul
def mode_calcul():
    global var_calcul
    global var_python
    var_calcul = 1  # active le mode calcul
    var_python = 0  # désactive le mode python
    # button1 correspond au nom du button qui exécute la fonction  mode_calcul()
    # button2 correspond au nom du button qui exécute la fonction mode_python()
    # désactive le bouton calcul pour ne plus que l'utilisateur puisse appuyer dessus vu que le mode calcul est déjà activé
    button1.config(stat="disable")
    # active le bouton python pour que l'utilisateur puisse rebasculer sur le mode python s'il le désire
    button2.config(stat="normal")
    config_affichage()  # configure l'affiche des fenêtres en fonction des nouvelles données
    config_button()  # configure l'affiche des boutons en fonction des nouvelles données


# Fonction mode_python():
# active et désactive le mode python
# permet de passer du mode calcul au mode python
def mode_python():
    global var_calcul
    global var_python
    var_calcul = 0  # désactive le mode calcul
    var_python = 1  # active le mode python
    # button1 correspond au nom du button qui exécute la fonction  mode_calcul()
    # button2 correspond au nom du button qui exécute la fonction mode_python()
    # active le bouton calcul pour que l'utilisateur puisse rebasculer sur le mode calcul s'il le désire
    button1.config(stat="normal")
    # désactive le bouton python pour que l'utilisateur ne puisse plus appuyer dessus vu que le mode python est déjà activé
    button2.config(stat="disable")
    config_affichage()  # configure l'affiche des fenêtres en fonction des nouvelles données
    config_button()  # configure l'affiche des boutons en fonction des nouvelles données


# Fonction mode_seconde():
# active et désactive l'option seconde
def mode_seconde():
    global var_alpha
    global var_seconde
    if var_seconde == 0:  # si var_seconde est déactivé
        var_seconde = 1  # on l'active
        button0.config(bg='blue')  # on configure le bouton sur bleu
        # button0 correspond au nom du button qui exécute la fonction mode_seconde()
    else:  # sinon
        var_seconde = 0  # on le désactive
        # on configure le bouton sur la couleur de base
        button0.config(bg='#F0F0F0')
    config_button()  # configure l'affiche des boutons en fonction des nouvelles données


# Fonction mode_alpha():
# active et désactive l'option alpha
def mode_alpha():  # fonctionne de la même manière que la fonction mode_seconde()
    global var_alpha
    global var_seconde
    if var_alpha == 0:
        button5.config(bg='green')
        var_alpha = 1
    else:
        button5.config(bg="#F0F0F0")
        var_alpha = 0
    config_button()

# Affichage et mise en forme

# Fonction config_button():
# reconfigure chaque bouton en fonction des modes et option activés.
# on répète le processus pour chaque possibilité de combinaison d'option et de mode


def config_button():
    if var_calcul == 1:  # si le mode calcul est activé
        if var_seconde == 0 and var_alpha == 0:  # il n’y a pas d'option d'activé
            # dans l'affichage il y a 5 boutons par ligne et 8 lignes donc 8×5=40 boutons
            for i in range(8):
                for j in range(5):
                    # p = le numéro du bouton en fonction de sa ligne et de son rang sur la ligne
                    p = (5*i)+j
                    # on configure cette configuration pour les touches de base (sans option)
                    exec(f'button{p}.config(text="{touches[p]}",fg="black")')
                    # suit la liste des numéros des boutons qui vont être modifiés et dont le nom va changer par celui présent dans la liste touches[p]
                    if p == 10 or p == 11 or p == 12 or p == 13 or p == 15 or p == 16 or p == 17 or p == 18 or p == 19 or p == 20 or p == 21 or p == 22 or p == 23 or p == 25 or p == 26 or p == 27 or p == 28 or p == 30 or p == 31 or p == 32 or p == 33 or p == 35 or p == 36 or p == 37:
                        # on va chercher dans la liste le caractère qui correspond à la place du bouton dans la liste et on affecte comme commande le fait que lors de l'appui (lambda:) on déclenche la fonction opération() avec argument la touche correspondante à la place p dans la liste.
                        exec(
                            f'button{p}.config(command=lambda: operation(str(touches[{p}])))')
                    # on configure les boutons qui vont être désactivé et activé pour cette configuration
                    if p == 14:
                        button14.config(state='normal', command=lambda: ecriture())
                    if p == 29:
                        button29.config(state='disabled')
                    if p == 34:
                        button34.config(state='normal')
                    if p == 37:
                        button37.config(state='normal')
                    if p == 38:
                        button38.config(state='disabled')

        if var_seconde == 1 and var_alpha == 0:
            for i in range(8):
                for j in range(5):
                    p = (5*i)+j
                    if p == 33:
                        button33.config(text='◡', fg="blue",
                                        command=lambda: operation(' '))
                    if p == 36:
                        button36.config(text='\\', fg="blue",
                                        command=lambda: operation('\\'))
                    if p == 23:
                        button23.config(fg="blue", text='"',
                                        command=lambda: operation('"'))
                    if p == 38:
                        button38.config(
                            fg="blue", text=touches_mode_seconde[38], command=lambda: operation('    '))
                    if p == 10 or p == 11 or p == 12 or p == 13 or p == 14 or p == 15 or p == 16 or p == 17 or p == 18 or p == 19 or p == 20 or p == 21 or p == 22 or p == 25 or p == 26 or p == 27 or p == 28 or p == 30 or p == 31 or p == 32 or p == 35 or p == 37:
                        exec(
                            f'button{p}.config(text="{touches_mode_seconde[p]}")')
                        exec(
                            f'button{p}.config(fg="blue",command=lambda: operation(str(touches_mode_seconde[{p}])))')
                    if p == 14:
                        button14.config(state='normal')
                    if p == 29:
                        button29.config(state='disabled')
                    if p == 34:
                        button34.config(state='normal')
                    if p == 37:
                        button37.config(state='normal')
                    if p == 38:
                        button38.config(state='normal')

        if var_seconde == 0 and var_alpha == 1:
            for i in range(8):
                for j in range(5):
                    p = (5*i)+j
                    exec(f'button{p}.config(text="{touches_mode_alpha[p]}")')
                    if p == 10 or p == 11 or p == 12 or p == 13 or p == 14 or p == 15 or p == 16 or p == 17 or p == 18 or p == 19 or p == 20 or p == 21 or p == 22 or p == 23 or p == 25 or p == 26 or p == 27 or p == 28 or p == 30 or p == 31 or p == 32 or p == 33 or p == 35 or p == 36 or p == 37 or p == 38:
                        exec(
                            f'button{p}.config(fg="green",command=lambda: operation(str(touches_mode_alpha[{p}])))')
                    if p == 14:
                        button14.config(state='normal')
                    if p == 29:
                        button29.config(state='disabled')
                    if p == 34:
                        button34.config(state='normal')
                    if p == 37:
                        button37.config(state='normal')
                    if p == 38:
                        button38.config(state='normal')

        if var_seconde == 1 and var_alpha == 1:
            for i in range(8):
                for j in range(5):
                    p = (5*i)+j
                    exec(
                        f'button{p}.config(text="{touches_seconde_alpha[p]}")')
                    if p == 10 or p == 11 or p == 12 or p == 13 or p == 14 or p == 15 or p == 16 or p == 17 or p == 18 or p == 19 or p == 20 or p == 21 or p == 22 or p == 23 or p == 25 or p == 26 or p == 27 or p == 28 or p == 30 or p == 31 or p == 32 or p == 33 or p == 35 or p == 36 or p == 37 or p == 38:
                        exec(
                            f'button{p}.config(fg="green",command=lambda: operation(str(touches_seconde_alpha[{p}])))')
                    if p == 14:
                        button14.config(state='normal')
                    if p == 29:
                        button29.config(state='disabled')
                    if p == 34:
                        button34.config(state='normal')
                    if p == 37:
                        button37.config(state='normal')
                    if p == 38:
                        button38.config(state='normal')

    if var_python == 1:

        if var_seconde == 0 and var_alpha == 0:
            for i in range(8):
                for j in range(5):
                    p = (5*i)+j
                    exec(
                        f'button{p}.config(text="{touches_python[p]}",fg="black")')
                    if p == 10 or p == 11 or p == 12 or p == 13 or p == 15 or p == 16 or p == 17 or p == 18 or p == 19 or p == 20 or p == 21 or p == 22 or p == 23 or p == 25 or p == 26 or p == 27 or p == 28 or p == 30 or p == 31 or p == 32 or p == 33 or p == 35 or p == 36 or p == 37:
                        exec(
                            f'button{p}.config(command=lambda: operation(str(touches_python[{p}])))')
                    if p == 14:
                        button14.config(state='disabled')
                    if p == 29:
                        button29.config(state='normal')
                    if p == 34:
                        button34.config(state='disabled')
                    if p == 37:
                        button37.config(state='disabled')
                    if p == 38:
                        button38.config(
                            state='normal', command=lambda: executer())

        if var_seconde == 1 and var_alpha == 0:
            for i in range(8):
                for j in range(5):
                    p = (5*i)+j
                    if p == 33:
                        button33.config(text='◡', fg="blue",
                                        command=lambda: operation(' '))
                    if p == 36:
                        button36.config(text='\\', fg="blue",
                                        command=lambda: operation('\\'))
                    if p == 23:
                        button23.config(fg="blue", text='"',
                                        command=lambda: operation('"'))
                    if p == 38:
                        button38.config(
                            fg="blue", text=touches_mode_seconde_python[38], command=lambda: operation('    '))
                    if p == 10 or p == 11 or p == 12 or p == 13 or p == 14 or p == 15 or p == 16 or p == 17 or p == 18 or p == 19 or p == 20 or p == 21 or p == 22 or p == 25 or p == 26 or p == 27 or p == 28 or p == 30 or p == 31 or p == 32 or p == 35 or p == 37:
                        exec(
                            f'button{p}.config(text="{touches_mode_seconde_python[p]}")')
                        exec(
                            f'button{p}.config(fg="blue",command=lambda: operation(str(touches_mode_seconde_python[{p}])))')
                    if p == 14:
                        button14.config(state='normal')
                    if p == 29:
                        button29.config(state='normal')
                    if p == 34:
                        button34.config(state='disabled')
                    if p == 37:
                        button37.config(state='normal')
                    if p == 38:
                        button38.config(state='normal')

        if var_seconde == 0 and var_alpha == 1:
            for i in range(8):
                for j in range(5):
                    p = (5*i)+j
                    exec(f'button{p}.config(text="{touches_mode_alpha[p]}")')
                    if p == 10 or p == 11 or p == 12 or p == 13 or p == 14 or p == 15 or p == 16 or p == 17 or p == 18 or p == 19 or p == 20 or p == 21 or p == 22 or p == 23 or p == 25 or p == 26 or p == 27 or p == 28 or p == 30 or p == 31 or p == 32 or p == 33 or p == 35 or p == 36 or p == 37 or p == 38:
                        exec(
                            f'button{p}.config(fg="green",command=lambda: operation(str(touches_mode_alpha[{p}])))')
                    if p == 14:
                        button14.config(state='normal')
                    if p == 29:
                        button29.config(state='normal')
                    if p == 34:
                        button34.config(state='disabled')
                    if p == 37:
                        button37.config(state='normal')
                    if p == 38:
                        button38.config(state='normal')

        if var_seconde == 1 and var_alpha == 1:
            for i in range(8):
                for j in range(5):
                    p = (5*i)+j
                    exec(
                        f'button{p}.config(text="{touches_seconde_alpha[p]}")')
                    if p == 10 or p == 11 or p == 12 or p == 13 or p == 14 or p == 15 or p == 16 or p == 17 or p == 18 or p == 19 or p == 20 or p == 21 or p == 22 or p == 23 or p == 25 or p == 26 or p == 27 or p == 28 or p == 30 or p == 31 or p == 32 or p == 33 or p == 35 or p == 36 or p == 37 or p == 38:
                        exec(
                            f'button{p}.config(fg="green",command=lambda: operation(str(touches_seconde_alpha[{p}])))')
                    if p == 14:
                        button14.config(state='normal')
                    if p == 29:
                        button29.config(state='normal')
                    if p == 34:
                        button34.config(state='disabled')
                    if p == 37:
                        button37.config(state='normal')
                    if p == 38:
                        button38.config(state='normal')


# Fonction config_affichage():
# permet de configurer l'affichage des fenêtres en fonction du mode
def config_affichage():
    if var_calcul == 1:  # si le mode calcul est activé
        Console.forget()  # on cache la console
        Python.forget()  # on cache la zone de saisie du code python
        for i in range(7, -1, -1):
            # on fait apparaître chaque espace de texte pour le mode calcul. On configure les espaces de texte dans le bon sens pour que l'espace Resultat0 soit le plus bas des 8
            exec(f'Resultat{i}.pack(expand = "true",fill = "both")')
        # on affiche la zone de saisie pour les opérations du mode calcul
        Entree_operation.pack(expand="true", fill="both")
        Entree_operation.focus()  # on met le curseur d’insertion dans la zone d’écriture
    if var_python == 1:  # on fait l'inverse lorsque le mode python est activé
        for i in range(7, -1, -1):
            exec(f'Resultat{i}.forget()')
        Entree_operation.forget()
        Python.pack(expand="true", fill="both")
        Python.focus()


# on appelle la fonction config_button() pour configurer ce que fait chaque bouton sauf ceux configurés au début
config_button()

# ces 3 commandes écoute le clavier quand le curseur d'injection est dans le widget Entree_operation
# si la touche entrée est pressée alors, on déclenche la fonction egal
Entree_operation.bind("<Return>", egal)
# si la touche flèche vers le haut est pressée, on déclenche la fonction haut()
Entree_operation.bind("<Up>", haut)
# si la touche flèche vers le bas est pressée, on déclenche la fonction bas()
Entree_operation.bind("<Down>", bas)
Calculatrice.mainloop()