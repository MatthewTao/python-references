from threading import Thread
import time
from datetime import datetime
from pyautogui import prompt

thread_running = True


class TestObject:
    def __init__(self):
        self.run_thread = True

    def my_forever_while(self):
        current_time = datetime.now().isoformat()
        print(f"{current_time}: First thread is starting")
        # run this while there is no input
        while self.run_thread is True:
            time.sleep(5)
            current_time = datetime.now().isoformat()
            print(f"{current_time}: Another 5 seconds has passed in the 1st thread")
            # if time.time() - start_time >= 5:
            #     start_time = time.time()
            #     print('Another 5 seconds has passed')
        print(f"{datetime.now().isoformat()}: First thread is now ending")

    def take_input(self):
        user_input = prompt(
            text="Input your wisdom", title="Simple Threading Example", default=""
        )
        # Normally this would require the process to stop and wait for the user input
        # Instead it is run on it's own thread, therefore the forever while

        # doing something with the input
        print("The user input is: ", user_input)
        print("Will end the 2nd thread now")


if __name__ == "__main__":
    test_object = TestObject()
    # Can alternatively pass in args with args or kwargs
    # e.g. Thread(target=some_function, args=(10, )
    t1 = Thread(target=test_object.my_forever_while)
    t2 = Thread(target=test_object.take_input)

    t1.start()
    t2.start()

    t2.join()  # interpreter will wait until your process get completed or terminated
    test_object.run_thread = False
    print("The end")
