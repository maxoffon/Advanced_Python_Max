import logging


def addition(a, b):
    try:
        logger.info('Addition operation is starting')
        result = int(a) + int(b)
        logger.info(f'Operation\'s result: {result}')
        return result
    except ValueError:
        logger.error('Operation is impossible')
        raise


def subtraction(a, b):
    try:
        logger.info('Subtracion operation is starting')
        result = int(a) - int(b)
        logger.info(f'Operation\'s result: {result}')
        return result
    except ValueError:
        logger.error('Operation is impossible')
        raise


def multiplication(a, b):
    try:
        logger.info('Multiplication operation is starting')
        result = int(a) * int(b)
        logger.info(f'Operation\'s result: {result}')
        return result
    except ValueError:
        logger.error('Operation is impossible')
        raise


def division(a, b):
    try:
        logger.info('Division operation is starting')
        result = int(a) / int(b)
        logger.info(f'Operation\'s result: {result}')
        return result
    except ValueError:
        logger.error('Operation is impossible')
        raise
    except ZeroDivisionError:
        logger.warning('You can\'t divide by zero')
        raise


logger = logging.getLogger('calculator_utils')
# configurate_log(logger)
