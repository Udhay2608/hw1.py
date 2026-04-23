from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Length Converter")

Label(root, text="Length Converter", font=("Arial", 16)).pack(pady=10)

Label(root, text="Enter value in centimeters:").pack()
entry_cm = Entry(root)
entry_cm.pack()

result_box = Text(root, height=4, width=30)
result_box.pack(pady=10)

def convert():
    cm = float(entry_cm.get())
    meters = cm / 100
    km = cm / 100000
    result_box.delete("1.0", END)
    result_box.insert(END, f"Meters: {meters}\nKilometers: {km}")

Button(root, text="Convert", command=convert).pack()

root.mainloop()
