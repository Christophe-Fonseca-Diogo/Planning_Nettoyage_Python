# Projet Planning Nettoyage Python Importation
# Made by Christophe Fonseca Diogo
# 01.09.2023
# Version 1

import mysql.connector
import csv

filename_classes = "classes.csv"
filename_students = "students.csv"


def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='christophe', password='Pa$$w0rd', database='classroom_cleaning',
                                   buffered=True, autocommit=True)
    return db_connection

def close_dbconnection():
    db_connection.close()


def add_classes(classes_name, classes_room):
    query = "INSERT INTO classes (name, room) values (%s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (classes_name, classes_room))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id


def get_classe_id(classe_name):
    query = "SELECT id FROM classes WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (classe_name,))
    row = cursor.fetchone()
    cursor.close()
    return row[0]

def add_student(firstname, lastname, student_email,class_id):
    query = "INSERT INTO students (firstname, lastname, email, class_id) values (%s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (firstname, lastname, student_email, class_id))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id

def delete_data():
    query = "SET FOREIGN_KEY_CHECKS = 0"
    query2 = "TRUNCATE table classes"
    query3 = "TRUNCATE table students"
    query4 = "SET FOREIGN_KEY_CHECKS = 1"

    cursor = db_connection.cursor()
    cursor.execute(query)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.close()

def open_classes_fromcsv():
    with open(filename_classes, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=(";"))
        next(csvreader, None)
        for row in csvreader:
            add_classes(row[0],row[1])

def open_students_fromcsv():
    with open(filename_students, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=(";"))
        next(csvreader, None)
        for row in csvreader:
            classes_id = get_classe_id(row[3])
            if classes_id == None:
                print("Il manque une valeur dans le document")
            if len(row) != 4:
                print("il manque une colonne dans le document")
            try:
                add_student(row[0],row[1],row[2],classes_id)
            except Exception as exc:
                print(exc)



open_dbconnection()
delete_data()
close_dbconnection()

open_dbconnection()
open_classes_fromcsv()
close_dbconnection()


open_dbconnection()
open_students_fromcsv()
close_dbconnection()