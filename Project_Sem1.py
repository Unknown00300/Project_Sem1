import tkinter as tk
from functools import partial
import mysql.connector as msc
from tkinter import *


def user_ver(status, username, password):
    u = username.get()
    p = password.get()

    con = msc.connect(host='localhost', user='root', passwd='onkar123', database='pyproject')
    cur = con.cursor()
    sql = "select * from staff where First_Name = '{0}' AND Emp_code = '{1}' ;".format(u, p)

    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) == 0:
        status = False
    else:
        status = True
    Open_New_Window(status, rows)
    return


def Adding_patient():
    win = Tk()
    win.geometry('1920x1080')
    win.title("PATIENT UPDATE PAGE ")

    label1 = Label(win, text="STAFF PROFILE AND PATIENT INFORMATION ", font=("Arial", 32, "bold"), border=10,
                   relief=GROOVE, bg="lightgrey", fg="blue")
    label1.grid(row=0, column=0, columnspan=4, padx=75)

    # -------ENTRIES------#

    patient_name = Label(win, text="PATIENT NAME :", font=('Arial', 17, "bold"), bg="lightgrey", fg="blue")
    patient_name.grid(row=1, column=0, pady=15)

    patient_ent = Entry(win, bd=12, font=("Arial", 12), width=25)
    patient_ent.grid(row=1, column=1)
    # just get how to post a dateonce
    date = Label(win, text="DATE WHEN ADMITTED :", font=('Arial', 17, 'bold'), bg='lightgrey', fg='blue')
    date.grid(row=1, column=2, pady=15)

    date_ent = Entry(win, bd=12, font=("Arial", 12), width=25)
    date_ent.grid(row=1, column=3)

    code_pat_lab = Label(win, text="PATIENT CODE", font=('Arial', 17, 'bold'), bg='lightgrey', fg='blue')
    code_pat_lab.grid(row=2, column=0, pady=15)

    code_entry = Entry(win, bd=12, font=("Arial", 12), width=25)
    code_entry.grid(row=2, column=1)

    presc = Label(win, text='PRESCRIPTION CODE', font=('Arial', 17, 'bold'), bg='lightgrey', fg='blue')
    presc.grid(row=4, column=0, pady=15)

    presc_box = Entry(win, bd=12, font=("Arial", 12), width=25)
    presc_box.grid(row=4, column=1)

    age = Label(win, text='AGE OF THE PATIENT', font=('Arial', 17, 'bold'), bg='lightgrey', fg='blue')
    age.grid(row=2, column=2, pady=15)

    cond = [
        "0-3",
        "3-12",
        "12-18",
        "18-45",
        "45-60",
        ">60"
    ]

    sup = StringVar()
    sup.set(cond[0])

    age_box = OptionMenu(win, sup, *cond)
    age_box.grid(row=2, column=3)

    bed = Label(win, text="BED ASSIGNED TO PATIENT", font=('Arial', 17, "bold"), bg="lightgrey", fg="blue")
    bed.grid(row=3, column=0, pady=15)

    bed_ent = Entry(win, bd=12, font=("Arial", 12), width=25)
    bed_ent.grid(row=3, column=1)

    name = Label(win, text="DOCTOR ASSIGNED", font=('Arial', 17, "bold"), bg="lightgrey", fg="blue")
    name.grid(row=3, column=2, pady=15)

    name_ent = Entry(win, bd=12, font=("Arial", 12), width=25)
    name_ent.grid(row=3, column=3)

    phone = Label(win, text="PATIENT PHONE NUM", font=('Arial', 17, "bold"), bg="lightgrey", fg="blue")
    phone.grid(row=5, column=0, pady=15)

    phone_ent = Entry(win, bd=12, font=("Arial", 12), width=25)
    phone_ent.grid(row=5, column=1)

    guard = Label(win, text="GUARDIAN PHONE NUM", font=('Arial', 17, "bold"), bg="lightgrey", fg="blue")
    guard.grid(row=5, column=2, pady=15)

    guard_ent = Entry(win, bd=12, font=("Arial", 12), width=25)
    guard_ent.grid(row=5, column=3)

    address = Label(win, text="ADDRESS OF THE PATIENT", font=('Arial', 17, "bold"), bg="lightgrey", fg="blue")
    address.grid(row=6, column=0, pady=15)

    address_ent = Entry(win, bd=12, font=("Arial", 12), width=25)
    address_ent.grid(row=6, column=1)

    insurance = Label(win, text="INSURANCE APPLICABLE", font=('Arial', 17, "bold"), bg="lightgrey", fg="blue")
    insurance.grid(row=6, column=2, pady=15)

    insur = [
        "STATE BANK OF INDIA",
        "HDFC BANK",
        "CANARA BANK",
        "PUNJAB BANK",
        "WORLD BANK",
        "ICICI BANK",
        "YES BANK",
        "UICOO BANK",
        "NONE"
    ]
    insuran = StringVar()
    insuran.set(insur[0])

    insurance_box = OptionMenu(win, insuran, *insur)
    insurance_box.grid(row=6, column=3)

    gender = Label(win, text='GENDER OF PATIENT', font=('Arial', 17, 'bold'), bg='lightgrey', fg='blue')
    gender.grid(row=4, column=2, pady=15)

    email = Label(win, text="EMAIL OF THE PATIENT", font=('Arial', 17, "bold"), bg="lightgrey", fg="blue")
    email.grid(row=7, column=0, pady=15)

    email_ent = Entry(win, bd=12, font=("Arial", 12), width=25)
    email_ent.grid(row=7, column=1)

    email1 = Label(win, text="EMAIL OF THE GUARDIAN", font=('Arial', 17, "bold"), bg="lightgrey", fg="blue")
    email1.grid(row=7, column=2, pady=15)

    email_ent1 = Entry(win, bd=12, font=("Arial", 12), width=25)
    email_ent1.grid(row=7, column=3)

    gend = [
        "MALE",
        "FEMALE",
        "OTHER"
    ]

    holo = StringVar()
    holo.set(gend[0])

    gend_box = OptionMenu(win, holo, *gend)
    gend_box.grid(row=4, column=3)

    def submit():
        con = msc.connect(host='localhost', user='root', passwd='onkar123', database='pyproject')
        cur = con.cursor()
        # "INSERT into patients (Code,Name,Age,gender,Doc_code,Prescription_code,Bed_Assigned,Entry,Insurance,Patient_Ph.no,Patient_Address,Patient_Email,Guardian_Ph.no,Guardian_Email) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(code_entry.get(),patient_ent.get(),sup.get(),holo.get(),name_ent.get(),presc_box.get(),bed_ent.get(),date_ent.get(),insuran.get(),phone_ent.get(),address_ent.get(),email_ent.get(),guard_ent.get(),email_ent1.get())
        sql1 = "INSERT into patients (Code,Name,Age,gender,Doc_code,Prescription_code,Entry,Insurance,Bed_Assigned,Patient_phone,Patient_Address,Patient_Email,Guardian_phone,Guardian_Email) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(code_entry.get(), patient_ent.get(), sup.get(), holo.get(), name_ent.get(), presc_box.get(), date_ent.get(),insuran.get(), bed_ent.get(), phone_ent.get(), address_ent.get(), email_ent.get(), guard_ent.get(),email_ent1.get())
        cur.execute(sql1)
        con.commit()
        return

    def cancel():
        return win.destroy()

    button1 = Button(win, text="SUBMIT AND SAVE", bg="green", fg="white", padx=0, pady=0, font=("Arial", 20, "bold"),border=5, command=submit)
    button3 = Button(win, text="QUIT OR LEAVE ", bg="green", fg="white", padx=0, pady=0, font=("Arial", 20, "bold"),border=5, command=cancel)

    button1.grid(row=12, column=0, pady=30)
    button3.grid(row=12, column=3, pady=30, padx=50, columnspan=2)

    # -------ENTRIES------#

    label10 = Label(win, text="FOR ANY QUERIES PLZ CONTACT THE PHONE NUMBER 9877238478,9876532863",font=("Arial", 19, "bold"), bg="lightgrey", fg="blue")
    label10.grid(row=13, column=0, columnspan=3)


