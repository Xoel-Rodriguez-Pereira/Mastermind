import random
from colorama import Fore
from generation_generator import generation_generator

def offspring (values, fitness):

    SAMPLE_SIZE = 100
    selected_individuals = random.sample(list(values.keys()), SAMPLE_SIZE)
    weights = list(fitness[individual].values() for individual in selected_individuals) 

    parents = (random.choices(selected_individuals, weights, k=2))

    return parents ##Aun sin terminar, el return está para que se pueda usar el debugger

if __name__ == '__main__':

    offspring(* generation_generator(200, 4, [Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹']))