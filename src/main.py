import matplotlib.pyplot as plt
import test_instances as ti
from pathlib import Path  # Pour manipuler les chemins de fichiers
from glob import glob  # Pour rechercher des fichiers
import random
import utils as ut


def main():
    # Chao_directory = "TestInstances\Chao"
    # Tsiligirides_directory = "TestInstances\Tsiligirides"

    # # Appel de la fonction pour lire le fichier et stocker les données dans un DataFrame
    # nom_fichier = Chao_directory + "\Set_64_234\p6.2.a.txt" 
    # print(nom_fichier)
    # resultat = ut.read_instances(nom_fichier)

    # if resultat is not None:
    #     print(resultat.head())  # Affichage des premières lignes du DataFrame pour vérifier

    n,m,tmax,coords = ut.read_problem_instance("TestInstances\Chao\Set_64_234\p6.2.a.txt")
    print(n)
    print(m)
    print(tmax)
    print(coords)
    # print(coords['x'])
    # print(coords['y'])
    # print(coords['s'])



if __name__ == "__main__":
    main()
