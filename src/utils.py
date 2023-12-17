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
    return ( scores.mean() - scores.std() ) / scores.mean()

# Returns the VRP savings matrix
def vrp_savings(time, n):
    savings = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j :
                savings[i, j] = time[i,n-1] + time[0,j] - time[i, j]
    return savings

# Returns the TOP sorted list where each element is a tuple (saving, i, j) 
# i and j are the indices of the clients corresponding to the compium of the saving from i to j 
def top_savings(coords, savings, alpha, n, banned_routes):
    new_savings = np.zeros((n, n, 3))
    visited_pairs = set()  # Keep track of visited pairs to avoid duplication

    for i in range(n):
        for j in range(n):
            if i != j and ((i, j) not in visited_pairs or (j, i) not in visited_pairs) and i not in banned_routes and j not in banned_routes:
                new_savings[i, j, 0] = alpha * savings[i, j] + (1 - alpha) * (coords['s'][i] + coords['s'][j])
                new_savings[i, j, 1] = i  # i element
                new_savings[i, j, 2] = j  # j element
                visited_pairs.add((i, j))  # Mark the pair as visited
                visited_pairs.add((j, i))  # Mark the reverse pair as visited
    
    # Flatten the 3D array into a list of tuples
    list_of_tuples = [tuple(row) for row in new_savings.reshape((-1, 3)) if not all(elem == 0 for elem in row) and row[2] != 0 and row[1] != n-1 and row[1] != 0 and row[2] != n-1]

    # Sort the list based on the saving values (element 0 of each tuple)
    sorted_top_savings_list = sorted(list_of_tuples, key=lambda x: x[0], reverse=True)

    return sorted_top_savings_list

 
def init_solution(time, coords, n, tmax):
    # create a data frame composed by the route of each vehicle , its total travel time and its profit
    sol = pd.DataFrame(columns=['route', 'travel_time', 'profit'])
    # initialize every routes with only one client
    for i in range(1, n-1):
        sol.loc[i] = [[i], time[0, i] + time[i, n-1], int(coords['s'][i])]

    # Remove routes with travel_time > tmax
    banned_routes = []
    for index, row in sol.iterrows():
        if row['travel_time'] > tmax:
            sol = sol.drop(index)
            banned_routes.append(index)

    return sol, banned_routes

def selectNextArc(sorted_savings_list):
    return sorted_savings_list[0]

def GetiRoute(solution, i):
    for index, row in solution.iterrows():
        if i in row['route']:
            return index, row['route']

def GetjRoute(solution, j):
    for index, row in solution.iterrows():
        if j in row['route']:
            return index, row['route']

def mergeRoutes(iRoute, jRoute, i, j, n):
    # Merge the routes by concatenating the client lists of iRoute and jRoute if these are terminal points
    if iRoute[-1] == i or jRoute[0] == j:
        return iRoute + jRoute  # Combine without considering the depot 
    return []  # Return an empty list if the conditions are not met

def calcRouteTravelTime(solution, iIndex, jIndex, time_matrix, n):
    return solution.loc[iIndex]['travel_time'] + solution.loc[jIndex]['travel_time'] + time_matrix[iIndex, jIndex] - time_matrix[0, jIndex] - time_matrix[iIndex, n-1]
        


def validateMergeDrivingConstraints(travelTime, tmax):
    return travelTime <= tmax

def updateSolution(solution, newRoute, iIndex, jIndex, jRoute, travelTime):
     # Update the solution DataFrame with the newly merged route
    solution.at[iIndex, 'route'] = newRoute
    
    # Recalculate travel time for the merged route (assuming time is a column in the DataFrame)
    solution.at[iIndex, 'travel_time'] = travelTime
    
    # Sum the profits of the merged routes and update the solution DataFrame
    test1 = solution.loc[iIndex]['profit']
    test2 = solution.loc[jIndex]['profit']

    total_profit = solution.loc[iIndex]['profit'] + solution.loc[jIndex]['profit']
    solution.at[iIndex, 'profit'] = total_profit
    
    # Drop the jRoute as it's been merged into iRoute
    solution = solution.drop(jRoute)

def deleteEdgeFromSavingList(arc):
    arc.pop(0)

def sortRoutesByProfit(solution):
    return solution.sort_values(by='profit', ascending=False)

def deleteRoutesByProfit(sol, maxVehicles):
    # Sort routes by profit
    sol = sol.sort_values(by='profit', ascending=False)
    
    # Keep only the top 'maxVehicles' profitable routes
    sol = sol.head(maxVehicles)
    
    return sol

def two_opt(route, time_matrix, n):
    best = route.copy()  # Make a copy of the original route
    improved = True

    while improved:
        improved = False

        for i in range(1, n-2):
            for j in range(i+1, n-1):
                if j-i == 1:
                    continue  # Changes nothing, skip then

                new_route = route[:i] + route[i:j][::-1] + route[j:]

                new_route_travel_time = calculate_route_travel_time(new_route, time_matrix)

                route_travel_time = calculate_route_travel_time(route, time_matrix)

                if new_route_travel_time < route_travel_time:
                    best = new_route[:]
                    improved = True

        route = best[:]

    return best

def or_opt(route, time_matrix, n):
    best = route.copy()  # Make a copy of the original route
    improved = True

    while improved:
        improved = False

        for i in range(1, n-2):
            for j in range(i+2, n):
                if j >= len(route):
                    continue  # Skip if j is out of bounds

                for k in range(n):
                    if k != i and k != j:
                        new_route = (
                            route[:i] +
                            [route[j]] +
                            route[i+1:j] +
                            [route[i]] +
                            route[j+1:]
                        )

                        new_route_travel_time = calculate_route_travel_time(new_route, time_matrix)
                        route_travel_time = calculate_route_travel_time(route, time_matrix)

                        if new_route_travel_time < route_travel_time:
                            best = new_route[:]
                            improved = True

        route = best[:]

    return best

def calculate_route_travel_time(route, time_matrix):
    travel_time = time_matrix[0, route[0]] + time_matrix[route[-1], len(route) - 1]
    travel_time += sum([time_matrix[route[k], route[k + 1]] for k in range(len(route) - 1)])
    return travel_time