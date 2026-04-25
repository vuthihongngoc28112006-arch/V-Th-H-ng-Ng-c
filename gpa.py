from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class GPAClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculate GPA")
        self.root.geometry("600x400+300+200")
        self.root.config(bg="white")


        #variables
        self.var_roll = StringVar()
        self.roll_list = []

        self.fetch_roll()

        #Title
        title = Label(self.root, text="Calculate Student GPA", font=("arial", 20, "bold"), bg="orange", fg = "black")
        title.pack(fill = X)

        #Selcet Student
        lbl_select = Label(self.root, text = "Select Student", font=("arial", 15), bg="white")
        lbl_select.place(x=50, y=80)

        self.cmb_roll = ttk.Combobox(
            self.root,
            textvariable = self.var_roll,
            values = self.roll_list,
            state="readonly",
            justify=CENTER,
            font=("arial", 13)
        )
        self.cmb_roll.place(x=220, y=80, width=200)
        self.cmb_roll.set("Select")
         
         #Button 
        btn_calc = Button(self.root, text="Calculate GPA",
                            font=("arial", 14, "bold"),
                            cursor="hand2",command=self.calculate_gpa)
        btn_calc.place(x=200, y=150, width=200, height=40)

        #resulf label
        self.lbl_resulf = Label(self.root, text="GPA: ", font=("arial", 18, "bold"), bg="white", fg="blue")
        self.lbl_resulf.place(x=200, y=250)