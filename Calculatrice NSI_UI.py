from nsi_ui import *


touches = ["0", "1", "2", "3", "4", "5", "6",
           "7", "8", "9", "/", "*", "+", "-", 'C', '=']
a = ""


def calcul(x):       # Créée une chaine de caractères avec a comme variable vide (...)
    # (...) initialement et ensuite incrémenté de x, soit la touche saisie.
    global a
    a = a + x
    set_text(l, a)
    if "/0" in a:                       # Affiche "Erreur" en cas de division par zero
        a = "Erreur !!! Division par 0"
        set_text(l, a)
        a = ""


def egal():
    global a
    a = str(eval(a))    		# Eval() change les str en operations
    set_text(l, a)


def reset():              # Cette fonction supprime le contenu de la variable a
    global a
    a = ""
    set_text(l, a)


def calcul_operation(x):  # Effectue le calculen transformantstr en operations avec eval()
    global a
    a = str(eval(a))+x
    set_text(l, a)


begin_vertical()
begin_horizontal()
end_horizontal()
begin_horizontal()
l = label(a)
end_horizontal()
begin_horizontal()
b = button(f'{touches[7]:1}', calcul, touches[7])
b = button(f'{touches[8]:1}', calcul, touches[8])
b = button(f'{touches[9]:1}', calcul, touches[9])
b = button(f'{touches[10]:1}', calcul_operation, touches[10])
end_horizontal()
begin_horizontal()
b = button(f'{touches[4]:1}', calcul, touches[4])
b = button(f'{touches[5]:1}', calcul, touches[5])
b = button(f'{touches[6]:1}', calcul, touches[6])
b = button(f'{touches[11]:1}', calcul_operation, touches[11])
end_horizontal()
begin_horizontal()
b = button(f'{touches[1]:1}', calcul, touches[1])
b = button(f'{touches[2]:1}', calcul, touches[2])
b = button(f'{touches[3]:1}', calcul, touches[3])
b = button(f'{touches[12]:1}', calcul_operation, touches[12])
end_horizontal()
begin_horizontal()
b = button(f'{touches[14]:1}', reset)
b = button(f'{touches[0]:1}', calcul, touches[0])
b = button(f'{touches[15]:1}', egal)
b = button(f'{touches[13]:1}', calcul_operation, touches[13])

main_loop()
