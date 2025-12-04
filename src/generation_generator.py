import random

def generation_generator(generation_size, code_lenght):

    pins = ('rojo', 'verde', 'azul', 'amarillo', 'roja', 'celeste', 'blanco', 'negro')

    generation = {}
    for individual in generation_size:

        individual_code = list(pins[random.randrange(0,7)] for _ in range(code_lenght))
        generation[individual] = individual_code
    
    return generation