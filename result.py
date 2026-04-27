from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3
class resultClass:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1200x550+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #title
        title=Label(self.root,text="Add Student Results", font=("arial", 20, "bold"), bg="orange", fg="#262626").place(x=10, y=15, width=1180, height =50) 
        #widgets
        #variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.var_credit = StringVar()
        self.roll_list=[]
        self.fetch_roll()
        

        lbl_select =Label(self.root, text="Select Student", font=("arial", 20, "bold"),bg="white").place(x=50, y=100)
        lbl_name= Label(self.root, text="Name",font=("arial", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course=Label(self.root,text="Course",font=("arial",20,"bold"), bg="white").place(x=50, y=220)
        lbl_makrs_ob = Label(self.root, text="Marks Obtained", font=("arial", 20, "bold"), bg="white").place(x=50,y=280)
        lbl_full_marks=Label(self.root, text="Full Marks", font=("arial", 20, "bold"), bg="white").place(x=50, y=340)
        lbl_credit = Label(self.root, text="Credit", font=("arial", 20, "bold"), bg="white")
        lbl_credit.place(x=50, y=400)
        self.lbl_gpa = Label(self.root, text="GPA: ", font=("arial", 18, "bold"), bg="white", fg="blue")
        self.lbl_gpa.place(x=650, y=470)


        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("arial", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_student.place(x=280,y=100,width=320, height=30)
        self.txt_student.set("Select")

        self.txt_student['values'] = self.roll_list
        btn_search=Button(self.root,text="Search", font=("arial",15,"bold"), bg="#03a9f4", fg="white",cursor="hand2",command=self.search).place(x=620,y=100,width=120,height=30)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("arial",20,"bold"),bg="lightyellow",state="readonly").place(x=280,y=160,width=320,height=30)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("arial",20,"bold"),bg="lightyellow",state="readonly").place(x=280,y=220,width=320,height=30)
        txt_marks=Entry(self.root,textvariable=self.var_marks,font=("arial",20,"bold"),bg="lightyellow").place(x=280,y=280,width=320,height=30)
        txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("arial",20,"bold"), bg="lightyellow").place(x=280,y=340,width=320,height=30)
        txt_credit=Entry(self.root, textvariable=self.var_credit, font=("arial", 20, "bold"), bg="lightyellow")
        txt_credit.place(x=280, y=400, width=320, height=30)

        #button
        btn_add=Button(self.root,text="Submit",font=("arial",15), bg="lightgreen", activebackground="lightgreen",cursor="hand2", command=self.add).place(x=280,y=450,width=140,height=40)
        btn_clear=Button(self.root,text="Clear",font=("arial",15), bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=440,y=450,width=140,height=40)
        # ===== TABLE HIEN THI MON DA NHAP =====
        self.table = ttk.Treeview(self.root, columns=("course","marks","full","credit"), show="headings")

        self.table.heading("course", text="Course")
        self.table.heading("marks", text="Marks")
        self.table.heading("full", text="Full")
        self.table.heading("credit", text="Credit")

        self.table.place(x=650, y=300, width=500, height=150)
        
        
        
        #image
        # self.bg_img=Image.open("images/result.png")
        # self.bg_img=self.bg_img.resize((250,150),Image.LANCZOS)
        # self.bg_img = ImageTk.PhotoImage(self.bg_img)

        # self.lbl_bg=Label(self.root,image=self.bg_img).place(x=800, y=1100)
#############################################################
    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows) >0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        finally:
            con.close()

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name, course from student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()

            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
                return

            # ===== XOA BANG CU =====
            for item in self.table.get_children():
                self.table.delete(item)

            # ===== LOAD LAI DU LIEU =====
            cur.execute(
                "SELECT course, marks_ob, full_marks, credit FROM result WHERE roll=?",
                (self.var_roll.get(),)
            )
            rows = cur.fetchall()

            for r in rows:
                self.table.insert("", END, values=r)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def percent_to_gpa(self, per):
        if per >= 85:
            return 4.0
        elif per >= 80:
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

    def classify(self, gpa):
        if gpa >= 3.6:
            return "Xuat sac"
        elif gpa >= 3.2:
            return "Gioi"
        elif gpa >= 2.5:
            return "Kha"
        elif gpa >= 2.0:
            return "Trung binh"
        else:
            return "Yeu"
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?", (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present", parent=self.root)
                else:
                    if self.var_marks.get()=="" or self.var_full_marks.get()=="" or self.var_credit.get()=="":
                        messagebox.showerror("Error","Please enter marks and credit", parent=self.root)
                        return

                    per = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                    cur.execute("insert into result (roll, name, course, marks_ob, full_marks, per , credit) values (?,?,?,?,?,?,?)",
            (
                self.var_roll.get(),
                self.var_name.get(),
                self.var_course.get(),
                self.var_marks.get(),
                self.var_full_marks.get(),
                str(per),
                int(self.var_credit.get())
            ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)

                    # ===== TINH GPA NGAY =====
                    cur.execute(
                        "SELECT per, credit FROM result WHERE roll=?",
                        (self.var_roll.get(),)
                    )
                    rows = cur.fetchall()

                    total_points = 0
                    total_credits = 0

                    for r in rows:
                        if r[0] is None or r[1] is None:
                            continue

                        per = float(r[0])
                        credit = int(r[1])

                        gpa = self.percent_to_gpa(per)

                        total_points += gpa * credit
                        total_credits += credit

                    final_gpa = total_points / total_credits if total_credits != 0 else 0

                    rank = self.classify(final_gpa)

                    # hien len man hinh
                    self.lbl_gpa.config(
                        text=f"GPA: {round(final_gpa,2)} | Xep loai: {rank}"
                    )

                    # them vao bang hien thi
                    self.table.insert("", END, values=(
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        self.var_credit.get()
                    ))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")
        self.var_credit.set("")
        # reset bảng
        for item in self.table.get_children():
            self.table.delete(item)

        # reset GPA
        self.lbl_gpa.config(text="GPA: ")


if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()