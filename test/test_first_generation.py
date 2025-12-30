from src.first_generation import first_generation
from colorama import Fore


def test_first_generation():

    values, fitness = first_generation ([Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹'])
    assert len(values) == 200
    assert len(fitness) == 200
