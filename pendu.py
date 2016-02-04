import os

# On demande à l'utilisateur un mot
motADeviner = str(input("Veuillez saisir le mot qui devra être deviné par le joueur :"))
longueurMot = len(motADeviner)
victoire = True
lettresDejaSaisies = list()

# On s'assure que le mot fait au moins 4 caractères
if longueurMot < 4:
    print("Attention, le mot que vous avez entré est trop cout. La longueur minimale est de 4 caractères")
else:
    os.system('cls' if os.name == 'nt' else 'clear')

    premiereLettre = motADeviner[0]
    derniereLettre = motADeviner[longueurMot - 1]

    # Etant donné que la première et la dernière lettre du mot vont être
    # directement lisible la taille du mot à deviner est réduite
    restantATrouver = longueurMot - 2

    # Création du masque par concaténation
    motEnCours = premiereLettre

    for i in range(1, longueurMot - 1):
        motEnCours += '-'
    motEnCours += derniereLettre

    mauvaiseReponse = 0
    nombreDeChances = 5
    while restantATrouver != 0 and mauvaiseReponse < nombreDeChances:
        lettrePropose = input("Proposez une lettre : " + motEnCours + "\n")

        if lettresDejaSaisies.count(lettrePropose) > 0:
            print("Vous avez déjà saisi les lettres suivantes : " + str(lettresDejaSaisies))
        else:
            lettresDejaSaisies.append(lettrePropose)

            lettreTrouvee = 0
            Trouve = False

            # On cherche la lettrePropose dans le mot
            for j in range(1, longueurMot - 1):
                if motADeviner[j] == lettrePropose:
                    print("Bravo, vous avez trouvé une lettre ! \n")
                    lettreTrouvee += 1
                    restantATrouver -= 1
                    motEnCours = motEnCours[:j] + lettrePropose + motEnCours[j + 1:]
                    Trouve = True

            if not Trouve:
                mauvaiseReponse += 1
                chancesRestantes = nombreDeChances - mauvaiseReponse

                if chancesRestantes > 0:
                    print("Ah, non! Attention il ne vous reste plus que " + str(chancesRestantes) + " chances!\n")
                else:
                    print("Vous avez perdu")
                    victoire = False

    if victoire:
        print("Bravo, vous avez trouvé le mot ! Le mot était \"" + motADeviner + "\"")

input("Veuillez taper sur une touche pour quitter.")