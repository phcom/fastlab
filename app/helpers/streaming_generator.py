""" This module contains a generator function that yields a string with a number from 0 to 19. 
"""
def generator() -> str:
    """ This function is a generator that yields a string with a number from 0 to 19.
    """
    for i in range(20):
        yield f"Number {i}"
