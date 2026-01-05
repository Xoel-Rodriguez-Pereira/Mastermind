import random
from src.fitness_function import fitness_function
from src.constants import GENERATION_SIZE, PINS, CODE_LENGHT

def first_generation(solution):
    
    individual_value = tuple(list(PINS[random.randint(0,7)] for _ in range(CODE_LENGHT)) for _ in range(GENERATION_SIZE))

    values = {individual : individual_value[individual] for individual in range(GENERATION_SIZE)}
    
    fitness = {individual : fitness_function(solution, individual_value[individual]) for individual in range(GENERATION_SIZE)}

    return values, fitness


