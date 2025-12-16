
def fitness_function (solution, individual):

    individual_copy = individual[:]
    solution_copy = solution[:]
    fitness = 0
    for position in range(len(solution)): # NOPE se utiliza para evitar que un elemento en la solucón pueda aumentar 
                                          # el fitness de un individuo por repetición
        if individual_copy[position] == solution_copy[position]:
            fitness += 2  
            solution_copy[position] = 'NOPE'
            individual_copy[position] = None

    for position in range(len(solution)):
        if individual_copy[position] != solution_copy[position] and individual_copy[position] in solution_copy:
            fitness += 1
            solution_copy[solution_copy.index(individual_copy[position])] = 'NOPE'
            individual_copy[position] = None

    
    if fitness == 0:
        fitness += 0.5

    return fitness
