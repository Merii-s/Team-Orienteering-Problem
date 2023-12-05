import matplotlib.pyplot as plt
import test_instances as ti
from pathlib import Path  # Pour manipuler les chemins de fichiers
from glob import glob  # Pour rechercher des fichiers
import random


def main():
    Chao_directory = "TestInstances\Chao"
    Tsiligirides_directory = "TestInstances\Tsiligirides"

    Tsiligirides = ti.read_test_sets(Tsiligirides_directory)
    Chao = ti.read_test_sets(Chao_directory)

    # # Print the contents of the dictionary for verification
    # print("Tsiligirides :\n")
    # for test_set, instances in Tsiligirides.items():
    #     print(f"Test Set: {test_set}")
    #     for instance in instances:
    #         print(instance)
    # print("Chao :\n")
    # for test_set, instances in Chao.items():
    #     print(f"Test Set: {test_set}")
    #     for instance in instances:
    #         print(instance)

    print(
        sum([len(Tsiligirides[i]) for i in Tsiligirides] + [len(Chao[i]) for i in Chao])
    )

    # Récupérer une clé aléatoire pour Tsiligirides
    random_key_t = random.choice(list(Tsiligirides.keys()))

    # Récupérer une clé aléatoire pour Chao
    random_key_c = random.choice(list(Chao.keys()))

    # Utiliser la clé aléatoire pour tracer les points d'une instance
    ti.plot_instance_points(random.choice(Tsiligirides[random_key_t]))
    ti.plot_instance_points(random.choice(Chao[random_key_c]))




if __name__ == "__main__":
    main()
