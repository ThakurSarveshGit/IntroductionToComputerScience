import random
import string

def MainFunction(text):
    print("I can put in anything here, but it will be overwritten when main.py imports me")
    print("This is because there's an overriding function with same name present")

def GetRandomText():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

if __name__ == "__main__":
    print("Testing GetRandomText(): \n", GetRandomText)
