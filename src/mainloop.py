from src.user_input import correct_code
from src.first_generation import first_generation
from src.offspring import offspring
from src.select_representative_individual import select_representative_individual
from src.print_solutions import print_solutions
from src.constants import MAX_GENERATIONS 
from src.grafics import fitness_grafic

def mainloop():
    
    generations_almanac = []
    fitness_almanac = []

    solution = correct_code()
    generation = 1

    values, fitness = first_generation(solution)

    solutions_history = []
    solutions_history += select_representative_individual (values, fitness, solutions_history)

    ## Registro para las gráficas
    generations_almanac += [generation]
    fitness_almanac += [list(fitness.values())]

    print_solutions(solutions_history, generation)

    while generation < MAX_GENERATIONS:

        if solutions_history[-1][0] == solution:
            break

        values, fitness = offspring(values, fitness, solution)
        generation += 1
        solutions_history += select_representative_individual (values, fitness, solutions_history)

        ## Registro para las gráficas
        generations_almanac += [generation]
        fitness_almanac += [list(fitness.values())]
        
        print_solutions(solutions_history, generation)
    
    fitness_grafic(generations_almanac, fitness_almanac)
            


    

    










    





    



