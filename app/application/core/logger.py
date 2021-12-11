import logging


def create_logger(log_level):
    console_handler = logging.StreamHandler()
    line_format = '[%(asctime)s] | %(levelname)s : %(message)s'
    date_format = '%d-%m-%Y %H:%M:%S'
    logging.basicConfig(format=line_format, datefmt=date_format, level=log_level, handlers=[console_handler])
    return logging.getLogger('enlighten')
