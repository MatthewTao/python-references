import datetime as dt
import multiprocessing
import time
from pyautogui import prompt


def get_user_input(queue: multiprocessing.Queue):
    for i in range(5):
        # The built-in input doesn't work.
        user_input = prompt(
            text="Input your wisdom", title="Simple Queue Example", default=""
        )
        queue.put(user_input)

    print("Entered all the allowed inputs. Process 1 will now end.")


def print_user_input(queue: multiprocessing.Queue):
    start = time.time()
    print(f"{dt.datetime.now().isoformat()} - Starting Listener")
    while True:
        if not queue.empty():
            print(queue.get())
        else:
            time.sleep(1)  # let it chill out for a bit

        if time.time() - start > 60 * 3:
            # Only run the little demo for 3 minutes
            break

    print(f"{dt.datetime.now().isoformat()} - Process 2 will now end")


if __name__ == "__main__":
    message_queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=get_user_input, args=(message_queue,))
    p2 = multiprocessing.Process(target=print_user_input, args=(message_queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
