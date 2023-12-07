import pandas as pd
import numpy as np

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


def alpha(coords):
    scores = coords['s']
    # Taux d'évolution alpha déterminant l'homogénéité des scores de chacun des clients
    return scores.mean() - scores.std() / scores.mean()

def vrp_savings(time, n):
    savings = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            savings[i, j] = time[i,n-1] + time[0,j] - time[i, j]
    return savings

def top_savings(coords, savings, alpha, n):
    new_savings = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            new_savings[i, j] = alpha * savings[i, j] + (1 - alpha) * (coords['s'][i] + coords['s'][j])
        
    return new_savings


 
def init_solution(time, coords, n):
    # create a data frame composed by the route of each vehicle , its total travel time and its profit
    sol = pd.DataFrame(columns=['route', 'travel_time', 'profit'])
    # initialize every routes with only one client
    for i in range(1, n):
        sol.loc[i] = [[i], time[0, i] + time[i, n-1], coords['s'][i]]
    return sol

    
def selectNextArc(sorted_savings_list):
    # TODO : return the next arc with i and j
    return NotImplemented

def iRoute(solution, i):
    # TODO : return the route of the ith client
    return NotImplemented

def jRoute(solution, j):
    # TODO : return the route of the jth client
    return NotImplemented

def mergeRoutes(solution, iRoute, jRoute):
    # TODO : merge the routes of i and j
    return NotImplemented

def calcRouteTravelTime(solution, route):
    # TODO : calculate the travel time of the route
    return NotImplemented

def validateMergeDrivingConstraints(travelTime, tmax):
    # TODO : check if the merge of i and j is valid
    return NotImplemented

def updateSolution(newRoute, iRoute, jRoute, sol):
    # TODO : update the solution after merging i and j
    return NotImplemented

def deleteEdgeFromSavingList(arc):
    # TODO : delete the edge (i,j) from the sorted saving list
    return NotImplemented

def sortRoutesByProfit(solution):
    # TODO : sort the routes by profit
    return NotImplemented

def deleteRoutesByProfit(sol, maxVehicles):
    # TODO : delete the routes that are not profitable
    return NotImplemented