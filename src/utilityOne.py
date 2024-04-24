<<<<<<< HEAD
import random
import string

def MainFunction(text):
    print("I can put in anything here, but it will be overwritten when main.py imports me")
    print("This is because there's an overriding function with same name present")

def GetRandomText():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

if __name__ == "__main__":
    print("Testing GetRandomText(): \n", GetRandomText)
=======
import random
import string

def MainFunction(text):
    print("I can put in anything here, but it will be overwritten when main.py imports me")
    print("This is because there's an overriding function with same name present")

def GetRandomText():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

if __name__ == "__main__":
    print("Testing GetRandomText(): \n", GetRandomText)
>>>>>>> 955d19c3e56ac38de6c16326d9b340cd99a379a5
