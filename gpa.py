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

    #fetch roll numbers







    #Calculate GPA
    def calculate_gpa(self):
        if self.var_roll.get() =="Select":
            messagebox.showerror("Error", "Please select student")
            return 

            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            try:
                cur.execute(
                    "SELECT per, credit FROM result WHERE roll=?",
                    (self.var_roll.get(),)
                )
                rows = cur.fetchall()

                if len(rows) == 0:
                    messagebox.showerror("Error", "No result found")
                    return 

                total_points = 0
                total_credits = 0

                for row in rows:
                    per = float(row[0])
                    credit = int(row[1])

                    gpa = self.percent_to_gpa(per)

                    total_points += gpa * credit
                    total_credits += credit
                
                final_gpa = total_point / total_credits if total_credits != 0 else 0

                self.lbl_result.config(text=f"GPA: {round(finaal_gpa, 2)}")

            except Exception as ex:
                messagebox.showerror("Error", str(ex))
            finally:
                con.close()


if __name__ = "__main__":
    root = Tk()
    obj = GPAClass(root)
    root.mainloop()