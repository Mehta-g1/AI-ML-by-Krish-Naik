from logger import logging

def add(a,b):
    logging.debug("The addition Operation is taking place")

    return a+b


logging.debug("The addition function is gatting called")
add(5,10)