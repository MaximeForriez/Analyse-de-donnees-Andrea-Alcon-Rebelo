#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)
# Question 5
data = pd.DataFrame(contenu)
print(data)
#Question 6
nb_lignes = len(data)
print (nb_lignes)
nb_colonnes = len(data.columns)
print(nb_colonnes)
#Question 7 
print (data.dtypes)
#Question 8
print (data.head ())
# ou : 
print (data.columns)
#Question 9 
colonne_a_afficher = data.columns[2]
print (data[colonne_a_afficher].head())

#Question 10
print (data.sum())
effectifs = data.sum()
liste_effectifs = []

for valeur in effectifs:
    liste_effectifs.append(valeur)

print(liste_effectifs)






# Mettre dans un commentaire le numéro de la question
# Question 1
# ...
