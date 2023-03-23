
from tkinter import *
from tkinter import messagebox
from scrolltable import *
import sqlite3


GUI = Tk()
GUI.geometry('980x320')
GUI.option_add('*font', 'tahoma 12')
GUI.option_add('*Button*background', 'light gray')

con = sqlite3.connect('/Users/apaonum/Documents/python-101/HW7/db.sqlite')
cur = con.cursor()

show_columns = ['id', 'name', 'position', 'salary', 'phone', 'birthday']
column_widths = [4, 15, 15, 10, 13, 13]
table = None

'''Define the procedure that will be called data from Method 
and can recall the data if add new data or update data'''


def show_data():
    global table
    if isinstance(table, TableView):  # remove the old table
        table.destroy()

    cols = ','.join(show_columns)  # attend columns with ','
    # Collect only specify columns to fill in SQL
    sql = f'SELECT {cols} FROM Employee'
    cur.execute(sql)
    rows = cur.fetchall()
    table = TableView(GUI, height=250, headers=show_columns,
                      column_widths=column_widths,
                      header_font='tahoma 12 bold',
                      header_bg='navy', header_fg='white')

    table.grid(row=0, column=0, padx=10, pady=10)
    table.setdata(rows)


show_data()  # Call the Method to show the data when program started

# ------------------ Input data for add or edit --------------------------------
frame = LabelFrame(GUI, text='Employee Information')
frame.grid(row=0, column=1, padx=10, pady=5)

# add widget in Frame (Used grid structure)


def add_grid(w, r, c, cspan=1):
    w.grid(row=r, column=c, columnspan=cspan, sticky=W, padx=10, pady=5)


add_grid(Label(frame, text='id:'), r=0, c=0)
ent_id = Entry(frame, width=10)
add_grid(ent_id, r=0, c=1, cspan=2)

add_grid(Label(frame, text='Name:'), r=1, c=0)
ent_name = Entry(frame, width=20)
add_grid(ent_name, r=1, c=1, cspan=2)

add_grid(Label(frame, text='Position:'), r=2, c=0)
ent_pos = Entry(frame, width=20)
add_grid(ent_pos, r=2, c=1, cspan=2)

add_grid(Label(frame, text='Salary:'), r=3, c=0)
ent_salary = Entry(frame, width=20)
add_grid(ent_salary, r=3, c=1, cspan=2)

add_grid(Label(frame, text='Phone:'), r=4, c=0)
ent_tel = Entry(frame, width=20)
add_grid(ent_tel, r=4, c=1, cspan=2)

add_grid(Label(frame, text='Birthday:'), r=5, c=0)
ent_birth = Entry(frame, width=20)
add_grid(ent_birth, r=5, c=1, cspan=2)

bt_add = Button(frame, text='Add', command=lambda: add_data())
bt_add.grid(row=6, column=1, padx=10, pady=10)

bt_update = Button(frame, text='Update', command=lambda: update_data())
bt_update.grid(row=6, column=2, padx=10, pady=10)

# Used Entry to built list for easy access
all_entries = [ent_id, ent_name, ent_pos, ent_salary, ent_tel, ent_birth]

# Read data from all Entry to kept in all_entries list and define them to SQL's parameter


def get_data():
    data = []
    for w in all_entries:
        data.append(w.get())
    return data


def add_data():
    sql = 'INSERT INTO Employee VALUES(null, ?, ?, ?, ?, ?)'
    data = get_data()
    del data[0]  # id column is AutoIncrement in SQL

    r = cur.execute(sql, data)
    if r.rowcount == 1:
        con.commit()
        messagebox.showinfo('Success', 'Save Success!')
        show_data()
        clear_data()
    else:
        messagebox.showerror('Error', 'Save data failed, Please try again.')


def update_data():
    sql = '''UPDATE Employee SET
             name=?, position=?, salary=?, phone=?, birthday=?
             WHERE id=?'''

    data = get_data()
    data.append(data[0])
    del data[0]  # id column is AutoIncrement in SQL

    r = cur.execute(sql, data)
    if r.rowcount == 1:
        con.commit()
        messagebox.showinfo('Success', 'Save Success!')
        show_data()
        clear_data()
    else:
        messagebox.showerror('Error', 'Save data failed, Please try again.')


def clear_data():
    for w in all_entries:
        w.delete(0, END)


mainloop()
