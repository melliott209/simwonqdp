import tkinter as tk
from tkinter import ttk
import tkcalendar
import utils

# CONSTANTS
WIDGET_WIDTH = 15

# TODO: In INI file, new list of parts and partnos from Master List with all subs/singles,etcy
# Process INI file into variables
ini_parts = open("parts.ini","r")
parts = utils.readList(ini_parts)
partnos = utils.readList(ini_parts)
endassy = utils.readList(ini_parts)
line = utils.readList(ini_parts)
cause = utils.readList(ini_parts)
rework = utils.readList(ini_parts)
supplier = utils.readList(ini_parts)
process = utils.readList(ini_parts)
shift = utils.readList(ini_parts)
dept = utils.readList(ini_parts)
ini_parts.close()

# Create window
window = tk.Tk()
window.title("Simwon QDP")
tk.Grid.rowconfigure(window,0,weight=1)
tk.Grid.columnconfigure(window,0,weight=1)

## Create Tab holder
tabCtl = ttk.Notebook(window)
tk.Grid.rowconfigure(tabCtl,0,weight=1)
tk.Grid.columnconfigure(tabCtl,0,weight=1)

## Create tabs
tabAdd = tk.Frame(tabCtl)
tabEdit = tk.Frame(tabCtl)

### Add functionality to "Add Entry" Tab

#### Add "General" Container
generalLabel = tk.Label(tabAdd,text="General",width=WIDGET_WIDTH)
general = tk.Frame(tabAdd,relief=tk.GROOVE,borderwidth=1)

dateLabel = tk.Label(general,text="Date",width=WIDGET_WIDTH).grid(row=0,column=0)
dateEntry = tkcalendar.DateEntry(general,width=WIDGET_WIDTH).grid(row=0,column=1)
partNameLabel = tk.Label(general,text="Part Name",width=WIDGET_WIDTH).grid(row=1,column=0,sticky='nsew')
partNameEntry = ttk.Combobox(general,width=WIDGET_WIDTH,values=parts).grid(row=1,column=1,sticky='nsew')
partNoLabel = tk.Label(general,text="Part Number",width=WIDGET_WIDTH).grid(row=2,column=0,sticky='nsew')
partNoEntry = tk.Label(general,width=WIDGET_WIDTH).grid(row=2,column=1,sticky='nsew')
endAssyLabel = tk.Label(general,text="End Assembly",width=WIDGET_WIDTH).grid(row=3,column=0,sticky='nsew')
endAssyEntry = ttk.Combobox(general,width=WIDGET_WIDTH,values=endassy).grid(row=3,column=1,sticky='nsew')
lineLabel = tk.Label(general,text="Line",width=WIDGET_WIDTH).grid(row=4,column=0,sticky='nsew')
lineEntry = ttk.Combobox(general,width=WIDGET_WIDTH,values=line).grid(row=4,column=1,sticky='nsew')

tk.Grid.rowconfigure(general,0,weight=1)
tk.Grid.columnconfigure(general,0,weight=1)
generalLabel.grid(row=0,column=0)
general.grid(row=1,column=0,sticky='nsew')

#### Add "Defect" Container
defectLabel = tk.Label(tabAdd,text="Defect",width=WIDGET_WIDTH)
defect = tk.Frame(tabAdd,relief=tk.GROOVE,borderwidth=1)

