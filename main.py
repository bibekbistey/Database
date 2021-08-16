from tkinter import *
import sqlite3
root=Tk()
root.title("Creating database")
#Database
con=sqlite3.connect("contact.db")
#Create cursor
c=con.cursor()
#create table

'''c.execute("""CREATE TABLE contacts(
                first_name text
                last_name text
                city text
                phone_number integer
                state text
                pincode integer)""")
print("Table created succesfully")'''
def submit():
    con = sqlite3.connect("contact.db")
    c = con.cursor()
    c.execute("INSERT INTO contacts VALUES(:first_name, :last_name, :city_name, :phone_num, :state_name, :pin_code)",{
        "first_name": f_name.get(),
        "last_name": l_name.get(),
        "city_name": c_name.get(),
        "phone_num": p_num.get(),
        "state_name": s_name.get(),
        "pin_code": p_code.get()
    })
    con.commit()
    #commit close
    con.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    c_name.delete(0,END)
    p_num.delete(0,END)
    s_name.delete(0,END)
    p_code.delete(0,END)

def query():
    con = sqlite3.connect("contact.db")
    c = con.cursor()
    c.execute("SELECT *,oid FROM contacts")
    records=c.fetchall()
    print(records)
    con.commit()
    # commit close
    con.close()
    print_record=''
    for record in records:
        print_record+=str(record)+"/n"
    query_record=Label(root,text=print_record)
    query_record.grid(row=8,column=0,columnspan=2)


f_name=Entry(root)
f_name.grid(row=0,column=1)
l_name=Entry(root)
l_name.grid(row=1,column=1)
c_name=Entry(root)
c_name.grid(row=2,column=1)
p_num=Entry(root)
p_num.grid(row=3,column=1)
s_name=Entry(root)
s_name.grid(row=4,column=1)
p_code=Entry(root)
p_code.grid(row=5,column=1)
f=Label(root,text="Firstname").grid(row=0,column=0)
l=Label(root,text="Lastname").grid(row=1,column=0)
t=Label(root,text="City").grid(row=2,column=0)
p=Label(root,text="Phonenumber").grid(row=3,column=0)
s=Label(root,text="State").grid(row=4,column=0)
i=Label(root,text="Pincode").grid(row=5,column=0)
button1=Button(root,text="Add records",command=submit).grid(row=6,column=0,columnspan=2)
button2=Button(root,text="Show records",command=query).grid(row=7,column=0,columnspan=2)
#commit change
con.commit()
#commit close
con.close()
root.mainloop()