import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkcalendar

# CONSTANTS
WIDGET_WIDTH = 15
FILE_LABEL_DEFAULT = "None Chosen"
DEFAULT_PADDING = 5

#============================================================
# Define Functions
#============================================================

# Reads line from INI file and returns a list
def readList(iniFile):
    string = iniFile.readline()
    startIndex = string.find("=") + 1
    return string[startIndex:].split(",")

# Chooses a file and returns it to the button that asked for it
def chooseFile(label):
    fileName = filedialog.askopenfilename(title="Select File")
    label.insert(0,fileName)
    return

# Chooses a directory and returns it to the button that asked for it
def chooseDir(label):
    dirName = filedialog.askdirectory(title="Choose Directory")
    label.insert(0,dirName)
    return

#============================================================
# Load and Process Input Files
#============================================================

# TODO: In INI file, new list of parts and partnos from Master List with all subs/singles,etcy
# Process INI file into variables
ini_parts = open("parts.ini","r")
parts = readList(ini_parts)
partnos = readList(ini_parts)
endassy = readList(ini_parts)
line = readList(ini_parts)
cause = readList(ini_parts)
rework = readList(ini_parts)
supplier = readList(ini_parts)
process = readList(ini_parts)
shift = readList(ini_parts)
dept = readList(ini_parts)
ini_parts.close()

#============================================================
# GUI Code
#============================================================

# Create window
window = tk.Tk()
window.title("Simwon QDP")
window.resizable(False,False)

## Create Tab holder
tabCtl = ttk.Notebook(window)

## Create tabs
tabAdd = tk.Frame(tabCtl,padx=DEFAULT_PADDING,pady=DEFAULT_PADDING)
tabEdit = tk.Frame(tabCtl,padx=DEFAULT_PADDING,pady=DEFAULT_PADDING)
tabEdit.grid_columnconfigure(0,weight=1)
tabEdit.grid_columnconfigure(1,weight=1)

### Add functionality to "Add Entry" Tab

#### Add "General" Container
generalLabel = tk.Label(tabAdd,text="General",relief=tk.GROOVE)
general = tk.Frame(tabAdd,relief=tk.GROOVE,borderwidth=1,padx=DEFAULT_PADDING,pady=DEFAULT_PADDING)

dateLabel = tk.Label(general,text="Date",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=0,column=0)
dateEntry = tkcalendar.DateEntry(general,width=WIDGET_WIDTH).grid(row=0,column=1)
partNameLabel = tk.Label(general,text="Part Name",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=1,column=0)
partNameEntry = ttk.Combobox(general,width=WIDGET_WIDTH,values=parts).grid(row=1,column=1)
partNoLabel = tk.Label(general,text="Part Number",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=2,column=0)
partNoEntry = tk.Label(general,width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=2,column=1,sticky='ew')
endAssyLabel = tk.Label(general,text="End Assembly",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=3,column=0)
endAssyEntry = ttk.Combobox(general,width=WIDGET_WIDTH,values=endassy).grid(row=3,column=1)
lineLabel = tk.Label(general,text="Line",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=4,column=0)
lineEntry = ttk.Combobox(general,width=WIDGET_WIDTH,values=line).grid(row=4,column=1)

generalLabel.grid(row=0,column=0,sticky='ew')
general.grid(row=1,column=0,sticky='n')

#### Add "Defect" Container
defectLabel = tk.Label(tabAdd,text="Defect",relief=tk.GROOVE)
defect = tk.Frame(tabAdd,relief=tk.GROOVE,borderwidth=1,padx=DEFAULT_PADDING,pady=DEFAULT_PADDING)

descLabel = tk.Label(defect,text="Description",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=0,column=0,sticky='n')
descEntry = tk.Text(defect,width=WIDGET_WIDTH,height=5).grid(row=0,column=1)
causeLabel = tk.Label(defect,text="Cause",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=1,column=0)
causeEntry = ttk.Combobox(defect,width=WIDGET_WIDTH,values=cause).grid(row=1,column=1,sticky='ew')
qtyLabel = tk.Label(defect,text="Quantity",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=2,column=0)
qtyEntry = tk.Spinbox(defect,from_=0,to=10000,width=WIDGET_WIDTH).grid(row=2,column=1,sticky='ew')
decisionLabel = tk.Label(defect,text="Rework/Scrap",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=3,column=0)
decisionEntry = ttk.Combobox(defect,width=WIDGET_WIDTH,values=rework).grid(row=3,column=1,sticky='ew')
costLabel = tk.Label(defect,text="Scrap Cost",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=4,column=0)
costEntry = tk.Entry(defect,width=WIDGET_WIDTH).grid(row=4,column=1,sticky='ew')

