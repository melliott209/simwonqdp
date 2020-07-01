import tkinter

#============================================================
# Functions
#============================================================

# Reads line from INI file and returns a list
def readList(iniFile):
    string = iniFile.readline()
    startIndex = string.find("=") + 1
    return string[startIndex:].split(",")

# Chooses a file and returns it to the button that asked for it
def chooseFile():
    return tkinter.filedialog.askopenfile()
