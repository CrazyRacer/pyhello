import threading, multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    # python 中只能通过多进程的方式 来将cpu吃死 , 多线程会被卡在GIL锁上
    t = multiprocessing.Process(target=loop)
    t.start()
