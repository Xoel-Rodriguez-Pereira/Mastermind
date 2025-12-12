import random
from fitness_function import fitness_function
from constants import GENERATION_SIZE, PINS

def generation_generator(code_lenght, solution):
    
    individual_value = tuple(list(PINS[random.randint(0,7)] for _ in range(code_lenght)) for _ in range(GENERATION_SIZE))
    values = {individual : individual_value[individual] for individual in range(GENERATION_SIZE)}
    fitness = {individual : fitness_function(solution, individual_value[individual]) for individual in range(GENERATION_SIZE)}

    return values, fitness