def billing_page(p_code):

    con = msc.connect(host='localhost', user='root', passwd='onkar123', database='pyproject')
    cur = con.cursor()

    sql6 = "select p.dosage*m.cost from prescription p, medicine m where (p.Med_Name=m.Med_name) and p.Patient_No='P003';"
    cur.execute(sql6)
    Med_Lab = str(cur.fetchall()[0][0])    
    
    bill = Toplevel()
    # In the patients table the duration of stay will be added then the patient code is entered here and the exit is changed from n to y
    # The main labels

    bill.geometry('1920x1080')

    First = bill.title("Billing Page")

    bill_label = Label(bill, text="PAYMENT AND BILLING SECTION", font=("Arial", 40, "bold"), border=10, relief=GROOVE,bg="lightgrey", fg="blue")
    bill_label.grid(row=0, column=0, columnspan=5, padx=50, pady=25)

    intro_label = Label(bill, text='-----------Thank you for your stay!----------', font=('Arial', 30, 'bold'),bg='lightgrey', fg='blue')
    intro_label.grid(row=1, column=4, columnspan=5, pady=30)

    patient_details = Label(bill, text='Patient code:', font=('Arial', 30, 'bold'), bg='lightgrey', fg='blue')
    patient_details.grid(row=3, column=3, columnspan=2, pady=30)

    # doc_name = Label(bill,text = 'Treated by:')
    # doc_name.grid(row = 4, column = 3)

    meds_cost = Label(bill, text='Cost of medicines:', font=('Arial', 30, 'bold'), bg='lightgrey', fg='blue')
    meds_cost.grid(row=5, column=3, columnspan=2, pady=30)

    outro = Label(bill, text='----------HAPPY RECOVERY!----------', font=('Arial', 30, 'bold'), bg='lightgrey',fg='blue').grid(row=12, column=4, columnspan=5, pady=30)

    P_code = p_code.get()
    P_code_var = Label(bill, text=P_code,font=('Arial', 30, 'bold'), bg='lightgrey', fg='blue')
    P_code_var.grid(row=3, column=6)

    Meds_label = Label(bill, text= Med_Lab,font=('Arial', 30, 'bold'), bg='lightgrey', fg='blue')
    Meds_label.grid(row=5, column=6)

    sql5 = "SELECT Doc_code from patients where Code = '{0}' ".format(p_code.get())
    res1 = cur.execute(sql5)
    res1.fetchall()
    lst = [x[0] for x in res1]
    doc = lst[0][0]

    #doc = StringVar()
    #doc_var = Label(bill, text=doc)
    #doc_var.grid(row=4, column=4)

    bill.mainloop()


