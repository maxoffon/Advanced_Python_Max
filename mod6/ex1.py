import getpass
import hashlib
import logging
import ex2


logger = logging.getLogger('password_checker')


def input_and_check_password():
    password = getpass.getpass()

    if not password:
        logger.warning('Вы ввели пустой пароль')
        return False

    try:
        if ex2.is_strong_password(password):
            logger.info('Password is strong')
        else:
            logger.error('Password is week')

        hasher = hashlib.md5()
        hasher.update(password.encode('latin-1'))

        if hasher.hexdigest() == '098f6bcd4621d373cade4e832627b4f6':
            return True
        logger.error('Вы ввели неправильный пароль ')

    except ValueError as e:
        logger.exception('Вы ввели некорректный пароль ', exc_info=e)

    return False


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='stderr.txt',
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S')
    logger.info('Вы пытаетесь авторизоваться в Skillbox')
    count_number = 3
    logger.info(f'У вас есть {count_number} попыток')

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error('Пользователь трижды ввёл неверный пароль!')
    exit(1)
