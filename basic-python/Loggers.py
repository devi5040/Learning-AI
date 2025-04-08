import logging

# Basic configuration
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

# Logging messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Custom logging into file
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('This will be logged to a file')

# Logging in the function
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Tried to divide by zero", exc_info=True)
divide(10, 0)
