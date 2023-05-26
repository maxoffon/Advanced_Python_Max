import logging
import requests
import threading
import sqlite3
import time

URL = "https://swapi.dev/api/people/"
create_table = """
        DROP TABLE IF EXISTS star_wars;
        CREATE TABLE star_wars (
        name text primary key,
        birth_year text not null,
        gender text not null ) """
insert_request = """
INSERT INTO star_wars
VALUES (?, ?, ?)"""
logger = logging.getLogger('custom')
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S')

def add_value(values):
    with sqlite3.connect('database_mod11.db') as conn:
        c = conn.cursor()
        c.execute(insert_request, values)


def with_threading():
    with sqlite3.connect('database_mod11.db') as conn:
        cur = conn.cursor()
        cur.executescript(create_table)
    threads = []
    for i in range(20):
        index = i + 1 if i != 16 else 21
        res = requests.get(URL + f'{index}/').json()
        val = (res['name'], res['birth_year'], res['gender'])
        c = threading.Thread(target=add_value, args=[val])
        c.start()
        threads.append(c)

    for thread in threads:
        thread.join()



def no_threading():
    with sqlite3.connect('database_mod11.db') as conn:
        c = conn.cursor()
        c.executescript(create_table)
    for i in range(20):
        index = i + 1 if i != 16 else 21
        res = requests.get(URL + f'{index}/').json()
        add_value((res['name'], res['birth_year'], res['gender']))

def main():
    start_no_thread = time.time()
    no_threading()
    logger.info(f'Без потоков: {time.time() - start_no_thread} секунд')

    start_thread = time.time()
    with_threading()
    logger.info(f'С потоками: {time.time() - start_thread} секунд')


main()