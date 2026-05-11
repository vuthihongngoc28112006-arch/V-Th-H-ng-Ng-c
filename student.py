from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root,text="Manage Student Details",font=("goudy old style", 20, "bold"),bg="#033054",fg="white")
        title.place(x=10, y=35, width=1180, height=35)

        self.var_student = StringVar()
        self.var_course = StringVar()
        self.var_roll = StringVar()
        self.var_desc=StringVar()

        Label(self.root,text="Student Name",font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=90)
        Label(self.root,text="Roll",font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=190)
        Label(self.root,text="Course",font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)     
        Label(self.root,text="Description",font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=240)

        self.txt_studentName = Entry(self.root,textvariable=self.var_student,font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_studentName.place(x=200, y=90, width=200)
        self.txt_course = Entry(self.root,textvariable=self.var_course,font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_course.place(x=200, y=140, width=200)
        self.txt_roll = Entry(self.root,textvariable=self.var_roll,font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=200, y=190, width=200)
        self.txt_description = Text(self.root,font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_description.place(x=200, y=240, width=500, height=100)

        Button(self.root,text="Save",font=("goudy old style", 15, "bold"),bg="#2196f3", fg="white",command=self.add).place(x=150, y=400, width=110, height=40)
        Button(self.root,text="Update",font=("goudy old style", 15, "bold"),bg="#4caf50", fg="white",command=self.update).place(x=270, y=400, width=110, height=40)
        Button(self.root,text="Delete",font=("goudy old style", 15, "bold"),bg="#f44336", fg="white",command=self.delete).place(x=390, y=400, width=110, height=40)
        Button(self.root,text="Clear",font=("goudy old style", 15, "bold"),bg="#607d8b", fg="white",command=self.clear).place(x=510, y=400, width=110, height=40)

        self.var_search=StringVar()
        Label(self.root,text="Student Name",font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=80)
        Entry(self.root,textvariable=self.var_search,font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=900, y=80, width=180)
        Button(self.root,text="Search",font=("goudy old style", 15, "bold"),bg="#03a9f4", fg="white",command=self.search).place(x=1080, y=80, width=100, height=30)

        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=130,width=470,height=300)

        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)

        self.StudentTable=ttk.Treeview(self.C_Frame,columns=("name","roll","course","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)

        self.StudentTable.heading("roll",text="Student ID")
        self.StudentTable.heading("name",text="Name")
        self.StudentTable.heading("course",text="Course")
        self.StudentTable.heading("roll",text="Roll")
        self.StudentTable.heading("description",text="Description")

        self.StudentTable["show"]="headings"
        self.StudentTable.pack(fill=BOTH,expand=1)
        self.StudentTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def clear(self):
        self.show()
        self.var_student.set("")
        self.var_course.set("")
        self.var_roll.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_studentName.config(state=NORMAL)

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_student.get()=="":
                messagebox.showerror("Error","Student Name required",parent=self.root)
            else:
                cur.execute("select * from student where name=?",(self.var_student.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Student already present",parent=self.root)
                else:
                    cur.execute("INSERT INTO student (name, course, roll, description) VALUES (?, ?, ?, ?)",(
                        self.var_student.get(),
                        self.var_course.get(),
                        self.var_roll.get(),
                        self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_student.get()=="":
                messagebox.showerror("Error","Student Name required",parent=self.root)
            else:
                cur.execute("""
                    update student 
                    set name=?, course=?, roll=?, description=? 
                    where cid=?
                    """,(
                        self.var_student.get(),
                        self.var_course.get(),
                        self.var_roll.get(),
                        self.txt_description.get("1.0", END),
                        self.var_id
                    ))
                con.commit()
                messagebox.showinfo("Success","Student Updated Successfully",parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_student.get()=="":
                messagebox.showerror("Error","Select Student",parent=self.root)
            else:
                cur.execute("delete from student where name=?",(self.var_student.get(),))
                con.commit()
                messagebox.showinfo("Delete","Student deleted",parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,ev):
        self.txt_studentName.config(state="readonly")
        r=self.StudentTable.focus()
        content=self.StudentTable.item(r)
        row=content["values"]
        self.var_id = self.StudentTable.item(r, "tags")[0]  

        self.var_student.set(row[0])
        self.var_course.set(row[1])
        self.var_roll.set(row[2])

        self.txt_description.delete("1.0", END)
        self.txt_description.insert(END, row[3])

    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("CREATE TABLE IF NOT EXISTS student (cid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,course TEXT,roll TEXT,description TEXT)")
            cur.execute("SELECT * FROM student ORDER BY cid ASC")
            rows=cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('', 'end', values=row[1:], tags=(row[0],))
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where name LIKE ?",('%'+self.var_search.get()+'%',))
            rows=cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('', END, values=row[1:], tags=(row[0],))
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
