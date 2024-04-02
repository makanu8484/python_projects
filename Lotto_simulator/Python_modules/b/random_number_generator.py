"""
    Natural number generator.
    Utility functions.
"""
import random

def generate_number_between(min, max):
    """Randomizes a number from the range <min, max>.

    :param min:
    :param max:
    :return:
    """
    #pass
    number = int(random.random() * (max - min) + min)
    return number

def generate_until_drawn(number, min, max):
    """Randomly randomizes a number in the <min, max> range until it draws a number "number".

    :param number:
    :param min:
    :param max:
    :return: the number of draws needed to finally draw the number number.
    """
    #pass
    incrementor = 1
    while generate_number_between(min,max) != number:
        incrementor += 1
    return incrementor