defectLabel.grid(row=0,column=1,sticky='ew')
defect.grid(row=1,column=1)

# TODO: Add "Images" Container

# Add "Accountability" Container
accountLabel = tk.Label(tabAdd,text="Accountability",relief=tk.GROOVE)
account = tk.Frame(tabAdd,relief=tk.GROOVE,borderwidth=1,padx=DEFAULT_PADDING,pady=DEFAULT_PADDING)

supplierLabel = tk.Label(account,text="Supplier",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=0,column=0)
supplierEntry = ttk.Combobox(account,width=WIDGET_WIDTH,values=supplier).grid(row=0,column=1,sticky='ew')
processLabel = tk.Label(account,text="Process",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=1,column=0)
processEntry = ttk.Combobox(account,width=WIDGET_WIDTH,values=process).grid(row=1,column=1,sticky='ew')
shiftLabel = tk.Label(account,text="Shift",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=2,column=0)
shiftEntry = ttk.Combobox(account,width=WIDGET_WIDTH,values=shift).grid(row=2,column=1,sticky='ew')
deptLabel = tk.Label(account,text="Responsible Dept.",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=3,column=0)
deptEntry = ttk.Combobox(account,width=WIDGET_WIDTH,values=dept).grid(row=3,column=1,sticky='ew')
qcLabel = tk.Label(account,text="QC Inspector",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=4,column=0)
qcEntry = tk.Entry(account,width=WIDGET_WIDTH).grid(row=4,column=1,sticky='ew')
personLabel = tk.Label(account,text="Responsible Person",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=5,column=0)
personEntry = tk.Entry(account,width=WIDGET_WIDTH).grid(row=5,column=1,sticky='ew')
remarkLabel = tk.Label(account,text="Remarks",width=WIDGET_WIDTH,relief=tk.GROOVE).grid(row=6,column=0,sticky='n')
remarkEntry = tk.Text(account,width=WIDGET_WIDTH,height=3).grid(row=6,column=1)

accountLabel.grid(row=2,column=1,sticky='ew')
account.grid(row=3,column=1)

### Finalize "Add Entry" tab
tabCtl.add(tabAdd, text="Add Entry")

### Add functionality to "Process CMM" tab
inputLabel = tk.Label(tabEdit,text="Input Files",relief=tk.GROOVE)
outputLabel = tk.Label(tabEdit,text="Output Options",relief=tk.GROOVE)
inputFrame = tk.Frame(tabEdit,relief=tk.GROOVE,borderwidth=1)
inputFrame.grid_columnconfigure(0,weight=1)
inputFrame.grid_columnconfigure(1,weight=1)
outputFrame = tk.Frame(tabEdit,relief=tk.GROOVE,borderwidth=1)
outputFrame.grid_columnconfigure(0,weight=1)
outputFrame.grid_columnconfigure(1,weight=2)
fileLabel1 = tk.Entry(inputFrame,relief=tk.GROOVE)
fileLabel2 = tk.Entry(inputFrame,relief=tk.GROOVE)
fileLabel3 = tk.Entry(inputFrame,relief=tk.GROOVE)
saveDirLabel = tk.Entry(outputFrame,relief=tk.GROOVE)
fileBtn1 = tk.Button(inputFrame,text="Choose File",command=lambda: chooseFile(fileLabel1))    # Have to pass lambda in order to pass args
fileBtn2 = tk.Button(inputFrame,text="Choose File",command=lambda: chooseFile(fileLabel2))
fileBtn3 = tk.Button(inputFrame,text="Choose File",command=lambda: chooseFile(fileLabel3))
saveDirBtn = tk.Button(outputFrame,text="Choose Directory",command=lambda: chooseDir(saveDirLabel))
fileLabel1.grid(row=0,column=1,sticky='nsew')
fileLabel2.grid(row=1,column=1,sticky='nsew')
fileLabel3.grid(row=2,column=1,sticky='nsew')
fileBtn1.grid(row=0,column=0,sticky='ew')
fileBtn2.grid(row=1,column=0,sticky='ew')
fileBtn3.grid(row=2,column=0,sticky='ew')
saveDirBtn.grid(row=0,column=0,sticky='ew')
saveDirLabel.grid(row=0,column=1,sticky='nsew')
inputLabel.grid(row=0,column=0,sticky='ew')
outputLabel.grid(row=0,column=1,sticky='ew')
inputFrame.grid(row=1,column=0,sticky='ew')
outputFrame.grid(row=1,column=1,sticky="new")

### Finalize "Process CMM" tab
tabCtl.add(tabEdit, text="Process CMM")

## Finalize tab holder
tabCtl.grid(row=0,column=0)

#============================================================
# Hand Program over to Window's Main Loop
#============================================================

# Start main loop
window.mainloop()
