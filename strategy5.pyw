import time
import mysql.connector
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk

try:
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="trading", password="1234")
    
except Exception as b:
    tmsg.showerror("Database Connectivity", f"Error : {b}")
    exit()

dta = []
count = 0

def showMessage(title, msg, timeout=2000):
    message = Tk()
    message.withdraw()
    message.after(timeout, message.destroy)
    tmsg.showinfo(title, msg, master = message)

def on_closing():
    if tmsg.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        main_gui(user)
        return 

def check():
    e.set(1)   # variable e is used to check whether back button is clicked or not
    window.destroy()

def access():
    global dta
    global count
    global user
    count += 1
    if count > 1:
        main.destroy()
    root = Tk()
    root.geometry("400x250")
    root.title("Window 1")

    Label(root, text="Login Window", font="helvetica 20 italic underline",
          fg="red", pady=15).grid(row=0, column=2)
    Label(root, text="Username:  ", font="times 15 bold italic",
          pady=15, padx=15).grid(row=1, column=1)
    Label(root, text="Password:  ", font="times 15 bold italic",
          padx=15).grid(row=2, column=1)

    uservalue = StringVar()
    passvalue = StringVar()

    userentry = Entry(root, textvariable=uservalue)
    passentry = Entry(root, textvariable=passvalue, show="*")

    userentry.grid(row=1, column=2, pady=15)
    passentry.grid(row=2, column=2, pady=15)

    Button(text="Submit", command=root.destroy,
           font="comicsancsm 11 bold").grid(row=3, column=2, pady=15)

    root.mainloop()

    user = uservalue.get()
    pswd = passvalue.get()

    c = mydb.cursor()
    c.execute("select * from user")
    dta = c.fetchall()
    for i in dta:
        if pswd == i[0] and user == i[1]:
            c.execute(
                f"select day,amount,pnl,withdrawal,remarks,date_time from data where user='{user}'")
            dta = c.fetchall()
            showMessage("Authorization Confirmed", "Redirecting......Please Wait")
            main_gui(user)
            return True
    else:
        tmsg.showerror("Access Denied", "You have entered Incorrect details.")
        return False


def execution(user):
    global window, e
    global dta
    main.destroy()
    pc_time = time.asctime(time.localtime())
    pc_time = pc_time[:11]
    prev_pc_time = dta[-1][-1]

    if prev_pc_time == pc_time:
        tmsg.showwarning(
            "Bad Action", "Executing Twice in a Day! \nDon't Do this")
        main_gui(user)
        return
        

    day_count = dta[-1][0] + 1
    amount_prev = float(dta[-1][1])

    window = Tk()
    window.geometry("350x310")
    window.title("Window 2")
    Label(window, text="Execution", pady=10,
          font="lucida 20 bold italic underline", fg="blue").pack()
    Label(
        window, text=f"Starting  of DAY {day_count}\n     Total Amount is {amount_prev}\n", font="times 14 italic").pack()

    num = StringVar()
    remarks = StringVar()

    Label(window, text="Enter Today's Closing Amount",
          font="times 15 bold italic", pady=5, padx=10).pack()
    Entry(window, textvariable=num).pack()
    Label(window, text="Enter Remarks",
          font="times 15 bold italic", pady=5, padx=10).pack()
    Entry(window, textvariable=remarks).pack()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    Button(window, text="Submit", command=window.destroy,
           pady=5, padx=5).pack(pady=10, padx=60, side=RIGHT)
    e = IntVar()
    e.set(0)
    Button(window, text="Back", command=check, pady=5,
           padx=5).pack(pady=10, padx=60, side=RIGHT)

    window.mainloop()

    # variable e is used to check whether back button is clicked or not
    if e.get():
        main_gui(user)
        return 0

    amount_today = float(num.get())
    r = remarks.get()
    c = mydb.cursor()
    pnl = amount_today - amount_prev
    print(pnl)
    c.execute("insert into data(day,amount,pnl,remarks,date_time,user) values({},{},{},'{}','{}','{}')".format(
        day_count, amount_today, pnl, r, pc_time, user))
    mydb.commit()
    c.execute(
        f"select day,amount,pnl,withdrawal,remarks,date_time from data where user='{user}'")
    dta = c.fetchall()
    if pnl < 0:
        tmsg.showinfo("Message", "Not all your days will be the same.\nA day of sadness and another of happiness. \nA day of profit and another of loss. \nThat's the test of life.\nRemember the Commitment you have done and your values to your family.\nNever Lose Faith in you.\nImprove The Mistakes.")

    else:
        tmsg.showinfo("Message", "Don't be so happy. \nYou have to go long. \nRemember Consistency is the key to Success. \nNo one is better Than You!\nDon't Trade Now.\nEnjoy Your Day!\nSpend time in playing and with friends.")

    main_gui(user)




