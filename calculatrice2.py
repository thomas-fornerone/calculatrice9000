#Couleurs
#Noir : #101419
#Bleu : #273985
#Rouge : #852729
#Blanc : #FFF

from tkinter import *

expression = ""

def appuyer(touche):
    if touche == "=":
        calculer()
        return

    global expression
    expression += str(touche)
    equation.set(expression)

def calculer():
    global expression
    if "√" in expression: #Racine carré
        expression = expression.replace("√","")
        print(expression)
        expression += "**(1/2)"
    try:
        total = str(eval(expression))

        equation.set(total)
        expression = total
    except:
        equation.set("Erreur")
        expression=""

def effacer():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()

    #Couleur de fond
    gui.configure(background="#FFF")

    #Titre de l'application
    gui.title("Calculatrice9000")

    #Taille de la fenêtre
    gui.geometry("194x430")

    #Variable pour stocker le contenu actuel
    equation = StringVar()

    #Boîte de résultats
    resultat = Label(gui, bg="#FFF", fg="#101419", textvariable=equation, height="2")
    resultat.grid(columnspan=4)

    #Boutons
    boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", ".", 0, "/", "=", "√", "%"]
    ligne = 1
    colonne = 0

    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="#A2a2a2", fg="#101419", height=4, width=6)
        #Rendre le texte cliquable
        b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))

        b.grid(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1

    b = Label(gui, text="Effacer", bg="#852729", fg="#101419", height=4, width=26)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(columnspan=4)
    gui.mainloop()