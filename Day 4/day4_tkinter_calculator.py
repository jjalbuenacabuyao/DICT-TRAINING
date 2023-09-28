from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#242424")

entry = Entry(root, font="SegoeUI 20", justify=RIGHT)
entry.grid(row=0, column=0, columnspan=3, pady=10, padx=4)


button1 = Button(root, text="1", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("1"))
button1.grid(row=1, column=0, padx=2, pady=10)

button2 = Button(root, text="2", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("2"))
button2.grid(row=1, column=1, padx=2, pady=10)

button3 = Button(root, text="3", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("3"))
button3.grid(row=1, column=2, padx=2, pady=10)

button_plus = Button(root, text="+", font="SegoeUI 14", width=6, height=3, command=lambda:operator_select("+"))
button_plus.grid(row=1, column=3, padx=2, pady=10)

button4 = Button(root, text="4", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("4"))
button4.grid(row=2, column=0, padx=2, pady=10)

button5 = Button(root, text="5", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("5"))
button5.grid(row=2, column=1, padx=2, pady=10)

button6 = Button(root, text="6", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("6"))
button6.grid(row=2, column=2, padx=2, pady=10)

button_minus = Button(root, text="-", font="SegoeUI 14", width=6, height=3, command=lambda:operator_select("-"))
button_minus.grid(row=2, column=3, padx=2, pady=10)

button7 = Button(root, text="7", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("7"))
button7.grid(row=3, column=0, padx=2, pady=10)

button8 = Button(root, text="8", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("8"))
button8.grid(row=3, column=1, padx=2, pady=10)

button9 = Button(root, text="9", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("9"))
button9.grid(row=3, column=2, padx=2, pady=10)

button_multiply = Button(root, text="x", font="SegoeUI 14", width=6, height=3, command=lambda:operator_select("*"))
button_multiply.grid(row=3, column=3, padx=2, pady=10)

button_point = Button(root, text=".", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("."))
button_point.grid(row=4, column=0, padx=2, pady=10)

button0 = Button(root, text="0", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("0"))
button0.grid(row=4, column=1, padx=2, pady=10)

button_equals = Button(root, text="=", font="SegoeUI 14", width=6, height=3, command=lambda:calculate())
button_equals.grid(row=4, column=2, padx=2, pady=10)

button_divide = Button(root, text="/", font="SegoeUI 14", width=6, height=3, command=lambda:num_display("/"))
button_divide.grid(row=4, column=3, padx=2, pady=10)


def num_display(value: str):
    current = entry.get()
    entry.insert(0, value)
    entry.delete(0, END)
    new = current + value
    entry.insert(0, new)
    

def operator_select(opr):
    global firstnum
    global operator
    operator = opr
    firstnum = float(entry.get())
    entry.delete(0, END)


def calculate():
    second_num = float(entry.get())
    entry.delete(0, END)
    answer = 0
    if operator == "+":
        answer = firstnum + second_num
    elif operator == "-":
        answer = firstnum - second_num
    elif operator == "*":
        answer = firstnum * second_num
    elif operator == "/":
        answer = firstnum / second_num
    
    if str(answer).endswith(".0"):
        splitted = str(answer).split(".")
        answer = splitted[0]

    entry.insert(0, answer)

root.mainloop()