def delete(user):
    global window, e, dta
    main.destroy()
    day_count = dta[-1][0]

    window = Tk()
    window.geometry("350x230")
    window.title("Window 4")
    Label(window, text="Deletion of a Day", pady=10,
          font="lucida 20 bold italic underline", fg="blue").pack()
    Label(
        window, text=f"   Last Day of Trading was {day_count}\n", font="times 14 italic").pack()

    day = StringVar()
    Label(window, text="Which day? ",
          font="times 15 bold italic", pady=5, padx=10).pack()
    Entry(window, textvariable=day).pack()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    Button(window, text="Submit", command=window.destroy,
           pady=5, padx=5).pack(pady=10, padx=60, side=RIGHT)
    e = IntVar()
    e.set(0)
    Button(window, text="Back", command=check, pady=5,
           padx=5).pack(pady=10, padx=60, side=RIGHT)

    window.mainloop()

    # variable e is used to check whether back button is clicked or not
    if e.get():
        main_gui(user)
        return 0

    d = int(day.get())
    c = mydb.cursor()

    if d > day_count:
        tmsg.showerror("Error", f"Error : Day out of Range!")
        exit()

    c.execute(f"delete from data where day={d} and user='{user}'")
    mydb.commit()
    showMessage("Confirmation", "Successfully deleted")

    c.execute(
        f"select day,amount,pnl,withdrawal,remarks,date_time from data where user='{user}'")
    dta = c.fetchall()
    main_gui(user)


def change_amount(user):
    global window, e, dta
    main.destroy()
    day_count = dta[-1][0]

    window = Tk()
    window.geometry("350x290")
    window.title("Window 4")
    Label(window, text="Change Amount", pady=10,
          font="lucida 20 bold italic underline", fg="blue").pack()
    Label(
        window, text=f"   Last Day of Trading was {day_count}\n", font="times 14 italic").pack()

    day = StringVar()
    am = StringVar()

    Label(window, text="Which day? ",
          font="times 15 bold italic", pady=5, padx=10).pack()
    Entry(window, textvariable=day).pack()
    Label(window, text="New Amount",
          font="times 15 bold italic", pady=5, padx=10).pack()
    Entry(window, textvariable=am).pack()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    Button(window, text="Submit", command=window.destroy,
           pady=5, padx=5).pack(pady=10, padx=60, side=RIGHT)
    e = IntVar()
    e.set(0)
    Button(window, text="Back", command=check, pady=5,
           padx=5).pack(pady=10, padx=60, side=RIGHT)

    window.mainloop()

    # variable e is used to check whether back button is clicked or not
    if e.get():
        main_gui(user)
        return 0

    new_amount = float(am.get())
    d = int(day.get())
    amount = float(dta[-2][1])
    pnl = new_amount - amount
    c = mydb.cursor()
    if d > day_count:
        tmsg.showerror("Error", f"Error : Day out of Range!")
        exit()
    c.execute(
        f"update data set amount={new_amount},pnl={pnl} where day={d} and user='{user}'")
    mydb.commit()
    showMessage("Confirmation", "Successfully changed")

    c.execute(
        f"select day,amount,pnl,withdrawal,remarks,date_time from data where user='{user}'")
    dta = c.fetchall()
    main_gui(user)


def show_details():
    global window, e, dta
    main.destroy()
    if len(dta)==0:
    
        tmsg.showwarning("Error", "No data found!")
        main_gui(user)
        return 0
    day_count = dta[-1][0] + 1

    window = Tk()
    window.title("Window 7")
    window.geometry("820x500")

        
    style = ttk.Style()
    style.theme_use('clam')

    l = ("Day", "Amount", "PnL", "Remarks")
    table = ttk.Treeview(window, column=l, show="headings", height=20)
    for i in range(1, 5):
        if i == 4:
            table.column(f"# {i}", anchor=CENTER, stretch=NO, width=500)
            table.heading(f"# {i}", text=l[i-1])
            break
        table.column(f"# {i}", anchor=CENTER, stretch=NO, width=100)
        table.heading(f"# {i}", text=l[i-1])

    for i in range(day_count):
        table.insert('', 'end', values=(
            dta[i][0], dta[i][1], dta[i][2], dta[i][4]))

    table.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=table.yview)
    table.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    window.protocol("WM_DELETE_WINDOW", on_closing)
    Button(window, text="Back", command=window.destroy,
           font="lucida 15 bold", padx=5, pady=5).grid(pady=10)
    window.mainloop()
    main_gui(user)

