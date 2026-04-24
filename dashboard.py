from tkinter import *
from PIL import Image,ImageTk
class RMS:
    def __init__(self, root):
        self.root= root
        self.root.title("student Result Management ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #title
        title= Label(self.root,text="Student Result Management System", font=("arial", 20,"bold"),bg="#033054",fg="white").place(x=0, y=0,relwidth=1,height=50)

        #menu 
        M_frame = LabelFrame(self.root,text="menu",font=("arial",15),bg="white")
        M_frame.place(x=10,y=70,width=1340,height=80)

        btn_student=Button(M_frame,text="Student",font=("arial",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=120,y=5,width=200,height=40)
        btn_result=Button(M_frame,text="Result",font=("arial",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=480,y=5,width=200,height=40)
        btn_report=Button(M_frame,text="Report",font=("arial",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)

        #content 
        self.bg_img=Image.open("images/bg.jpg")
        self.bg_img=self.bg_img.resize((920,350))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=200,y=200,width=920,height=350)
        

if __name__=="__main__":
    root = Tk()
    obj =RMS(root)
    root.mainloop()