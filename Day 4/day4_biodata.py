from tkinter import *
from tkinter import ttk, messagebox

BG_COLOR = "#242424"
WHITE = "#fff"
FONT_FAMILY_AND_SIZE = "SegoeUI 12"

root = Tk()

root.geometry("600x600")
root.title("Biodata")
root.configure(bg=BG_COLOR)

name_label = Label(root, text="Name", font=FONT_FAMILY_AND_SIZE, bg=BG_COLOR, fg=WHITE, justify="left")
name_label.grid(row=0, column=0, padx=3, pady=1)

name_entry = Entry(root, width=20)
name_entry.grid(row=0, column=1, padx=3, pady=1)

age_label = Label(root, text="Age", font=FONT_FAMILY_AND_SIZE, bg=BG_COLOR, fg=WHITE)
age_label.grid(row=1, column=0, padx=3, pady=1)

age_list = [x for x in range(12, 99)]

selected_age = IntVar()
age_combo = ttk.Combobox(root, values=age_list, textvariable=selected_age)
age_combo.grid(row=1, column=1, padx=3, pady=1)

gender_label = Label(root, text="Gender", font=FONT_FAMILY_AND_SIZE, bg=BG_COLOR, fg=WHITE)
gender_label.grid(row=2, column=0, padx=5, pady=1)

selected_gender = StringVar()

gender_male = Radiobutton(root, text="Male", variable=selected_gender, value="Male")
gender_male.grid(row=2, column=1, padx=5, pady=1)

gender_female = Radiobutton(root, text="Female", variable=selected_gender, value="Female")
gender_female.grid(row=3, column=1, padx=5, pady=1)

hobbies_label = Label(root, text="Hobbies", font=FONT_FAMILY_AND_SIZE, bg=BG_COLOR, fg=WHITE)
hobbies_label.grid(row=5, column=0, padx=3)

hobby1_sel = IntVar()
hobby1 = Checkbutton(root, text="Reading books", variable=hobby1_sel)
hobby1.grid(row= 4, column=1)

hobby2_sel = IntVar()
hobby2 = Checkbutton(root, text="Programming", variable=hobby2_sel)
hobby2.grid(row= 5, column=1)

hobby3_sel = IntVar()
hobby3 = Checkbutton(root, text="Cooking", variable=hobby3_sel)
hobby3.grid(row= 6, column=1)

hobby4_sel = IntVar()
hobby4 = Checkbutton(root, text="Sports", variable=hobby4_sel)
hobby4.grid(row= 7, column=1)

description_label = Label(root, text="Description", font=FONT_FAMILY_AND_SIZE, bg=BG_COLOR, fg=WHITE)
description_label.grid(row=10, column=0, padx=3, pady=1)

description = Text(root, width=50, height=4)
description.grid(row=10, column=1)

submit = Button(root, text="Submit", font=FONT_FAMILY_AND_SIZE, width=10, height=1, command=lambda:compile_data())
submit.grid(row=12, column=1, padx=3, pady=10)

def compile_data():
    nametxt = name_entry.get()
    agetxt = selected_age.get()
    gendertxt = selected_gender.get()
    descriptiontxt = description.get("1.0", "end-1c")
    hobbytxt = ""

    if hobby1_sel.get() == 1:
        hobbytxt += " Reading books"

    if hobby2_sel.get() == 1:
        hobbytxt += " Programming"

    if hobby3_sel.get() == 1:
        hobbytxt += " Cooking"

    if hobby4_sel.get() == 1:
        hobbytxt += " Sports"

    message = f"Hi {nametxt}, {agetxt} years old - {gendertxt} {descriptiontxt} {hobbytxt}"
    messagebox.showinfo("success", message)


root.mainloop()