def withdrawal(user):
    global window, e, dta
    main.destroy()
    c = mydb.cursor()
    day_count = dta[-1][0]
   
    window = Tk()
    window.geometry("350x290")
    window.title("Window 5")
    Label(window, text="Withdrawal", pady=10,
          font="lucida 20 bold italic underline", fg="blue").pack()
    Label(
        window, text=f"   Last Day of Trading was {day_count}\n", font="times 14 italic").pack()

    day = IntVar()
    with_am = StringVar()

    Label(window, text="Which day? ",
          font="times 15 bold italic", pady=5, padx=10).pack()
    Entry(window, textvariable=day).pack()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    Label(window, text="Withdrawal",
          font="times 15 bold italic", pady=5, padx=10).pack()
    Entry(window, textvariable=with_am).pack()
    Button(window, text="Submit", command=window.destroy,
           pady=5, padx=5).pack(pady=10, padx=60, side=RIGHT)
    e = IntVar()
    e.set(0)
    Button(window, text="Back", command=check, pady=5,
           padx=5).pack(pady=10, padx=60, side=RIGHT)

    window.mainloop()

    if e.get():
        main_gui(user)
        return 0

    d = day.get()
    w = float(with_am.get())
    if d > day_count:
        tmsg.showerror("Error", "Error : Day out of Range!")
        exit()
    amount = float(dta[-1][1]) - w
    c.execute(f"Select remarks from data where day={d} and user='{user}'")
    remarks1 = c.fetchone()
    remarks = str(remarks1[0]) + " + Withdrawal $" + str(w)
    c.execute(
        f"update data set withdrawal={w},amount={amount},remarks='{remarks}' where day={d} and user='{user}'")
    mydb.commit()
    showMessage("Confirmation", "Successful! Added to Database")
 
    c.execute(
        f"select day,amount,pnl,withdrawal,remarks,date_time from data where user='{user}'")
    dta = c.fetchall()
    main_gui(user)


def remarks(user):
    global window, e, dta
    main.destroy()
    c = mydb.cursor()

    day_count = dta[-1][0]
    window = Tk()
    window.geometry("350x290")
    window.title("Window 6")
    Label(window, text="Change Remarks", pady=10,
          font="lucida 20 bold italic underline", fg="blue").pack()
    Label(
        window, text=f"   Last Day of Trading was {day_count}\n", font="times 14 italic").pack()

    day = StringVar()
    remarks = StringVar()

    Label(window, text="Which day? ",
          font="times 15 bold italic", pady=5, padx=10).pack()
    Entry(window, textvariable=day).pack()
    Label(window, text="Remarks",
          font="times 15 bold italic", pady=5, padx=10).pack()
    Entry(window, textvariable=remarks).pack()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    Button(window, text="Submit", command=window.destroy,
           pady=5, padx=5).pack(pady=10, padx=60, side=RIGHT)
    e = IntVar()
    e.set(0)
    Button(window, text="Back", command=check, pady=5,
           padx=5).pack(pady=10, padx=60, side=RIGHT)

    window.mainloop()

    if e.get():
        main_gui(user)
        return 0

    d = int(day.get())
    r = remarks.get()
    if d > day_count:
        tmsg.showerror("Error", f"Error : Day out of Range!")
        main_gui(user)
        return

    c.execute(f"update data set remarks='{r}' where day={d} and user='{user}'")
    mydb.commit()
    
    showMessage("Confirmation", "Successful! Added to Database")

    c.execute(
        f"select day,amount,pnl,withdrawal,remarks,date_time from data where user='{user}'")
    dta = c.fetchall()
    main_gui(user)


def graph(loc, label):
    global dta

    y = [dta[i][loc] for i in range(len(dta))]
    x = [dta[i][0] for i in range(len(dta))]
    z = [0 for i in range(len(dta))]

    # Create a line plot
    plt.plot(x, y)
    plt.plot(x, z)

    # Customize the plot
    plt.xlabel('Days -->')
    plt.ylabel(label + '($) -->')
    plt.title(label + ' Analysis')

    # Display the plot
    plt.show()


class topbar:
    """This class is made for organising the topbar functions together."""
    def help(event):
        tmsg.showinfo("Need help", "Ask Chirag for help.")

    def contact_us(event):
        tmsg.showinfo(
            "Contact Details", "Feel Free to Contact Us on following details:\nMail: chirag.goyal0303@gmail.com\nMobile: +919XXXXXXXXX")

    def rate(event):
        value = tmsg.askquestion(
            "Was your experience Good?", "You used this gui.. Was your experience Good?")
        if value == "yes":
            msg = "Great. Rate us on appstore please"
        else:
            msg = "Tell us what went wrong. We will call you soon"
        tmsg.showinfo("Experience", msg)

    def dev_info(event):
        tmsg.showinfo(
            "Developing Info", "This program is developed by Chirag Goyal.\nDeveloping since May 2023.\nReleasing on July 2023.")
        
