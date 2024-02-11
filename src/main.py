# Main File
from utilityOne import MainFunction, GetRandomText

# This will overwrite MainFunction from utilityOne.py
def MainFunction(text):
    if text is None:
        print("Main Function Called")
    else:
        print(text)


# Following will only execute, when this file is directly run
if __name__ == "__main__":
    # From this file
    debugText = "This text will only show up when you run main.py directly"
    MainFunction(debugText)

    # Using an imported function
    MainFunction(GetRandomText())
