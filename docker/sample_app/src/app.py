"""
Entry point to whatever
"""
import logging
import os
import time


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    while True:
        logging.info("I am groot")
        logging.info(f"Read from env: {os.getenv('SECRET_MESSAGE')}")

        # Silly loop to keep the container alive.
        # Therefore, the container can be explored interactively
        time.sleep(5)
