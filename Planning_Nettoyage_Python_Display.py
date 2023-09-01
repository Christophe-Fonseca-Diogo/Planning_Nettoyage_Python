# Projet Planning Nettoyage Python Display
# Made by Christophe Fonseca Diogo
# 01.09.2023

banner = ("Merci de choisir une option : \n\n"
          "1. Afficher l’ordre en classe\n"
          "2. Générer le planning « Ordre en classe »\n"
          "3. Valider l’ordre en classe de la semaine\n"
          "4. Supprimer un élève de la liste\n"
          "5. Ajouter un élève de la liste\n"
          "6. Générer le document « Ordre en classe »\n"
          "7. Sortir du menu\n")

print(banner)

while True:
    try:
        choice = int(input("Votre option : \n"))
        if choice < 1 or choice > 7:
            print("Choix inexistant merci de rentrer un bon choix ci-dessous \n")
            print(banner)
        else:
            print("Merci de votre choix mais ce n'est pas encore prêt")
            break
        if choice == 7:
            print("Vous avez quitter le programme\n")
            exit()
    except ValueError:
        print("Merci de rentrer un nombre de la liste \n")
        print(banner)