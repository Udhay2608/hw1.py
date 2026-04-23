from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")

label_info = Label(root, text="This app multiplies two numbers.")
label_info.pack(pady=10)

label1 = Label(root, text="Enter first number:")
label1.pack()
entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Enter second number:")
label2.pack()
entry2 = Entry(root)
entry2.pack()

def calculate():
    n1 = int(entry1.get())
    n2 = int(entry2.get())
    result_box.delete("1.0", END)
    result_box.insert(END, str(n1 * n2))

button = Button(root, text="Calculate Product", command=calculate)
button.pack(pady=10)

result_box = Text(root, height=3, width=30)
result_box.pack()

root.mainloop()
