import logging
import csv

#logging.basicConfig(level=logging.DEBUG, filename='logger.txt')

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


"""
problem statement  
read data from 'data.csv' and calculate the total value for each product and dump the
data into reports.csv
"""

logging.basicConfig(level=logging.INFO, filename='data_processing_log.txt',
                    format='%(levelname)s:%(asctime)s:%(name)s:%(message)s')

def read_data(filename):
    try:
        logging.info('Initiating data read operation...')
        with open(filename, newline='') as fp:
            reader = csv.reader(fp)
            next(reader)
            datalist = [row for row in reader]
            processed_data = process_data(datalist)
    except FileNotFoundError as fnfe:
        logging.error(f'error {fnfe}')
    else:
        logging.info('Data processed...')
        return processed_data

def process_data(datalist):
    logging.info('processing data.')
    try:
        process_data_list = []
        for row in datalist:
            process_data_list.append([row[0], int(row[1]) * int(row[2])])
    except Exception as msg:
        logging.exception(msg)    
    
    return process_data_list

def write_data(filename, data):
    logging.info('data writing operation initiated...')
    try:
        with open(filename, 'w', newline='') as fp:
            columns = ['Product', 'Total Value']
            writer = csv.DictWriter(fp, fieldnames=columns)
            writer.writeheader()
            for row in data:
                writer.writerow({columns[0]:row[0], columns[1]:row[1]})
    except Exception as msg:
        logging.exception(msg)
    else:
        logging.info('Data successfully updated...')
        
def main():
    logging.info('main program initiated...')
    try:
        read_filename = 'data.csv'
        write_filename = 'reports.csv'
        data = read_data(read_filename)
        write_data(write_filename, data)
    except Exception as msg:
        logging.exception(msg)
    else:
        logging.info('successfully.')

if __name__ == '__main__':
    main()