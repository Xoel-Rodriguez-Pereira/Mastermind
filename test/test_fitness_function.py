from src.fitness_function import fitness_function
from colorama import Fore

def test_fitness_function():

    assert fitness_function([1, 1, 1, 1], [1, 1, 1, 1]) == 8

    assert fitness_function([1, 1, 1, 0], [0, 0, 0, 3]) == 1

    assert fitness_function([1, 1, 0, 0], [1, 3, 3, 3]) == 2