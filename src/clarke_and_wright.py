import utils as ut

def clarke_wright(solution, sorted_savings_list, tmax, time_matrix, n, m):
    
    while len(sorted_savings_list) != 0 :
        arc = ut.selectNextArc(sorted_savings_list)
        iIndex, iRoute = ut.GetiRoute(solution, arc[1])
        jIndex, jRoute = ut.GetjRoute(solution, arc[2])
        newRoute = ut.mergeRoutes(iRoute, jRoute, arc[1], arc[2], n)
        newtravelTime = ut.calcRouteTravelTime(solution, iIndex, jIndex, time_matrix, n)
        if ut.validateMergeDrivingConstraints(newtravelTime, tmax) and newRoute != []:
            # two_opt_route = ut.two_opt(newRoute, time_matrix, n)
            # ut.updateSolution(solution, two_opt_route, iIndex, jIndex, jRoute, newtravelTime)
            or_opt_route = ut.or_opt(newRoute, time_matrix, n)
            ut.updateSolution(solution, or_opt_route, iIndex, jIndex, jRoute, newtravelTime)
            ut.deleteEdgeFromSavingList(sorted_savings_list)
        else:
            ut.deleteEdgeFromSavingList(sorted_savings_list)
    
    solution = ut.sortRoutesByProfit(solution)
    solution = ut.deleteRoutesByProfit(solution, m)

    return solution
        