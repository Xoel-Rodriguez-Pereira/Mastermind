
from src.user_input import correct_code
from src.generation_generator import generation_generator
from src.offspring import offspring
from src.select_representative_individual import select_representative_individual
from src.print_solutions import print_solutions
from src.constants import MAX_GENERATIONS 

def mainloop():
    solution = correct_code()
    generation = 1

    values, fitness = generation_generator(solution)

    solutions_history = []
    solutions_history += select_representative_individual(values, fitness)
    print_solutions(solutions_history, generation)
    
    while generation < MAX_GENERATIONS:

        if solutions_history[-1][0] == solution:
            break

        values, fitness = offspring(values, fitness, solution)
        generation += 1
        solutions_history = select_representative_individual(values, fitness)
        print_solutions(solutions_history, generation)
        
            


    

    










    





    



