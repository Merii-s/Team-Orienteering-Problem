import matplotlib.pyplot as plt
import test_instances as ti
import numpy as np
from pathlib import Path  # Pour manipuler les chemins de fichiers
from glob import glob  # Pour rechercher des fichiers
import random
import utils as ut
from scipy.spatial.distance import pdist, squareform


def main():
    # Chao_directory = "TestInstances\Chao"
    # Tsiligirides_directory = "TestInstances\Tsiligirides"

    # # Appel de la fonction pour lire le fichier et stocker les données dans un DataFrame
    # nom_fichier = Chao_directory + "\Set_64_234\p6.2.a.txt" 
    # print(nom_fichier)
    # resultat = ut.read_instances(nom_fichier)

    # if resultat is not None:
    #     print(resultat.head())  # Affichage des premières lignes du DataFrame pour vérifier

    n,m,tmax,coords = ut.read_problem_instance("TestInstances/Chao/Set_64_234/p6.2.a.txt")
    start = coords.iloc[0]
    end = coords.iloc[-1]
    # print(n)
    # print(m)
    # print(tmax)
    # print(coords)
    print(start)
    print(end)
    # print(coords['x'])
    # print(coords['y'])
    # print(coords['s'])

    # Compute pairwise Euclidean distances
    distances = pdist(coords[['x', 'y']], metric='euclidean')

    # Compute time matrix
    v = 1
    time = distances / v

    # Create a square time matrix
    time_matrix = squareform(time)

    
    # Compute VRP initial savings
    savings = ut.vrp_savings(time_matrix, n)

    # Compute Clarke and Wright Savings
    alpha = ut.alpha(coords)
    top_savings = ut.top_savings(coords, savings, alpha, n)

    


if __name__ == "__main__":
    main()
