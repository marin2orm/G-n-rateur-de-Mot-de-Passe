import random
import tkinter as tk
import pyperclip

# Fonction pour générer le mot de passe
def generer_mot_de_passe():
    NombreCar = int(entry_caracteres.get())
    niveauComp = int(entry_niveau.get())

    listeCarComp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    listeCarMid= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    listeLow= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    motDePasse = ""
    for i in range(NombreCar):
        if niveauComp not in [1, 2, 3]:
            result_label.config(text="Niveau de complexité invalide")
            break
        else:
            if niveauComp == 1:
                nombreAleatoire = random.randint(0, 51)
                nombreActuelle = listeLow[nombreAleatoire]
                motDePasse += nombreActuelle
            elif niveauComp == 2:
                nombreAleatoire = random.randint(0, 61)
                nombreActuelle = listeCarMid[nombreAleatoire]
                motDePasse += nombreActuelle
            else:
                nombreAleatoire = random.randint(0, 91)
                nombreActuelle = listeCarComp[nombreAleatoire]
                motDePasse += nombreActuelle

    if motDePasse != "":
        result_label.config(text=f"Votre mot de passe est : {motDePasse}")

# Interface graphique
window = tk.Tk()
window.title("Générateur de mot de passe")

label_caracteres = tk.Label(window, text="Combien de caractères voulez-vous dans votre mot de passe ?")
label_caracteres.pack()
entry_caracteres = tk.Entry(window)
entry_caracteres.pack()

label_niveau = tk.Label(window, text="Quel niveau de complexité voulez-vous ? (1 pour faible, 2 pour moyen, 3 pour fort)")
label_niveau.pack()
entry_niveau = tk.Entry(window)
entry_niveau.pack()

generate_button = tk.Button(window, text="Générer", command=generer_mot_de_passe)
generate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Fonction pour copier le mot de passe
def copier_mot_de_passe():
    mot_de_passe = result_label.cget("text")
    mot_de_passe = mot_de_passe.split(": ")[1]  # Récupérer le mot de passe à partir de la chaîne
    pyperclip.copy(mot_de_passe)


copy_button = tk.Button(window, text="Copier", command=copier_mot_de_passe)
copy_button.pack()


window.mainloop()
