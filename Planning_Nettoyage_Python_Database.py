# Projet Planning Nettoyage Python Students
# Made by Christophe Fonseca Diogo
# 01.09.2023

import csv

filename = "classes.csv"
classes = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(', '.join(row))
        classes.append(', '.join(row))

print("\n")

filename = "students.csv"
students = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        students.append(', '.join(row))
    print(students)