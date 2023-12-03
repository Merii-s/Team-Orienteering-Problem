import matplotlib.pyplot as plt
import test_instances as ti
from pathlib import Path  # Pour manipuler les chemins de fichiers
from glob import glob  # Pour rechercher des fichiers


def main():
    Chao_directory = "TestInstances\Chao"  
    Tsiligirides_directory = "TestInstances\Tsiligirides"  

    Tsiligirides = ti.read_test_sets(Tsiligirides_directory)
    Chao = ti.read_test_sets(Chao_directory)

    # Print the contents of the dictionary for verification
    print("Tsiligirides :\n")
    for test_set, instances in Tsiligirides.items():
        print(f"Test Set: {test_set}")
        for instance in instances:
            print(instance)
    print("Chao :\n")
    for test_set, instances in Chao.items():
        print(f"Test Set: {test_set}")
        for instance in instances:
            print(instance)


if __name__ == "__main__":
    main()