# Projet Planning Nettoyage Python Data
# Made by Christophe Fonseca Diogo
# 01.09.2023
# Version 1

from Planning_Nettoyage_Python_Importation import *
import mysql.connector
import datetime
def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='christophe', password='Pa$$w0rd', database='classroom_cleaning',
                                   buffered=True, autocommit=True)
    return db_connection

def close_dbconnection():
    db_connection.close()


open_dbconnection()
def add_students_choice(firstname, lastname, student_email, class_id):
    query = "INSERT INTO students (firstname, lastname, email, class_id) values (%s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (firstname, lastname, student_email, class_id),)
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id



def delete_students_choice(firstname, lastname, student_email, class_id):
    query = "DELETE FROM students WHERE firstname = %s AND lastname = %s AND email = %s AND class_id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (firstname, lastname, student_email, get_classe_id(class_id)))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id

def planing_generator(class_id, students_id, weeks):
    i = 0
    max = len(students_id)
    for week in weeks:
        query = "INSERT INTO classes_clean_students (class_id, student_id, start_date, end_date) values (%s, %s, %s, %s)"
        cursor = db_connection.cursor()
        cursor.execute(query, (class_id, students_id[i][0], week, weeks[week]))
        cursor.close()
        i = (i + 1) % max
