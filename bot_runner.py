from multiprocessing import Process
from main import run_bot
import time

if __name__ == '__main__':
    keywords_list = ['door panic bar', 'Emergency exit doors']
    quantities_list = [5, 2]

    processes = []
    for keywords, quantities in zip(keywords_list, quantities_list):
        process = Process(target=run_bot, args=(keywords, quantities))
        processes.append(process)
        process.start()
        time.sleep(30)

    for process in processes:
        process.join()