def Edit_page_for_docs(d_code, p_code):
    ep = Toplevel()
    ep.title("Doctor's Editing Page")
    ep.geometry('1920x1080')

    doc_label = Label(ep, text="THE PATIENT EVALUATION PAGE FOR DOCTORS", font=("Arial", 40, "bold"), border=10,relief=GROOVE, bg="lightgrey", fg="blue")
    doc_label.grid(row=0, column=0, columnspan=4, padx=50, pady=25)

    P_code_label = Label(ep, text='Patient code:', font=('Arial', 23, "bold"), bg="lightgrey", fg="blue")
    P_code_label.grid(row=1, column=1, pady=15)

    P_code_display = Label(ep, text=p_code.get(), font=('Arial', 23, "bold"), bg="lightgrey", fg="blue")
    P_code_display.grid(row=1, column=2, pady=15)

    # Further scope: The page can display the number of visits the paitent has had from the doc and the meds previously prescribed

    Med_name = Label(ep, text='Select Medicine prescribed', font=('Arial', 23, "bold"), bg="lightgrey", fg="blue")
    Med_name.grid(row=2, column=1, pady=15)

    Med_Option = ['COUGHSYRUP', 'VICODIN', 'REMEDISIVER', 'ALBUEROL', 'LISINOPRIL', 'GABAPENTIN', 'METFORMIN','LIPITOR',
                  'MDMN', 'AMLODIPINE', 'PARACETAMOL', 'LEVOTHYROXINE']
    Med_value = StringVar()
    Med_value.set("Select medicine")
    Med_menu = OptionMenu(ep, Med_value, *Med_Option)
    Med_menu.grid(row=2, column=2, columnspan=1)

    quantity = Label(ep, text='Enter the quantity', font=('Arial', 23, "bold"), bg="lightgrey", fg="blue")
    quantity.grid(row=3, column=1, pady=15)
    dosage = Label(ep, text='Enter the dosage', font=('Arial', 23, "bold"), bg="lightgrey", fg="blue")
    dosage.grid(row=4, column=1, pady=15)

    quantity_list = [100, 200, 300, 500, 650]
    quantity_var = IntVar()
    quantity_var.set('Quantity in mg')
    quantity_menu = OptionMenu(ep, quantity_var, *quantity_list)
    quantity_menu.grid(row=3, column=2, columnspan=1)

    dosage_list = [1, 2, 3, 4, 5, 6]
    dosage_var = IntVar()
    dosage_var.set('No. of days')
    dose_menu = OptionMenu(ep, dosage_var, *dosage_list)
    dose_menu.grid(row=4, column=2, columnspan=1, ipadx=15)

    Exit_label = Label(ep, text='Date of exit', font=('Arial', 23, "bold"), bg="lightgrey", fg="blue")
    Exit_label.grid(row=6, column=1, pady=15)
    exit_entry = Entry(ep, bd=12, font=("Arial", 15), width=25)
    exit_entry.grid(row=6, column=2, )

    His_label = Label(ep, text='History', font=('Arial', 23, "bold"), bg="lightgrey", fg="blue")
    His_label.grid(row=5, column=1, pady=15)
    His_box = Entry(ep, bd=12, font=("Arial", 15), width=60)
    His_box.grid(row=5, column=2,)

    def Go_billing():
        con = msc.connect(host='localhost', user='root', passwd='onkar123', database='pyproject')
        cur = con.cursor()

        sql4 = "UPDATE patients SET Date_of_Exit= '{0}' where Code = '{1}'".format(exit_entry.get(),p_code.get())
        cur.execute(sql4)
        con.commit()

        billing_page(p_code)

    Billing_Button = Button(ep, text='BILLING PAGE', bg="green", fg="white", font=("Arial", 20, "bold"), border=5,command=Go_billing)
    Billing_Button.grid(row=7, column=1)

    def Save_and_commit():
        con = msc.connect(host='localhost', user='root', passwd='onkar123', database='pyproject')
        cur = con.cursor()

        sql2 = "INSERT into prescription (Patient_No,Med_Name,Quantity,Dosage) VALUES('{0}','{1}','{2}','{3}')".format(
            p_code.get(), Med_value.get(), quantity_var.get(), dosage_var.get())
        cur.execute(sql2)

        sql3 = "INSERT into patients (History) VALUES ('{0}') WHERE Code = '{1}'".format(His_box.get(), p_code.get())
        cur.execute(sql3)

        con.commit()
        return

    Save_button = Button(ep, text='SAVE AND SUBMIT', bg="red", fg="white", font=("Arial", 20, "bold"), border=5)
    Save_button.grid(row=7, column=2, pady=25)

    ep.mainloop()


