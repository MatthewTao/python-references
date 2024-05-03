from datetime import datetime
import multiprocessing
import os


def time_consuming_task(number=90000000):
    print(f"{datetime.now().isoformat()}: Start intensive task")
    result = sum(i * i for i in range(number))
    print(f"{datetime.now().isoformat()}: Intensive task finished")
    return result


def worker1(message):
    # printing process id
    print(f"{datetime.now().isoformat()}: ID of process running worker1: {os.getpid()}")
    print(message)

    time_consuming_task()
    print(f"{datetime.now().isoformat()}: First process finished")


def worker2(punctuation, message):
    print(f"{datetime.now().isoformat()}: Second process started")
    # printing process id
    print(f"{datetime.now().isoformat()}: ID of process running worker2: {os.getpid()}")

    print(message, punctuation)
    print(f"{datetime.now().isoformat()}: Second process finished")


if __name__ == "__main__":
    # printing main program process id
    print(f"{datetime.now().isoformat()}: ID of main process: {os.getpid()}")

    # creating processes
    p1 = multiprocessing.Process(target=worker1, args=("Hello world", ))
    p2 = multiprocessing.Process(target=worker2, kwargs={"message": "Hello World", "punctuation": "!"})

    # starting processes
    p1.start()
    p2.start()

    # process IDs
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    # wait until processes are finished
    p1.join()
    p2.join()

    # both processes finished
    print(f"{datetime.now().isoformat()}: Both processes finished execution!")

    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))
