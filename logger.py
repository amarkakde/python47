import logging

logging.basicConfig(level=logging.DEBUG, filename='logger.txt')

def logging_initial():
    logger = {
        'CRITICAL':logging.CRITICAL,
        'ERROR':logging.ERROR,
        'WARNING':logging.WARNING,
        'INFO':logging.INFO,
        'DEBUG': logging.DEBUG}

    logging.critical('critial message')
    logging.warning('warning message')
    logging.error('error message')
    logging.info('info messaege')
    logging.debug('debug message')

def try_logger_first_time():
    logger = logging.getLogger(try_logger_first_time.__name__)
    logger.info(f'in {try_logger_first_time.__name__} function started.')
    for value in range(10):
        logger.log(logging.INFO, msg=f'{value} calculated')
    logger.info('{try_logger_first_time.__name__} function completed')