def Open_New_Window(status, rows):
    if status:
        root.destroy()
        posn = rows[0][3]
        if posn == 'Staff':
            Adding_patient()
        else:
            choose_patient(rows)
    else:
        new = Toplevel(root)
        new.title("Error Page")
        new.geometry("1920x1080")
        Label(new, text="ERROR WHILE LOGIN\nYou are attempting to use an unauthorised login.\nThis incident has been reported to the relevant authorities.\nPlz try again or contact Administrator -9837276362.",font=("Arial",35,"bold"),border=18,relief=GROOVE,bg="lightgrey",fg="blue").pack()


def choose_patient(doc_info):
    global p_code
    global doc_code
    global Choose_var

    uno = Tk()
    uno.geometry('1920x1080')

    decide = Label(uno,text="NUMBER OF PATIENTS ASSIGNED TO THE DOCTOR",font=("Arial", 40, "bold"), border=10,relief=GROOVE, bg="lightgrey", fg="blue")
    decide.grid(row=0, column=3, columnspan=5, padx=20, pady=50)

    doc_name = doc_info[0][1]
    doc_code = doc_info[0][0]

    Pat_code_list = Patient_list_for_doc(doc_code)

    Choose_var = StringVar()
    Choose_var.set('Choose Patient code')

    Choose_menu = OptionMenu(uno, Choose_var, *Pat_code_list)
    Choose_menu.grid(row=1,column=3,pady=50)

    proceed_next = Button(uno,text='CONTINUE',bg="green", fg="white",font=("Arial",30, "bold"),border=15,relief=GROOVE,command=open_edit_Page)
    proceed_next.grid(row=2,column=3, pady=50)

    uno.mainloop()


