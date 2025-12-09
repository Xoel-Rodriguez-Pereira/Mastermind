from src.generation_generator import generation_generator
import random
from colorama import Fore


def test_generation_generation():

    generation = generation_generator (200, 4, [Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹'])
    assert len(generation) == 200
    assert len(generation[random.randint(0,200)]) == 2
    assert len(generation[random.randint(0,200)][0]) == 4
