import random
from colorama import Fore
from src.generation_generator import generation_generator

def offspring (values, fitness):

    SAMPLE_SIZE = 100
    selected_individuals = random.sample(list(values.keys()), SAMPLE_SIZE)
    wheights = list(fitness[individual].values() for individual in selected_individuals) 

    return wheights

if __name__ == '__main__':

    offspring(* generation_generator(200, 4, [Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹']))