import sqlite3
import tkinter
import tkinter.messagebox as tk
from tkinter.font import Font
from easygui import *
from tkinter import *
from turtle import *
import random

conn = sqlite3.connect('leaveDb.db')
cur = conn.cursor()

conn.execute("CREATE TABLE if not EXISTS balance (employee_id text,sickleave int,maternityleave int,emergencyleave int)")
conn.execute("CREATE TABLE if not EXISTS status (leave_id int,employee_id text,leave text,Date1 text,Date2 text,days int,status text)")
conn.execute('''CREATE TABLE if not Exists employee (employee_id text,Name text,ContactNumber text,Department text,Password text)''')
conn.execute('''CREATE TABLE if not Exists payroll(employee_id text,Name text,occupation text,Hire_date Date,annual_salary int, bonus int )''')
conn.execute("CREATE TABLE if not EXISTS attendence (employee_id text primary key, presence int, leaves int, FOREIGN KEY (employee_id) REFERENCES employee (employee_id))")

def AdminLogin():
    message = "Enter Username and Password"
    title = "Admin Login"
    fieldnames = ["Username", "Password"]
    field = []
    field = multpasswordbox(message, title, fieldnames)
    if field[0] == 'vidushi' and field[1] == '123456':
        tkinter.messagebox.showinfo("Admin Login", "Login Successfully")
        adminwindow()
    else:
        tk.showerror("Error info", "Incorrect username or password")

def EmployeeLogin():
    message = "Enter Employee ID and Password"
    title = "Employee Login"
    fieldnames = ["Employee ID", "Password"]
    field = []
    field = multpasswordbox(message, title, fieldnames)
    for row in conn.execute('SELECT employee_id,Password FROM employee'):
        if field[0] == row[0] and field[1] == row[1]:
            global login
            login = field[0]
            f = 1
            print("Success")
            tkinter.messagebox.showinfo("Employee Login", "Login Successfully")
            EmployeeLoginWindow()
            break
    if f!=1:
        print("Invalid")
        tk.showerror("Error info", "Incorrect employee id or password")

def Employeelogout():
    global login
    login = -1
    LoginWindow.destroy()
######################################
'''def deptname():
    dept = Toplevel()
    txt = Text(dept)
    cur.execute("SELECT distinct(department)FROM employee")
    row = cur.fetchall()
    print(row)
    s=len(row)
    d="Department:"
    for i in row:
        txt.insert(INSERT, d)
        txt.insert(INSERT,i[0])
        txt.insert(INSERT,'\n')
        for j in conn.execute('SELECT employee_id ,Name ,ContactNumber FROM employee where department=?', (i[0])):
            txt.insert(INSERT, j[0])
            txt.insert(INSERT, '\n')
            txt.insert(INSERT, j[1])
            txt.insert(INSERT, '\n')
            txt.insert(INSERT, j[3])

    txt.pack()

    #txt.pack()
'''
######################################
def EmployeeLeaveStatus():
    global leaveStatus
    leaveStatus = []
    for i in conn.execute('SELECT * FROM status where employee_id=?', (login,)):
        leaveStatus = i

    WindowStatus()


def EmployeeAllStatus():
    allStatus = Toplevel()
    txt = Text(allStatus)
    for i in conn.execute('SELECT * FROM status where employee_id=?', (login,)):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')

    txt.pack()


def EmployeeInformationWindow():
    employeeInformation = Toplevel()
    txt = Text(employeeInformation)
    for i in conn.execute('SELECT * FROM employee where employee_id=?', (login,)):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')

    txt.pack()


def EmployeeAllInformationWindow():
    allEmployeeInformation = Toplevel()
    txt = Text(allEmployeeInformation)
    for i in conn.execute('SELECT employee_id,Name,ContactNumber FROM employee'):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')

    txt.pack()


