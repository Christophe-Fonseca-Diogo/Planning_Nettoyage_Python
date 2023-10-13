# Projet Planning Nettoyage Python Display
# Made by Christophe Fonseca Diogo
# 01.09.2023
# Version 1
from Planning_Nettoyage_Python_Data import *
from Planning_Nettoyage_Python_Importation import *
import mysql.connector

class dateexception(Exception):
    pass

def generate_planning():
    print("Vous avez choisi de généré le planning \n")
    while True:
        try:
            classe_student = get_classe_id(input("Merci de rentrer la classe de l'élève : "))
            break
        except:
            print("Merci de rentrer une classe valide")
    while True:
        try:
            students_id = get_students_id(classe_student)
            break
        except:
            print("Merci de rentrer une classe valide")
    while True:
        start_date = input("Merci de rentrer la date de début du planning : ")
        try:
            start_date = datetime.datetime.strptime(start_date, '%j.%m.%Y')
            if start_date.weekday() == 0:
                end_date = start_date + datetime.timedelta(days=4)
                break
            else:
                print("Ce n'est pas un lundi !")
        except:
            print("Mauvais format de date merci de faire le format : jj.mm.YYYY")

    weeks = {}
    nb_weeks = int(input("Générer pour combien de semaines ? : "))

    while nb_weeks != 0:
        weeks[start_date] = end_date
        start_date += datetime.timedelta(days=7)
        end_date += datetime.timedelta(days=7)
        nb_weeks -= 1

    if classe_student == None or start_date == '' or end_date == '':
        print("Il manque une information !")

    else:
        planing_generator(classe_student, students_id, weeks)
        print(f"Vous avez généré le planning !\n")

        close_dbconnection()


def validation_planning(start_date, end_date):
    while True:
        date_user = input("Merci de mettre la date du jour : ")
        try:
            date_user = datetime.datetime.strptime(start_date, '%j.%m.%Y')
            if end_date >= date_user >= start_date:
                break
        except:
            print("Merci de rentrer une date valide !")
        else:
            print(date_user)



def ask_infos_add():
    
    print("Vous avez choisi d'ajouter un élève \n")
    firstname_student = input("Merci de rentrer le prénom de l'élève : ")
    name_student = input("Merci de rentrer le nom de l'élève : ")
    while True:
        try:
            classe_student = get_classe_id(input("Merci de rentrer la classe de l'élève : "))
            break
        except:
            print("Merci de rentrer une classe valide")
    email_student = input("Merci de rentrer l'email de l'élève : ")

    if firstname_student == "" or name_student == "" or email_student == "" or classe_student == "":
        print("Il manque une information !")

    else:
        add_students_choice(firstname_student, name_student, email_student, classe_student)
        print(
            f"Vous avez bien réussi à ajouter l'élève : {firstname_student}, {name_student}, classe :{classe_student} email :,{email_student}")

    close_dbconnection()

def ask_infos_delete():
    
    print("Vous avez choisi de supprimer un élève \n")
    firstname_student = input("Merci de rentrer le prénom de l'élève que vous voulez supprimer : ")
    name_student = input("Merci de rentrer le nom de l'élève que vous voulez supprimer : ")
    while True:
        try :
            classe_student = input("Merci de rentrer la classe de l'élève : ")
            break
        except:
            print("Merci de rentrer une classe valide")
    email_student = input("Merci de rentrer l'email de l'élève que vous voulez supprimer : ")
    if firstname_student == '' or name_student == '' or email_student == '' or classe_student == '':
        print("Il manque une information !")
    else:
        delete_students_choice(firstname_student, name_student, email_student, classe_student)
        print(
            f"Vous avez bien réussi à supprimer l'élève : {firstname_student}, {name_student}, classe :{classe_student} email :,{email_student}")

    close_dbconnection()


banner = ("Merci de choisir une option : \n\n"
          "1. Afficher l’ordre en classe\n"
          "2. Générer le planning « Ordre en classe »\n"
          "3. Valider l’ordre en classe de la semaine\n"
          "4. Supprimer un élève de la liste\n"
          "5. Ajouter un élève de la liste\n"
          "6. Générer le document « Ordre en classe »\n"
          "7. Sortir du menu\n")

while True:
    try:
        open_dbconnection()
        print(banner)
        choice = int(input("Votre option : \n"))
        if choice < 1 or choice > 7:
            print("Choix invalide merci de rentrer un un nombre du menu \n ")
    
        if choice == 2:
            delete_data_planning()
            generate_planning()
        if choice == 4:
            ask_infos_delete()
        if choice == 5:
            ask_infos_add()
        if choice == 7:
            print("Vous avez quitté le programme\n")
            exit()
    except ValueError:
        print("Merci de rentrer un nombre de la liste \n")
