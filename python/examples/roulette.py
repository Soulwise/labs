#!/usr/bin/env python
from __future__ import print_function
import random


def get_number(number=random.randint(0, 100)):
    return number


def get_random(iterations, values):
    result = [get_number() for _ in range(iterations)]
    random.shuffle(result)
    return [result[random.randint(0, iterations)] for _ in range(values)]


def roulette():
    values = get_random(iterations=200, values=6)
    if values[0] > max(values[1:]):
        return False
    return True

if __name__ == "__main__":
    print(roulette())
