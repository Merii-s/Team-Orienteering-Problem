import pandas as pd

def test_temp():
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


def read_instances(nom_fichier):
    try:
        # Lecture du fichier texte en utilisant des espaces comme séparateurs
        dataframe = pd.read_csv(nom_fichier, sep='\s+', header=None, names=['A', 'B', 'C'])
        return dataframe
    except FileNotFoundError:
        print("Le fichier spécifié est introuvable.")
        return None


def read_problem_instance(file_path):
   #Lecture des 3 premieres lignes contenant le nombre de clients, de vehicules et le temps limite
    with open(file_path, 'r') as file:
        n = int(file.readline().split()[1]) 
        m = int(file.readline().split()[1])
        tmax = float(file.readline().split()[1])
 
    # Lecture des coordonnees et des profits de chaque sommet 
    df = pd.read_csv(file_path, delim_whitespace=True, skiprows=3, header=None, names=['y', 'x', 's'])
 
    return n,m,tmax,df


