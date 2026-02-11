from logger import setup_logging
import time

logger = setup_logging()

def logger_test():
    logger.info("Запрос 1 успешен")
    time.sleep(0.5)
    logger.info("Запрос 2 успешен")
    time.sleep(0.5)
    logger.info("Запрос 3 успешен")
    time.sleep(0.5)
    logger.info("Запрос 4 успешен")
    time.sleep(0.5)


logger_test()