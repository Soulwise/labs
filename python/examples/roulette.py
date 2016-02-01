#!/usr/bin/env python
from __future__ import print_function
import random


def get_random(iterations=100, values=2):
    result = [random.randint(0, 100) for _ in range(iterations)]
    random.shuffle(result)
    return [result[random.randint(0, iterations)] for _ in range(values)]


def roulette():
    values = get_random(iterations=200, values=6)
    if values[0] > max(values[1:]):
        return False
    return True

if __name__ == "__main__":
    print(roulette())
