
from src.user_input import correct_code
from src.generation_generator import generation_generator
from src.offspring import offspring
from src.select_representative_individual import select_representative_individual
from src.select_representative_individual import solutions_history
from src.print_solutions import print_solutions


def mainloop():
    solution = correct_code()
    generation = 1

    values, fitness = generation_generator(solution)

    solutions_history = select_representative_individual(values, fitness)
    print_solutions(solutions_history, solution)
    
    if solutions_history[-1] != solution:
        while generation <= 14:

            values, fitness = offspring(values, fitness)
            generation += 1
            solutions_history = select_representative_individual(values, fitness)
            print_solutions(solutions_history, solution)
            
            if solutions_history[-1] == solution:
                break


    

    










    





    



