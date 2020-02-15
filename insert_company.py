from tkinter import messagebox
import mysql.connector
import tkinter
win = tkinter.Tk()        
win.title("Insert Company Details")
win.configure(width=win.winfo_screenwidth(),height=win.winfo_screenheight(),background="green")
tit=tkinter.Label(win,text="Insert Company Details",font=('Times',20))
tit.place(x="300",y="50")


def insertfun():    
    mydb = mysql.connector.connect(host="localhost",user="root",database="job",passwd="12345")
    mycursor=mydb.cursor()
    cn11=cn1.get()
    lc11=lc1.get()
    r111=r11.get()
    r211=r21.get()
    r311=r31.get()
    jr11=jr1.get()
    sal11=sal1.get()
    cp11=cp1.get()
    cn11=cn1.get()
    ph11=ph1.get()
    
    #mycursor.execute("insert into company (cname,location,req1,req2,req3,jobrole,salary,contactperson,phone)values('HP','KARUR','JAVA','PYTHON','PHP','FACULTY',12000,'GOWTHAMAN','9894083890'")
    mycursor.execute("insert into company (cname,location,req1,req2,req3,jobrole,salary,contactperson,phone)values('%s','%s','%s','%s','%s','%s',%d,'%s','%s')"%(cn11,lc11,r111,r211,r311,jr11,sal11,cp11,cn11,ph11))
    mydb.commit()
    messagebox.showinfo("Done","Data inserted successfully")
    




cn=tkinter.Label(win,text="Enter company name")
cn.place(x=200,y=100)

cn1=tkinter.Entry(win)
cn1.place(x=350,y=100)

lc=tkinter.Label(win,text="Enter Location name")
lc.place(x=200,y=150)

lc1=tkinter.Entry(win)
lc1.place(x=350,y=150)


r1=tkinter.Label(win,text="Enter requirement 1")
r1.place(x=200,y=200)

r11=tkinter.Entry(win)
r11.place(x=350,y=200)


r2=tkinter.Label(win,text="Enter requirement 2")
r2.place(x=200,y=250)

r21=tkinter.Entry(win)
r21.place(x=350,y=250)


r3=tkinter.Label(win,text="Enter requirement 3")
r3.place(x=200,y=300)

r31=tkinter.Entry(win)
r31.place(x=350,y=300)


jr=tkinter.Label(win,text="Enter job role:")
jr.place(x=200,y=350)

jr1=tkinter.Entry(win)
jr1.place(x=350,y=350)


sal=tkinter.Label(win,text="Enter salary:")
sal.place(x=200,y=400)


sal1=tkinter.Entry(win)
sal1.place(x=350,y=400)

cp=tkinter.Label(win,text="contact person")
cp.place(x=200,y=450)

cp1=tkinter.Entry(win)
cp1.place(x=350,y=450)

cn=tkinter.Label(win,text="Enter contact number")
cn.place(x=200,y=500)

cn1=tkinter.Entry(win)
cn1.place(x=350,y=500)


ph=tkinter.Label(win,text="Enter phone number")
ph.place(x=200,y=550)

ph1=tkinter.Entry(win)
ph1.place(x=350,y=550)

but=tkinter.Button(win,text="Insert/Save",command=insertfun)
but.place(x=350,y=600)

win.mainloop()