descLabel = tk.Label(defect,text="Description",width=WIDGET_WIDTH).grid(row=0,column=0,sticky='nsew')
descEntry = tk.Text(defect,width=WIDGET_WIDTH,height=5).grid(row=0,column=1,sticky='nsew')
causeLabel = tk.Label(defect,text="Cause",width=WIDGET_WIDTH).grid(row=1,column=0,sticky='nsew')
causeEntry = ttk.Combobox(defect,width=WIDGET_WIDTH,values=cause).grid(row=1,column=1,sticky='nsew')
qtyLabel = tk.Label(defect,text="Quantity",width=WIDGET_WIDTH).grid(row=2,column=0,sticky='nsew')
qtyEntry = tk.Spinbox(defect,from_=0,to=10000,width=WIDGET_WIDTH).grid(row=2,column=1,sticky='nsew')
decisionLabel = tk.Label(defect,text="Rework/Scrap",width=WIDGET_WIDTH).grid(row=3,column=0,sticky='nsew')
decisionEntry = ttk.Combobox(defect,width=WIDGET_WIDTH,values=rework).grid(row=3,column=1,sticky='nsew')
costLabel = tk.Label(defect,text="Scrap Cost",width=WIDGET_WIDTH).grid(row=4,column=0,sticky='nsew')
costEntry = tk.Entry(defect,width=WIDGET_WIDTH).grid(row=4,column=1,sticky='nsew')

tk.Grid.rowconfigure(defect,0,weight=1)
tk.Grid.columnconfigure(defect,0,weight=1)
defectLabel.grid(row=0,column=1)
defect.grid(row=1,column=1,sticky='nsew')

# TODO: Add "Images" Container

# TODO: Add "Accountability" Container
accountLabel = tk.Label(tabAdd,text="Accountability",width=WIDGET_WIDTH)
account = tk.Frame(tabAdd,relief=tk.GROOVE,borderwidth=1)

supplierLabel = tk.Label(account,text="Supplier",width=WIDGET_WIDTH).grid(row=0,column=0,sticky='nsew')
supplierEntry = ttk.Combobox(account,width=WIDGET_WIDTH,values=supplier).grid(row=0,column=1,sticky='nsew')
processLabel = tk.Label(account,text="Process",width=WIDGET_WIDTH).grid(row=1,column=0,sticky='nsew')
processEntry = ttk.Combobox(account,width=WIDGET_WIDTH,values=process).grid(row=1,column=1,sticky='nsew')
shiftLabel = tk.Label(account,text="Shift",width=WIDGET_WIDTH).grid(row=2,column=0,sticky='nsew')
shiftEntry = ttk.Combobox(account,width=WIDGET_WIDTH,values=shift).grid(row=2,column=1,sticky='nsew')
deptLabel = tk.Label(account,text="Responsible Dept.",width=WIDGET_WIDTH).grid(row=3,column=0,sticky='nsew')
deptEntry = ttk.Combobox(account,width=WIDGET_WIDTH,values=dept).grid(row=3,column=1,sticky='nsew')
qcLabel = tk.Label(account,text="QC Inspector",width=WIDGET_WIDTH).grid(row=4,column=0,sticky='nsew')
qcEntry = tk.Entry(account,width=WIDGET_WIDTH).grid(row=4,column=1,sticky='nsew')
personLabel = tk.Label(account,text="Responsible Person",width=WIDGET_WIDTH).grid(row=5,column=0,sticky='nsew')
personEntry = tk.Entry(account,width=WIDGET_WIDTH).grid(row=5,column=1,sticky='nsew')
remarkLabel = tk.Label(account,text="Remarks",width=WIDGET_WIDTH).grid(row=6,column=0,sticky='nsew')
remarkEntry = tk.Text(account,width=WIDGET_WIDTH,height=3).grid(row=6,column=1,sticky='nsew')

tk.Grid.rowconfigure(account,0,weight=1)
tk.Grid.columnconfigure(account,0,weight=1)
accountLabel.grid(row=2,column=1)
account.grid(row=3,column=1,sticky='nsew')

### Finalize "Add Entry" tab
tabCtl.add(tabAdd, text="Add Entry",sticky='nsew')

### TODO: Add functionality to "Edit Entry" tab

### Finalize "Edit Entry" tab
tabCtl.add(tabEdit, text="Edit Entry",sticky='nsew')

## Finalize tab holder
tabCtl.grid(row=0,column=0,sticky='nsew')

# Start main loop
window.mainloop()


