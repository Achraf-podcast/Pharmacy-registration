from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

def exit2():
    confirm = messagebox.askyesnocancel("Pharmacy", "Confirm if you wanna to exit")
    if confirm:
        wind_registration.destroy()

def exit():
    confirm = messagebox.askyesnocancel("Pharmacy", "Confirm if you wanna exit")
    if confirm:
        wind.destroy()

def reset_registration():
    try:
        confirm = messagebox.askyesnocancel("Pharmacy", "Do you want to reset")
        if confirm:
            os.remove("Pharmacy_management\\pharmacy_database.db")
            open("Pharmacy_management\\pharmacy_database.db", "ab")
            wind_registration.destroy()
            registration()
    except:
        pass

def registration():
    global wind_registration
    try:
        def enter(data):
            list.delete(0, END)
            for i in data:
                for item in i:
                    list.insert(END, item)
    except:
        pass
                
    def update():
        try:
            file = open("Pharmacy_management\\pharmacy_database.db", "r").readlines()
            informations = []
            for i in file:
                a = i.split(", ")
                informations.append(a)
            return informations
        except:
            pass
    
    def receipt():
        a = en1.get()
        b = en2.get()
        c = en3.get()
        d = en4.get()
        e = en5.get()
        f = en6.get()
        g = en7.get()
        h = en8.get()
        i = en9.get()
        

        open("Pharmacy_management\\pharmacy_database.db", "ab").write(bytes(a + "    " + b + "   " + c + "   " + d + "   " + e + "   " + f + "   " + g + "   " + h + "   " + i + "\n", 'utf-8'))

        try:
            informations = update()
            enter(informations)
        except:
            pass
    
    try:
        wind.destroy()
    except:
        pass
    wind_registration = Tk()
    wind_registration.title('Patients registrations')

    Frame(wind_registration, width=1370, height=140, bd=20, relief='ridge').grid(row=0)
    Label(wind_registration, text='Patients registrations', font=('Calibri', 50), fg='#04c939').place(x=410, y=20)
    Frame(wind_registration, width=400, height=561, bd=20, relief='ridge').grid(row=1, sticky=W)
    Frame(wind_registration, width=970, height=561, bd=20, relief='ridge').place(x=400, y=140)

    Label(wind_registration, text='First name', font=('Calibri', 20)).place(x=20, y=190)
    Label(wind_registration, text='Second name', font=('Calibri', 20)).place(x=20, y=235)
    Label(wind_registration, text='Adress', font=('Calibri', 20)).place(x=20, y=280)
    Label(wind_registration, text='Post code', font=('Calibri', 20)).place(x=20, y=325)
    Label(wind_registration, text='Telephone', font=('Calibri', 20)).place(x=20, y=370)
    Label(wind_registration, text='Date', font=('Calibri', 20)).place(x=20, y=415)
    Label(wind_registration, text='Prove of id', font=('Calibri', 20)).place(x=20, y=460)
    Label(wind_registration, text='Type of member', font=('Calibri', 20)).place(x=20, y=505)
    Label(wind_registration, text='Method of payment', font=('Calibri', 20)).place(x=20, y=550)

    but = Button(wind_registration, text='Receipt', font=('Calibri', 15), bg='#64fa8c', width=35, command=receipt)
    but.place(x=20, y=638)
    but1 = Button(wind_registration, text='Reset', font=('Calibri', 15), bg='#64fa8c', width=45, command=reset_registration)
    but1.place(x=420, y=638)
    but2 = Button(wind_registration, text='Exit', font=('Calibri', 15), bg='#64fa8c', width=45, command=exit2)
    but2.place(x=887, y=638)

    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()
    t4 = StringVar()
    t5 = StringVar()
    t6 = StringVar()
    t7 = StringVar()
    t8 = StringVar()
    t9 = StringVar()

    en1 = Entry(wind_registration, textvariable=t1, fg='red')
    en1.place(x=250, y=203)
    en2 = Entry(wind_registration, textvariable=t2, fg='red')
    en2.place(x=250, y=247)
    en3 = Entry(wind_registration, textvariable=t3, fg='red')
    en3.place(x=250, y=291)
    en4 = Entry(wind_registration, textvariable=t4, fg='red')
    en4.place(x=250, y=335)
    en5 = Entry(wind_registration, textvariable=t5, fg='red')
    en5.place(x=250, y=379)
    en6 = Entry(wind_registration, textvariable=t6, fg='red')
    en6.place(x=250, y=423)
    en7 = ttk.Combobox(wind_registration, width=17, values=('Pilot license', 'Student Id', 'Passport', 'Driving license'), textvariable=t7)
    en7.place(x=250, y=467)
    en8 = ttk.Combobox(wind_registration, width=17, values=('Normal person', 'Employee', 'Business man', 'VIP'), textvariable=t8)
    en8.place(x=250, y=511)
    en9 = ttk.Combobox(wind_registration, width=17, values=('Mastercard', 'Paypal', 'Visa'), textvariable=t9)
    en9.place(x=250, y=559)
    
    list_frame = Frame(wind_registration, width=900, height=450)
    scroll_y = Scrollbar(list_frame, orient=VERTICAL)
    scroll_x = Scrollbar(list_frame, orient=HORIZONTAL)
    
    list = Listbox(list_frame, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    list.configure(foreground='red', font=('Calibri', 15), width=90, height=18)
    
    scroll_y.config(command=list.yview)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=list.xview)
    scroll_x.pack(side=BOTTOM, fill=X)
    list_frame.place(x=427, y=165)
    list.pack()

    try:
        informations = update()
        enter(informations)
    except:
        pass

    wind_registration.mainloop()

