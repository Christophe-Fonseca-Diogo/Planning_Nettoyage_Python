# Projet Planning Nettoyage Python Display
# Made by Christophe Fonseca Diogo
# 01.09.2023
# Version 1


from Planning_Nettoyage_Python_Data import *


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
    open_dbconnection()
    try:
        choice = int(input("Votre option : \n"))
        if choice < 1 or choice > 7:
            print("Choix invalide merci de rentrer un un nombre du menu \n ")
            print(banner)
        if choice == 4:
            print("Vous avez choisi de supprimer un élève \n")
            firstname_student = input("Merci de rentrer le prénom de l'élève que vous voulez supprimer : ")
            name_student = input("Merci de rentrer le nom de l'élève que vous voulez supprimer : ")
            classe_student = input("Merci de rentrer la classe de l'élève que vous voulez supprimer : ")
            email_student = input("Merci de rentrer l'email de l'élève que vous voulez supprimer : ")
            delete_students_choice(firstname_student,name_student,email_student,classe_student)
            print(f"Vous avez bien réussi à supprimer l'élève : {firstname_student}, {name_student}, classe :{classe_student} email :,{email_student}")
            print(banner)
        if choice == 5:
            print("Vous avez choisi d'ajouter un élève \n")
            firstname_student = input("Merci de rentrer le prénom de l'élève : ")
            name_student = input("Merci de rentrer le nom de l'élève : ")
            classe_student = input("Merci de rentrer la classe de l'élève : ")
            email_student = input("Merci de rentrer l'email de l'élève : ")
            add_students_choice(firstname_student,name_student,email_student,classe_student)
            print(f"Vous avez bien réussi à ajouter l'élève : {firstname_student}, {name_student}, classe :{classe_student} email :,{email_student}")
            print(banner)
        if choice == 7:
            print("Vous avez quitter le programme\n")
            exit()
    except ValueError:
        print("Merci de rentrer un nombre de la liste \n")
        print(banner)



