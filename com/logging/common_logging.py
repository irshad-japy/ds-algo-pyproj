import logging
import sys


def setup_logging():
    logger = logging.getLogger()
    for h in logger.handlers:
        logger.removeHandler(h)
    h = logging.StreamHandler(sys.stdout)
    FORMAT = '%(asctime)s log_level=%(levelname)s service_name="dl-to-rdb-ignition-lambda", %(message)s'
    h.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(h)
    logger.setLevel(logging.INFO)
    return logger


logger = setup_logging()


def print_sum():
    a, b = 20, 30
    logger.info("The sum of {} and {} is: ".format(a, b))
    logger.info(a+b)


print_sum()
