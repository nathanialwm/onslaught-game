import logging
from logging.handlers import RotatingFileHandler

def setup_logger(dev_mode):
    logger = logging.getLogger("onslaught_logs")
    logger.setLevel(logging.DEBUG)
    # Console handler
    stream_handler = logging.StreamHandler()
    if dev_mode:
        stream_handler.setLevel(logging.DEBUG)
    else:
        stream_handler.setLevel(logging.WARNING)
    # File handler
    file_handler = RotatingFileHandler('onslaught_logs.log', maxBytes=2_000_000, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    # Add handlers to logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger
    
