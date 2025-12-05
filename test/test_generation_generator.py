from src.generation_generator import generation_generator
import random


def test_generation_generation():

    generation = generation_generator (200, 4)
    assert len(generation) == 200
    assert len(generation[random.randint(0,200)]) == 4
