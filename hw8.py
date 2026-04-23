from tkinter import *
from datetime import date

root = Tk()
root.geometry("400x400")
root.title("Age Calculator App")

Label(root, text="Age Calculator", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

Label(root, text="Name:").grid(row=1, column=0, sticky="e")
name_entry = Entry(root)
name_entry.grid(row=1, column=1)

Label(root, text="Date:").grid(row=2, column=0, sticky="e")
date_entry = Entry(root)
date_entry.grid(row=2, column=1)

Label(root, text="Month:").grid(row=3, column=0, sticky="e")
month_entry = Entry(root)
month_entry.grid(row=3, column=1)

Label(root, text="Year:").grid(row=4, column=0, sticky="e")
year_entry = Entry(root)
year_entry.grid(row=4, column=1)

result_box = Text