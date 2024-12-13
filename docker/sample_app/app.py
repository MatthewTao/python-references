"""
Entry point to whatever
"""
import os


if __name__ == "__main__":
    print("I am groot")
    print(f"Read from env: {os.getenv('SECRET_MESSAGE')}")
