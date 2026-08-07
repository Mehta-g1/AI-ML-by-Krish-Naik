import logging

# Logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s ',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {a}-{b} = {result}")
    return result

def multiplication(a, b):
    result = a * b
    logger.debug(f"Multiplication {a}+{b} = {result}")
    return result

def devide(a, b):
    try:
        result = a / b
        logger.debug(f"Devide {a}+{b} = {result} ")
        return result
    except ZeroDivisionError as e:
        logger.error(e)
        return None


add(10,15)
subtract(10,15)
multiplication(10,15)
devide(50,0)
