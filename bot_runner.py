from multiprocessing import Process
from main import run_bot
import time

if __name__ == '__main__':
    while True:
        print('BOT Started')
        keywords_list = ['fire resistant doors', 'lead lined doors']
        quantities_list = [10, 2]
    
        processes = []
        for keywords, quantities in zip(keywords_list, quantities_list):
            process = Process(target=run_bot, args=(keywords, quantities))
            processes.append(process)
            process.start()
            time.sleep(30)
    
        for process in processes:
            process.join()

        print('BOT Ended')
        print('BOT will start after 23:59 hours')
        time.sleep(86400)
