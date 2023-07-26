import uuid
import random
import string


def generate_random_string(length:int=32):
    """
    Generates a random string of all upper and lower case letters
    """
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_uuid():
    """
    This generates a random UUID
    """
    return uuid.uuid4()


def generate_uuid_device_time():
    """
    This generates a UUID based on the device ID and device time
    """
    return uuid.uuid1()


if __name__ == '__main__':
    print('Device id and current time')
    for _ in range(10):
        print(generate_uuid_device_time())

    print('Random UUID')
    for _ in range(10):
        print(generate_uuid())
