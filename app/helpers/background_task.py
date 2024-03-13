""" This module contains the background task functions. 
"""

def after_route() -> None:
    """This function is executed after the route function terminated due to the background tasks
    """
    print(
        "This function is executed after the route function terminated due to the background tasks"
    )
