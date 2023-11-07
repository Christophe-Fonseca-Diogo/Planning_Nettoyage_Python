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


def validate_week(date):
    query = "SELECT id FROM classes_clean_students WHERE start_date = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (date,))
    rows = cursor.fetchall()
    cursor.close()
    return rows


def planning_checker(class_id):
    query = "SELECT done FROM classes_clean_students WHERE start_date = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (class_id))
    rows = cursor.fetchall()
    cursor.close()
    return rows


def validate_cleaning(classe_id, student_id, start_date, end_date):
    try:
        cursor = db_connection.cursor()
        query = "UPDATE classes_clean_students SET done = 1 WHERE class_id = %s AND start_date <= %s AND end_date >= %s AND student_id = %s"
        data_cleaning = (classe_id, start_date, end_date, student_id)
        cursor.execute(query, data_cleaning)
        affected_rows = cursor.rowcount
        cursor.close()
        if affected_rows == 1:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print("Erreur SQL : ", err)
        return False


