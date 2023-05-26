import logging
import requests
from multiprocessing.pool import Pool, ThreadPool
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
    with sqlite3.connect('database_mod12.db') as conn:
        c = conn.cursor()
        c.execute(insert_request, values)

def with_pool():
    with sqlite3.connect('database_mod12.db') as conn:
        cur = conn.cursor()
        cur.executescript(create_table)
    pool = Pool(processes=20)
    for i in range(20):
        index = i + 1 if i != 16 else 21
        res = requests.get(URL + f'{index}/').json()
        val = (res['name'], res['birth_year'], res['gender'])
        pool.apply(add_value, [val])
    pool.close()
    pool.join()

def with_threadpool():
    with sqlite3.connect('database_mod12.db') as conn:
        c = conn.cursor()
        c.executescript(create_table)

    tp = ThreadPool(processes=20)
    for i in range(20):
        index = i + 1 if i != 16 else 21
        res = requests.get(URL + f'{index}/').json()
        val = (res['name'], res['birth_year'], res['gender'])

        tp.apply(add_value, [val])
    tp.close()
    tp.join()

def main():
    start_no_thread = time.time()
    with_threadpool()
    logger.info(f'Pool: {time.time() - start_no_thread} секунд')

    start_thread = time.time()
    with_pool()
    logger.info(f'ThreadPool: {time.time() - start_thread} секунд')


main()