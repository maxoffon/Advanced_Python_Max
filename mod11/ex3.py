import logging
import random
import threading
import time

TOTAL_TICKETS = 10
SEATS_NUMBER = 100
SELLERS_COUNT = 4
TICKETS_ADD = 6
ARE_MORE_TICKETS = True

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Head(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Headmaster started work')

    def run(self):
        global TOTAL_TICKETS, ARE_MORE_TICKETS
        while True:
            if TOTAL_TICKETS <= SELLERS_COUNT:
                self.random_sleep()
                if TOTAL_TICKETS + TICKETS_ADD > SEATS_NUMBER:
                    ARE_MORE_TICKETS = False
                    logger.info(f'{self.name}:Head No more tickets;')
                    break
                else:
                    TOTAL_TICKETS += TICKETS_ADD
                    logger.info(f'{self.name}:Head added some tickets;  {TOTAL_TICKETS} now')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))
class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS, SEATS_NUMBER
        is_running = True
        while is_running:
            if TOTAL_TICKETS <= SELLERS_COUNT and ARE_MORE_TICKETS:
                self.random_sleep()
                continue
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                SEATS_NUMBER -= 1
                logger.info(f'{self.name} sold one;  {TOTAL_TICKETS} left')

        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))

def main():
    semaphore = threading.Semaphore()
    sellers = []

    head = Head(semaphore)
    head.start()

    for _ in range(SELLERS_COUNT):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()


if __name__ == '__main__':
    main()