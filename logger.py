import logging

def logging_initial():
    logger = {
        'CRITICAL':logging.CRITICAL,
        'ERROR':logging.ERROR,
        'WARNING':logging.WARNING,
        'INFO':logging.INFO,
        'DEBUG': logging.DEBUG}

    logging.basicConfig(level=logging.DEBUG)
    logging.critical('critial message')
    logging.warning('warning message')
    logging.error('error message')
    logging.info('info messaege')
    logging.debug('debug message')
