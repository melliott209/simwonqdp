import tkinter as tk
from tkinter import ttk
import tkcalendar

# CONSTANTS
WIDGET_WIDTH = 15

# Create window
window = tk.Tk()
window.title("Simwon QDP")
window.geometry("600x400")

## Create Tab holder
tabCtl = ttk.Notebook(window)

## Create tabs
tabAdd = tk.Frame(tabCtl)
tabEdit = tk.Frame(tabCtl)

### Add functionality to "Add Entry" Tab

#### Add "General" Container
generalLabel = tk.Label(tabAdd,text="General",width=WIDGET_WIDTH)
general = ttk.Frame(tabAdd,relief=tk.GROOVE,borderwidth=1)

dateLabel = tk.Label(general,text="Date",width=WIDGET_WIDTH).grid(row=0,column=0)
dateEntry = tkcalendar.DateEntry(general,width=WIDGET_WIDTH).grid(row=0,column=1)
partNameLabel = tk.Label(general,text="Part Name",width=WIDGET_WIDTH).grid(row=1,column=0)
partNameEntry = ttk.Combobox(general,width=WIDGET_WIDTH).grid(row=1,column=1)
partNoLabel = tk.Label(general,text="Part Number",width=WIDGET_WIDTH).grid(row=2,column=0)
partNoEntry = tk.Label(general,width=WIDGET_WIDTH).grid(row=2,column=1)
endAssyLabel = tk.Label(general,text="End Assembly",width=WIDGET_WIDTH).grid(row=3,column=0)
endAssyEntry = ttk.Combobox(general,width=WIDGET_WIDTH).grid(row=3,column=1)
lineLabel = tk.Label(general,text="Line",width=WIDGET_WIDTH).grid(row=4,column=0)
lineEntry = ttk.Combobox(general,width=WIDGET_WIDTH).grid(row=4,column=1)

generalLabel.grid(row=0,column=0)
general.grid(row=1,column=0)

#### Add "Defect" Container
defectLabel = tk.Label(tabAdd,text="Defect",width=WIDGET_WIDTH)
defect = tk.Frame(tabAdd,relief=tk.GROOVE,borderwidth=1)

descLabel = tk.Label(defect,text="Description",width=WIDGET_WIDTH).grid(row=0,column=0)
descEntry = tk.Text(defect,width=WIDGET_WIDTH,height=5).grid(row=0,column=1)
causeLabel = tk.Label(defect,text="Cause",width=WIDGET_WIDTH).grid(row=1,column=0)
causeEntry = ttk.Combobox(defect,width=WIDGET_WIDTH).grid(row=1,column=1)
qtyLabel = tk.Label(defect,text="Quantity",width=WIDGET_WIDTH).grid(row=2,column=0)
qtyEntry = tk.Spinbox(defect,from_=0,to=10000,width=WIDGET_WIDTH).grid(row=2,column=1)
decisionLabel = tk.Label(defect,text="Rework/Scrap",width=WIDGET_WIDTH).grid(row=3,column=0)
decisionEntry = ttk.Combobox(defect,width=WIDGET_WIDTH).grid(row=3,column=1)
costLabel = tk.Label(defect,text="Scrap Cost",width=WIDGET_WIDTH).grid(row=4,column=0)
costEntry = tk.Entry(defect,width=WIDGET_WIDTH).grid(row=4,column=1)

defectLabel.grid(row=0,column=1)
defect.grid(row=1,column=1)

# TODO: Add "Images" Container

# TODO: Add "Accountability" Container

### Finalize "Add Entry" tab
tabCtl.add(tabAdd, text="Add Entry")

### TODO: Add functionality to "Edit Entry" tab

### Finalize "Edit Entry" tab
tabCtl.add(tabEdit, text="Edit Entry")

## Finalize tab holder
tabCtl.pack(expand=1, fill="both")

# Start main loop
window.mainloop()
