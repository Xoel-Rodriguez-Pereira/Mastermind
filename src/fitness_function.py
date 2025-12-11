
def fitness_function (solution, individual):

    solution_copy = solution[:]
    fitness = 0
    for position in range(len(solution)): # NOPE se utiliza para evitar que un elemento en la solucón pueda aumentar 
                                          # el fitness de un individuo por repetición
        if individual[position] == solution_copy[position]:
            fitness += 2  
            solution_copy[position] == 'NOPE'
            
        elif individual[position] in solution_copy:
            fitness += 1
            solution_copy[solution_copy.index(individual[position])] = 'NOPE'

        else:
            fitness += 0 
    
    return fitness


