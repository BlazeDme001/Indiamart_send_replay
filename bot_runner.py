from multiprocessing import Process
from main import run_bot
import time

if __name__ == '__main__':
    keywords_list = ['fire resistant doors', 'lead lined doors']
    quantities_list = [30, 5]

    while True:
        processes = []
        for keywords, quantities in zip(keywords_list, quantities_list):
            process = Process(target=run_bot, args=(keywords, quantities))
            processes.append(process)
            process.start()
            time.sleep(30)

        for process in processes:
            process.join()
        time.sleep(120)
