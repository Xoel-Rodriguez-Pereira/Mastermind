
from user_input import correct_code
from select_survivors import select_survivors
from generation_generator import generation_generator
from offspring import offspring
from select_representative_individual import select_representative_individual
from select_representative_individual import solutions_history
from print_solutions import print_solutions


def mainloop():
    solution = correct_code()
    generation = 1

    values, fitness = generation_generator(solution)

    solutions_history = select_representative_individual(values, fitness, generation)
    print_solutions(solutions_history, solution)
    
    while generation <= 14:

        values, fitness = offspring(values, fitness)
        generation += 1
        solutions_history = select_representative_individual(values, fitness, generation)
        print_solutions(solutions_history, solution)
        
        if solutions_history[-1] == solution:
            break


    

    










    





    