def open_edit_Page():
    p_code = StringVar()
    p_code.set(Choose_var.get())
    Edit_page_for_docs(doc_code, p_code)


def Patient_list_for_doc(doc_code):
    con = msc.connect(host='localhost', user='root', passwd='onkar123', database='pyproject')
    cur = con.cursor()
    sql = "select Code from patients where Doc_code = '{0}' ;".format(doc_code)

    cur.execute(sql)
    tot = cur.fetchall()
    lst = [x[0] for x in tot]

    return lst


status = False
root = Tk()
root.title('Patient Management System')
root.geometry('1920x1080')


try:
    con = msc.connect(host='localhost', user='root', passwd='onkar123', database='pyproject')
    cur = con.cursor()
    status = None

    label = Label(root, text="THE PROFILE PAGE FOR STAFF AND DOCTORS", font=("Arial", 40, "bold"), border=10,relief=GROOVE, bg="lightgrey", fg="blue")
    label.grid(row=0, column=0, columnspan=4, padx=50, pady=50)

    username = tk.StringVar()
    password = tk.StringVar()
    usernamelabel = tk.Label(root,text="USERNAME:",font=('Arial',35,"bold"), bg="lightgrey", fg="blue").grid(row=1, column=0,columnspan=2,padx=50,pady=50)
    passwordlabel = tk.Label(root,text="PASSWORD:",font=('Arial',35,"bold"), bg="lightgrey", fg="blue").grid(row=2, column=0,columnspan=2,padx=50,pady=50)

    name = tk.Entry(root, textvariable=username, bd=12, font=("Arial", 20), width=35, borderwidth=15)
    name.grid(column=2, row=1, padx=20, pady=20)

    passw = tk.Entry(root, textvariable=password, bd=12, font=("Arial", 20), width=35, borderwidth=15, show='*')
    passw.grid(column=2, row=2, padx=20, pady=20)

    user_ver = partial(user_ver, status, username, password)

    con = tk.Button(root, text='Confirm', command=user_ver,bg="green", fg="white", font=("Arial", 30, "bold"), border=10)
    can = tk.Button(root, text='Cancel', command=root.quit,bg="red", fg="white", font=("Arial", 30, "bold"), border=10)
    can.grid(column=2, row=3,pady=30, padx=50,columnspan=2)
    con.grid(column=0, row=3,pady=30, padx=50,columnspan=2)

    root.mainloop()

except:
    print('A connection error was encountered')
