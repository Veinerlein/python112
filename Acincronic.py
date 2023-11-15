import time
from threading import Thread


def first_func():
    print("1 Func start")
    time.sleep(6)
    print("1 Func Finished")


def second_func():
    print("2 Func start")
    time.sleep(6)
    print("2 Func Finished")


# Thread(target=first_func()).start()
# Thread(target=second_func()).start()
t1 = Thread(target=first_func())
t1.start()
t2 = Thread(target=second_func())
t2.start()