def main_closing():
    global main
    if tmsg.askokcancel("Quit","Do you want to quit?"):
        main.destroy()
        return

def main_gui(user):
    global main
    top_bar = topbar()
    main = Tk()
    main.geometry("650x450")
    main.title("Main Window")
    main.minsize(650,450)
    main.maxsize(650,450)
    # menu
    mainmenu = Menu(main)
    mainmenu.add_command(label="Help", command=top_bar.help)
    mainmenu.add_command(label="Contact Us", command=top_bar.contact_us)
    mainmenu.add_command(label="Rate Us", command=top_bar.rate)
    mainmenu.add_command(label="Developer Info", command=top_bar.dev_info)
    main.config(menu=mainmenu)

    # statusbar
    status = StringVar()
    status.set("Ready")
    sbar = Frame(main, relief=SUNKEN, borderwidth=3)
    sbar.pack(side=BOTTOM, fill=X, pady=5)
    Button(sbar, text="Exit", command=main.destroy,
           padx=5).pack(side=LEFT, padx=5)
    pc_time = time.asctime(time.localtime())
    pc_time = f"\t\t\t\t\t\tLOC: 500\t\tPython\t  {pc_time[:10]}-{pc_time[20:]}-{pc_time[11:19]}"
    Label(sbar, text=pc_time).pack(side=LEFT, padx=10)

    # creating Frames
    f1 = Frame(main, bg="grey", borderwidth=4, relief=SUNKEN, padx=10)
    f1.pack(side=LEFT, fill=Y, padx=15)
    Label(f1, fg="white", text="Trading System",
          font="lucida 25 bold underline", padx=5, bg="skyblue").pack(pady=10)
    Label(f1, text="This Program is developed for storing, \nmaintaining,and analysing the data of\nany person's trading data. This program\nis developed using Python which is \nconnected to a database using SQL.\n\nThis program offers many operations for\nuser such as Executing,Changing details etc.\n\nThis program uses many libraries offered\nby Python.Some of them are:\n1. Mysql Connector\n2. Matplotlib\n3. Time\n4. Tkinter\n5. Getpass", font="times 12 italic").pack(pady=17)

    f2 = Frame(main, borderwidth=4, relief=SUNKEN, padx=30)
    f2.pack(side=RIGHT, fill=Y, padx=20)
    Label(f2, text="OPERATIONS:",
          font="helvetica 20 bold underline", padx=5).pack(pady=10)

    var = IntVar()
    var.set(10)
    main.protocol("WM_DELETE_WINDOW", main_closing)
    radio = Radiobutton(f2, text="Execute", padx=10,
                        variable=var, value=1, command=lambda: execution(user))
    radio.pack(anchor="w", pady=5)

    radio = Radiobutton(f2, text="Delete Day", padx=10,
                        variable=var, value=2, command=lambda: delete(user))
    radio.pack(anchor="w", pady=5)

    radio = Radiobutton(f2, text="Change Amount", padx=10,
                        variable=var, value=3, command=lambda: change_amount(user))
    radio.pack(anchor="w", pady=5)

    radio = Radiobutton(f2, text="Show details", padx=10,
                        variable=var, value=4, command=show_details)
    radio.pack(anchor="w", pady=5)

    radio = Radiobutton(f2, text="Withdrawal", padx=10,
                        variable=var, value=5, command=lambda: withdrawal(user))
    radio.pack(anchor="w", pady=5)

    radio = Radiobutton(f2, text="Change Remarks", padx=10,
                        variable=var, value=6, command=lambda: remarks(user))
    radio.pack(anchor="w", pady=5)

    radio = Radiobutton(f2, text="Graphical Analysis(Amount)", padx=10,
                        variable=var, value=7, command=lambda: graph(1, "Amount"))
    radio.pack(anchor="w", pady=5)

    radio = Radiobutton(f2, text="Graphical Analysis(PnL)", padx=10,
                        variable=var, value=8, command=lambda: graph(2, "PnL"))
    radio.pack(anchor="w", pady=5)

    radio = Radiobutton(f2, text="Change User", padx=10,
                        variable=var, value=9, command=access)
    radio.pack(anchor="w", pady=5)
    
    main.protocol("WM_DELETE_WINDOW", main_closing)
    main.mainloop()
    return 

# driver_code
if __name__== '__main__':
    access()
