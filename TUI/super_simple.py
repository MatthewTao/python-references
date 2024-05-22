import time


def updating_print(message=None, previous_message=None, clear=False):
    """
    This method prints a message in a way that can be updated
    """
    # Clear the line if there has already been a message there
    if previous_message is not None:
        print("\b" * len(previous_message), end="", flush=True)

    # Print out intended message
    if message is not None and clear is False:
        print(message, end="", flush=True)


def main():
    prev_msg = None
    count_down = 9
    for _ in range(10):
        message = f"Time left is {count_down}"
        updating_print(message, prev_msg)
        prev_msg = message
        count_down = count_down - 1
        time.sleep(1)

    updating_print(previous_message=prev_msg, clear=True)
    print("Count down should not be on the terminal anymore")


if __name__ == "__main__":
    print("starting test")
    print("Hey", end="", flush=True)
    time.sleep(1)
    for i in range(4):
        print("\b", end="")

    print("How is your day?")
    main()
