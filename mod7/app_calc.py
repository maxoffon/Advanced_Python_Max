import json
import logging
import logging.handlers
import requests

# import sys
import utils_calc as utils
from dict_config import dict_conf
import logging.config as cfg
import logging_tree

'''
def configurate_log(logger):
    logger.setLevel('DEBUG')
    handler = logging.StreamHandler()
    handler.setStream(sys.stdout)

    formatter = logging.Formatter(fmt='%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s')
    handler.setFormatter(formatter)

    levels = ['notset', 'debug', 'info', 'warning', 'error', 'critical']
    for lvl in levels:
        file_hdl = logging.FileHandler(f'calc_{lvl}.log', mode='a', encoding='utf-8')
        file_hdl.setFormatter(formatter)
        file_hdl.addFilter(CustomFilter(lvl))
        logger.addHandler(file_hdl)

    logger.addHandler(handler)
'''


class CustomFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record: logging.LogRecord) -> bool:
        return self.level == record.levelname.lower()


class AsciiFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().isascii()


class CustomHttpHandler(logging.handlers.HTTPHandler):
    def __init__(self, url, host, method):
        super().__init__(url=url, host=host, method=method)

    def emit(self, record: logging.LogRecord) -> None:
        res = self.mapLogRecord(record)
        requests.post(self.url, json.dumps(res))


def main():
    app_logger = logging.getLogger('calculator_app')
    # configurate_log(app_logger)
    operations = {'+': utils.addition, '-': utils.subtraction, '*': utils.multiplication, '/': utils.division}
    try:
        a, operation, b = input('Provide the expression using following format: A + B: ').split()
        app_logger.info(f'The expression is received: {a} {operation} {b}')
        result = operations[operation](a, b)
        app_logger.debug('Operation is successful')
        print('Answer:', result)

    except (ValueError, ZeroDivisionError):
        app_logger.error('Wrong format')
    except KeyError:
        app_logger.error('Wrong operation, use +, -, *, / only')


if __name__ == '__main__':
    cfg.dictConfig(dict_conf)
    with open('logging_tree.txt', 'w', encoding='utf-8') as file:
        file.write(logging_tree.format.build_description())
    main()
