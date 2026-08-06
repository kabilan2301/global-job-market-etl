import logging
from .constants import LOG_FORMAT


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(format=LOG_FORMAT)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