def WindowStatus():
    StatusWindow = Toplevel()
    label_1 = Label(StatusWindow, text="Employee ID=", fg="blue", justify=LEFT, font=("Calibri", 16))
    label_2 = Label(StatusWindow, text=leaveStatus[1], font=("Calibri", 16))
    label_3 = Label(StatusWindow, text="Type=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_4 = Label(StatusWindow, text=leaveStatus[2], font=("Calibri", 16))
    label_5 = Label(StatusWindow, text="start=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_6 = Label(StatusWindow, text=leaveStatus[3], font=("Calibri", 16))
    label_7 = Label(StatusWindow, text="end=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_8 = Label(StatusWindow, text=leaveStatus[4], font=("Calibri", 16))
    label_9 = Label(StatusWindow, text="Status:", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_10 = Label(StatusWindow, text=leaveStatus[6], font=("Calibri", 16))
    label_11 = Label(StatusWindow, text="leave_id:", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_12 = Label(StatusWindow, text=leaveStatus[0], font=("Calibri", 16))
    label_11.grid(row=0, column=0)
    label_12.grid(row=0, column=1)
    label_1.grid(row=1, column=0)
    label_2.grid(row=1, column=1)
    label_3.grid(row=2, column=0)
    label_4.grid(row=2, column=1)
    label_5.grid(row=3, column=0)
    label_6.grid(row=3, column=1)
    label_7.grid(row=4, column=0)
    label_8.grid(row=4, column=1)
    label_9.grid(row=5, column=0)
    label_10.grid(row=5, column=1)


def balance():
    global login
    #check = (login,)
    global balanced
    balanced = []
    for i in conn.execute('SELECT * FROM balance WHERE employee_id = ?', (login,)):
        balanced = i

    WindowBalance()


def WindowBalance():
    balanceWindow = Toplevel()
    label_1 = Label(balanceWindow, text="Employee ID=", fg="blue", justify=LEFT, font=("Calibri", 16))
    label_2 = Label(balanceWindow, text=balanced[0], font=("Calibri", 16))
    label_3 = Label(balanceWindow, text="Sick Leave=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_4 = Label(balanceWindow, text=balanced[1], font=("Calibri", 16))
    label_5 = Label(balanceWindow, text="Maternity Leave=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_6 = Label(balanceWindow, text=balanced[2], font=("Calibri", 16))
    label_7 = Label(balanceWindow, text="Emergency Leave=", fg="blue", font=("Calibri", 16), justify=LEFT)
    label_8 = Label(balanceWindow, text=balanced[3], font=("Calibri", 16))
    label_1.grid(row=0, column=0)
    label_2.grid(row=0, column=1)
    label_3.grid(row=1, column=0)
    label_4.grid(row=1, column=1)
    label_5.grid(row=2, column=0)
    label_6.grid(row=2, column=1)
    label_7.grid(row=3, column=0)
    label_8.grid(row=3, column=1)


def apply():
    message = "Enter the following details "
    title = "Leave Apply"
    fieldNames = ["Employee ID", "From", "To", "days"]
    fieldValues = []
    fieldValues = multenterbox(message, title, fieldNames)
    message1 = "Select type of leave"
    title1 = "Type of leave"
    choices = ["Sick leave", "Maternity leave", "Emergency leave"]
    choice = choicebox(message1, title1, choices)
    leaveid = random.randint(1, 1000)

    conn.execute("INSERT INTO status(leave_id,employee_id,leave,Date1,Date2,days,status) VALUES (?,?,?,?,?,?,?)",
                 (leaveid, fieldValues[0], choice, fieldValues[1], fieldValues[2], fieldValues[3], "Pending"))
    conn.commit()
###################################################################################################################
def attendencemark():
    message = "Enter the attendence details "
    title = "attendence"
    fieldNames = ["Employee ID"]
    fieldValues = []
    fieldValues = multenterbox(message, title, fieldNames)
    cur.execute("SELECT presence,leaves FROM attendence WHERE employee_id=?", (fieldValues[0],))
    row = cur.fetchall()
    print("row:",row)
    message1 = "mark attendence"
    title1 = "attendence"
    choices = ["Present","Absent"]
    choice = choicebox(message1, title1, choices)
    print("choice:",choice)
    present = row[0][0]
    leave = row[0][1]
    if choice == 'Present':
        present=present+1
    if choice == 'Absent':
        leave=leave+1
    conn.execute("update attendence set presence=? , leaves=? where employee_id=? ",(present,leave,fieldValues[0]))
    conn.commit()
    tkinter.messagebox.showinfo("Attendence","Attendence is marked!")
###################################################################################################################
def EmployeePayrollInformationWindow():
    allEmployeePayrollInformation = Toplevel()
    txt = Text(allEmployeePayrollInformation)
    for i in conn.execute('SELECT * FROM payroll'):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')

    txt.pack()
######################################################################################################################
def Employeepayroll():
    message = "Enter Details of Employee payroll details"
    title = "Payroll details"
    fieldNames = ["employee id","Employee name","occupation ","Hire date","Annual salary ", "bonus "]
    fieldValues = []
    fieldValues = multenterbox(message, title, fieldNames)
    #while 1:
     #   if fieldValues == None: break
      #  errmsg = ""
      #  for i in range(len(fieldNames)):
       #     if fieldValues[i].strip() == "":
        #        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])

        #if errmsg == "": break
    conn.execute("INSERT INTO payroll(employee_id ,Name ,occupation ,Hire_date ,annual_salary , bonus ) VALUES (?,?,?,?,?,?)",
                     (fieldValues[0], fieldValues[1], fieldValues[2], fieldValues[3], fieldValues[4],fieldValues[5]))

    tkinter.messagebox.showinfo("Employee Payroll", "payroll information updated successfully!")
    conn.commit()





def EditPayroll():
    message = "Enter the employee id"
    title = "update payroll"
    fieldNames = ["employee id", "Employee name", "occupation ", "Hire date", "Annual salary ", "bonus "]
    fieldValues = []
    fieldValues = multenterbox(message, title, fieldNames)
    cur.execute("SELECT * FROM employee WHERE employee_id =?", (fieldValues[0],))
    row = cur.fetchall()
    if not row:
        tkinter.messagebox.showinfo("Payroll update", "ID does not exist")
    else:
        conn.execute(
            "UPDATE payroll set Name=? ,occupation=? ,Hire_date=? ,annual_salary=? , bonus=? where employee_id=?",
            (fieldValues[1], fieldValues[2], fieldValues[3], fieldValues[4], fieldValues[5], fieldValues[0]))
        conn.commit()
        tkinter.messagebox.showinfo("Employee Payroll", "payroll information added successfully!")
######################################################################################################################
def editdetails():
    message = "Fill the details you want to change: "
    title = "Edit Details"
    fieldNames = ["Name", "Contact Number","Department","Password"]
    fieldValues = []
    fieldValues = multenterbox(message, title, fieldNames)
    conn.execute("update employee set Name=? ,ContactNumber=? ,Department= ? where employee_id=? ",(fieldValues[0],fieldValues[1],fieldValues[2],login))
    conn.commit()
    tkinter.messagebox.showinfo("Details", "Details are changed!")
###################################################################################################################
def seeattendence():
    employeeattendence = Toplevel()
    txt = Text(employeeattendence)
    cur.execute("SELECT presence,leaves FROM attendence WHERE employee_id=?", (login,))
    row = cur.fetchall()
    print(row)
    x1="total present: "
    x2="total absent: "
    x3="your attendence: "
    x4=row[0][0]+row[0][1]
    x5=(row[0][0]/x4)*100
    txt.insert(INSERT, x1)
    txt.insert(INSERT,row[0][0])
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, x2)
    txt.insert(INSERT, row[0][1])
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, x3)
    txt.insert(INSERT, x5)
    txt.pack()

###################################################################################################################
def LeaveApproval():
    message = "Enter leave_id"
    title = "leave approval"
    fieldNames = ["Leave_id"]
    fieldValues = []
    fieldValues = multenterbox(message, title, fieldNames)
    message1 = "Approve/Deny"
    title1 = "leave approval"
    choices = ["approve", "deny"]
    choice = choicebox(message1, title1, choices)

    conn.execute("UPDATE status SET status = ? WHERE leave_id= ?", (choice, fieldValues[0]))
    conn.commit()

    if choice == 'approve':
        print(0)
        cur.execute("SELECT leave FROM status WHERE leave_id=?", (fieldValues[0],))
        row = cur.fetchall()
        col = row

        for row in conn.execute("SELECT employee_id FROM status WHERE leave_id=?", (fieldValues[0],)):
            print(2)
            exampleId = row[0]

        for row in conn.execute("SELECT days FROM status WHERE leave_id=?", (fieldValues[0],)):
            print(2)
            exampleDays = row[0]

        for row in conn.execute("SELECT sickleave from balance where employee_id=?", (exampleId,)):
            balance = row[0]
            print(balance)

        for row in conn.execute("SELECT maternityleave from balance where employee_id=?", (exampleId,)):
            balance1 = row[0]
            print(balance1)

        for row in conn.execute("SELECT emergencyleave from balance where employee_id=?", (exampleId,)):
            balance2 = row[0]
            print(balance2)

        if (col[0] == ('sickleave',)):
            print(3)
            conn.execute("UPDATE balance SET sickleave =? WHERE employee_id= ?", ((balance - exampleDays), (exampleId)))

        if (col[0] == ('maternityleave',)):
            print(3)
            conn.execute("UPDATE balance SET maternityleave =? WHERE employee_id= ?", ((balance1 - exampleDays), (exampleId)))

        if (col[0] == ('emergencyleave',)):
            print(3)
            conn.execute("UPDATE balance SET emergencyleave =? WHERE employee_id= ?", ((balance2 - exampleDays), (exampleId)))



def leavelist():
    leavelistwindow = Toplevel()
    txt = Text(leavelistwindow)
    for i in conn.execute('SELECT * FROM status'):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')

    txt.pack()


def registration():
    message = "Enter Details of Employee"
    title = "Registration"
    fieldNames = ["Employee ID", "Name", "Contact Number","Department","Password"]
    fieldValues = []
    fieldValues = multpasswordbox(message, title, fieldNames)
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])

        if errmsg == "": break


        fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
    cur.execute("SELECT * FROM employee WHERE employee_id =?", (fieldValues[0],))
    row = cur.fetchall()
    if not row:
        conn.execute("INSERT INTO employee(employee_id,Name,ContactNumber,Department,Password) VALUES (?,?,?,?,?)",
                     (fieldValues[0], fieldValues[1], fieldValues[2], fieldValues[3], fieldValues[4]))
        conn.execute("INSERT INTO balance(employee_id,sickleave,maternityleave,emergencyleave) VALUES (?,?,?,?)",
                     (fieldValues[0], 12, 12, 50))
        conn.execute("INSERT INTO attendence(employee_id,presence,leaves) VALUES (?,?,?)",
                     (fieldValues[0], 0,0))
        tkinter.messagebox.showinfo("Employee Registeration", "Registered successfully!")
        conn.commit()
    else:
        tkinter.messagebox.showinfo("Employee Registeration","Please change your employee Id, it is already been assigned!")


def EmployeeLoginWindow():
    # employee login window after successful login
    global LoginWindow
    LoginWindow = Toplevel()
    LoginWindow.wm_attributes('-fullscreen', '1')
    Background_Label = Label(LoginWindow, image=filename)
    Background_Label.place(x=0, y=0, relwidth=1, relheight=1)

    informationEmployee = Button(LoginWindow, text='Employee information', command=EmployeeInformationWindow, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    informationEmployee['font'] = BtnFont
    informationEmployee.pack(fill=X)
    ##########################################################
    attendenceEmployee = Button(LoginWindow, text='Employee attendence', command=seeattendence, bd=12,
                                 relief=GROOVE, fg="blue", bg="#ffffb3",
                                 font=("Calibri", 36, "bold"), pady=3)
    attendenceEmployee['font'] = BtnFont
    attendenceEmployee.pack(fill=X)
    ##########################################################
    editEmployee = Button(LoginWindow, text='Edit Your Details Here', command=editdetails, bd=12,
                                relief=GROOVE, fg="blue", bg="#ffffb3",
                                font=("Calibri", 36, "bold"), pady=3)
    editEmployee['font'] = BtnFont
    editEmployee.pack(fill=X)
    ##########################################################
    submit = Button(LoginWindow, text='Submit Leave', command=apply, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    submit['font'] = BtnFont
    submit.pack(fill=X)

    LeaveBalance = Button(LoginWindow, text='Leave Balance', command=balance, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    LeaveBalance['font'] = BtnFont
    LeaveBalance.pack(fill=X)

    LeaveApplicationStatus = Button(LoginWindow, text='Last leave status', command=EmployeeLeaveStatus, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    LeaveApplicationStatus['font'] = BtnFont
    LeaveApplicationStatus.pack(fill=X)

    AllLeaveStatus = Button(LoginWindow, text='All leave status', command=EmployeeAllStatus, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    AllLeaveStatus['font'] = BtnFont
    AllLeaveStatus.pack(fill=X)


    LogoutBtn = Button(LoginWindow, text='Logout', bd=12, relief=GROOVE, fg="red", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3, command=Employeelogout)
    LogoutBtn['font'] = BtnFont
    LogoutBtn.pack(fill=X)

    informationEmployee.pack()
    submit.pack()
    LeaveBalance.pack()
    LeaveApplicationStatus.pack()
    AllLeaveStatus.pack()
    LogoutBtn.pack()
    ExitBtn.pack()



def adminwindow():
    adminmainwindow = Toplevel()
    adminmainwindow.wm_attributes('-fullscreen', '1')
    Background_Label = Label(adminmainwindow, image=filename)

    Background_Label.place(x=0, y=0, relwidth=1, relheight=1)
    informationEmployee = Button(adminmainwindow, text='All Employee information', command=EmployeeAllInformationWindow, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    informationEmployee['font'] = BtnFont
    informationEmployee.pack(fill=X)



    LeaveListButton = Button(adminmainwindow, text='Leave approval list', command=leavelist, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    LeaveListButton['font'] = BtnFont
    LeaveListButton.pack(fill=X)

    ApprovalButton = Button(adminmainwindow, text='Approve leave', command=LeaveApproval, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    ApprovalButton['font'] = BtnFont
    ApprovalButton.pack(fill=X)
    ####################################################################################################################
    PayrollButton = Button(adminmainwindow, text='Payroll information', command=Employeepayroll, bd=12, relief=GROOVE,
                           fg="blue", bg="#ffffb3",
                           font=("Calibri", 36, "bold"), pady=3)
    PayrollButton['font'] = BtnFont
    PayrollButton.pack(fill=X)

    informationPayroll = Button(adminmainwindow, text='All Employee payroll information',
                                command=EmployeePayrollInformationWindow,
                                bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                                font=("Calibri", 36, "bold"), pady=3)
    informationPayroll['font'] = BtnFont
    informationPayroll.pack(fill=X)

    EditPayrollinformation = Button(adminmainwindow, text='Edit payroll information', command=EditPayroll,
                                    bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                                    font=("Calibri", 36, "bold"), pady=3)
    EditPayrollinformation['font'] = BtnFont
    EditPayrollinformation.pack(fill=X)
    ####################################################################################################################

    ##########################
    DeptListButton = Button(adminmainwindow, text='Mark Attendence', command=attendencemark, bd=12, relief=GROOVE,
                            fg="blue", bg="#ffffb3",
                            font=("Calibri", 36, "bold"), pady=3)
    DeptListButton['font'] = BtnFont
    DeptListButton.pack(fill=X)
    ###########################
    LogoutBtn = Button(adminmainwindow, text='Logout', command=adminmainwindow.destroy, bd=12, relief=GROOVE, fg="red",
                     bg="#ffffb3",
                     font=("Calibri", 36, "bold"), pady=3)
    LogoutBtn['font'] = BtnFont
    LogoutBtn.pack(fill=X)

    informationEmployee.pack()
    LeaveListButton.pack()
    ApprovalButton.pack()
    ExitBtn.pack()


root = Tk()

root.wm_attributes('-fullscreen', '1')
root.title("Employee Management System")
root.iconbitmap(default='leavelogo.ico')
filename = PhotoImage(file="login.gif")
background_label = Label(root, bg="#f4e9e8")
background_label.place(x=1, y=1, relwidth=1, relheight=1)
BtnFont = Font(family='Calibri(Body)', size=20)
MainLabel = Label(root, text="Employee Management System", bd=12, relief=GROOVE, fg="White", bg="blue",
                      font=("Calibri", 36, "bold"), pady=20,padx=20)
MainLabel.pack(fill=X)
im = PhotoImage(file='login.gif')

AdminLgnBtn = Button(root, text='Admin login',  bd=12, relief=GROOVE, fg="blue", bg="#ccc2cb",
                      font=("Calibri", 36, "bold"), pady=3,padx=10,width=10, command=AdminLogin)
AdminLgnBtn['font'] = BtnFont
AdminLgnBtn.pack(fill=X)


LoginBtn = Button(root, text='Employee login', bd=12, relief=GROOVE, fg="blue", bg="#ccc2cb",
                      font=("Calibri", 36, "bold"), pady=3, command=EmployeeLogin)
LoginBtn['font'] = BtnFont
LoginBtn.pack(fill=X)


EmployeeRegistration = Button(root, text='Employee registration', command=registration, bd=12, relief=GROOVE, fg="blue", bg="#ccc2cb",
                      font=("Calibri", 36, "bold"), pady=3)
EmployeeRegistration['font'] = BtnFont
EmployeeRegistration.pack(fill=X)

ExitBtn = Button(root, text='Exit', command=root.destroy, bd=12, relief=GROOVE, fg="red", bg="#ccc2cb",
                      font=("Calibri", 36, "bold"), pady=3)
ExitBtn['font'] = BtnFont
ExitBtn.pack(fill=X)
MainLabel.pack()
AdminLgnBtn.pack()
LoginBtn.pack()
EmployeeRegistration.pack()
ExitBtn.pack()


root.mainloop()
