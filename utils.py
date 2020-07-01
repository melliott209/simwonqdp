#============================================================
# Functions
#============================================================

# Reads line from INI file and returns a list
def readList(iniFile):
    string = iniFile.readline()
    startIndex = string.find("=") + 1
    return string[startIndex:].split(",")
