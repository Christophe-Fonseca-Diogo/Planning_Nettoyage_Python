# Projet Planning Nettoyage Python Data
# Made by Christophe Fonseca Diogo
# 01.09.2023

import mysql.connector
import csv

filename_classes = "classes.csv"
filename_students = "students.csv"

def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='christophe', password='Pa$$w0rd', database='classroom_cleaning',
                                   buffered=True, autocommit=True)


def add_classes(classes_name, classes_room):
    query = "INSERT INTO classes (name, room) values (%s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (classes_name, classes_room))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id

def close_dbconnection():
    db_connection.close()

open_dbconnection()
with open(filename_classes, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(";"))
    next(csvreader, None)
    for row in csvreader:
        add_classes(row[0],row[1])


print("\n")




close_dbconnection()




# Example from here :
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# or here https://www.w3schools.com/python/python_mysql_getstarted.asp













