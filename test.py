import logging
from pathlib import Path
import os

logging.basicConfig(level=logging.INFO, filename='test.log.txt', 
                    format='%(levelname)s:%(asctime)s:%(name)s:%(message)s')

logger = logging.getLogger(os.path.basename(__file__))

def add(x, y):
    logger.info(f'adding two numbers {x} {y}')
    return x + y

def main():
    logger.info('inside main...two variables initiated')
    num1 = 25
    num2 = 78
    logger.info(f'function add() called with {num1} and {num2}')
    result = add(num1, num2)
    logger.info(f'result recieved from add() {result=}')

if __name__=='__main__':
    logger.info(f'module {os.path.basename(__file__)} initialized...')
    main()