def login():
    username = en1.get()
    password = en2.get()

    if username == "admin" and password == "admin":
        b3.config(state=NORMAL, bg='#64fa8c')
        en1.config(state=DISABLED)
        en2.config(state=DISABLED)
    elif username == "" and password == "":
        messagebox.showerror('Pharmacy', 'please enter your details')
    else:
        messagebox.showerror('Pharmacy', 'This informations is incorrect')

def reset():
    s1.set("")
    s2.set("")

wind  = Tk()
wind.resizable(0, 0)
wind.title('Pharmacy management system')

l1 = Label(text='  Pharmacy management system  ', fg='#04c939', font=('Calibri', 50))
l1.grid(row=0)
l2 = Label(text='')
l2.grid(pady=20)
l3 = Frame(width=1010, height=300, bd=20, relief='ridge')
l3.grid(row=2)
l4 = Label(text='')
l4.grid(pady=5)
l5 = Frame(width=1000, height=100, bd=20, relief='ridge')
l5.grid(row=4)

b = Button(text='Login', bg='#04c939', font=("Calibri"), height=2, width=30, command=login)
b.grid(row=4, column=0, sticky=W, padx=50)
b1 = Button(text='Reset', bg='#04c939', font=("Calibri"), height=2, width=30, command=reset)
b1.grid(row=4, column=0)
b2 = Button(text='Exit', bg='#04c939', font=("Calibri"), height=2, width=30, command=exit)
b2.place(x=715, y=505)

s1 = StringVar()
s2 = StringVar()

Label(text='  Username  ', font=('Calibri', 50)).place(x=50, y=170)
Label(text='  Password  ', font=('Calibri', 50)).place(x=55, y=300)

en1 = Entry(wind, textvariable=s1, width=30, fg='red', font=('Calibri', 20))
en1.place(x=500, y=203)
en2 = Entry(wind, textvariable=s2, width=30, fg='red', show='*', font=('Calibri', 20))
en2.place(x=500, y=330)

l6 = Frame(width=600, height=90, bd=20, relief='ridge')
l6.grid()

b3 = Button(text='Patients registrations', font=("Calibri", 15), height=1, width=46, state=DISABLED, command=registration)
b3.place(x=265, y=605)

wind.mainloop()
