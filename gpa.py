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
        self.lbl_result = Label(self.root, text="GPA: ", font=("arial", 18, "bold"), bg="white", fg="blue")
        self.lbl_result.place(x=200, y=250)

    #fetch roll numbers
    def fetch_roll(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            for row in rows:
                self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", str(ex))
        finally:
            con.close()

    #convert % -> GPA(thang4)
    def percent_to_gpa(self, per):
        if per >= 85:
            return 4.0
        elif per >=80:
            return 3.5
        elif per >= 70:
            return 3.0
        elif per >= 60:
            return 2.5
        elif per >= 55:
            return 2.0
        elif per >= 40:
            return 1.0
        else:
            return 0.0


    #xep loai
    def classify(self, gpa):
        if gpa >=3.6:
            return "Xuat sac"
        elif gpa >= 3.2:
            return "gioi"
        elif gpa >= 2.5:
            return "Kha"
        elif gpa >= 2.0:
            return "Trung binh"
        else:
            return "Yeu"


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
                if row[0] is None or row[1] is None:
                    continue

                per = float(row[0])
                credit = int(row[1])

                gpa = self.percent_to_gpa(per)

                total_points += gpa * credit
                total_credits += credit
                
            final_gpa = total_points / total_credits if total_credits != 0 else 0

            rank =self.classify(final_gpa)

            self.lbl_result.config(
                text=f"GPA: {round(final_gpa, 2)} | Xep loai: {rank}"
            )

            messagebox.showinfo(
                "Ket qua",
                f"GPA: {round(final_gpa, 2)} \nXep loai: {rank}"
            )

        except Exception as ex:
            messagebox.showerror("Error", str(ex))
        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = GPAClass(root)
    root.mainloop()