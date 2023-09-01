# Projet Planning Nettoyage Python Data
# Made by Christophe Fonseca Diogo
# 01.09.2023


import csv

filename = "classes.csv"


filename = "students.csv"


with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(', '.join(row))


print("\n")

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(', '.join(row))