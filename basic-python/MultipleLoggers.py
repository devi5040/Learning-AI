import logging

# Logger 1: for database
db_logger = logging.getLogger('database')
db_logger.setLevel(logging.DEBUG)

db_handler = logging.FileHandler('database.log')
db_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
db_logger.addHandler(db_handler)


# Logger 2: for API
api_logger = logging.getLogger('api')
api_logger.setLevel(logging.INFO)

api_handler = logging.FileHandler('api.log')
api_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
api_logger.addHandler(api_handler)


# Using the loggers
db_logger.debug("Database connection successful.")
db_logger.warning("Query took too long.")

api_logger.info("API request received.")
api_logger.error("API failed to respond.")