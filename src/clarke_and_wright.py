import src.utils as ut

def clarke_wright(savings):
    solution = ut.init_solution()

    # transformation de la matrice en liste en triant les valeurs par ordre décroissant
    saving_list = savings.flatten().tolist()
    # Order the list in descending order
    sorted_savings_list = sorted(saving_list, reverse=True)

    while sorted_savings_list.empty() is False:
        arc = ut.selectNextArc(sorted_savings_list)
        iRoute = solution[arc[0]]
        jRoute = solution[arc[1]]
        