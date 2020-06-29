import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Simwon QDP")
window.geometry("600x400")

tabCtl = ttk.Notebook(window)

tabAdd = tk.Frame(tabCtl)
tabCtl.add(tabAdd, text="Add Entry")
tabEdit = tk.Frame(tabCtl)
tabCtl.add(tabEdit, text="Edit Entry")

tabCtl.pack(expand=1, fill="both")

window.mainloop()
