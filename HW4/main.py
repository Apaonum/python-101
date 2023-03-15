import csv
import cartype as ct
from tkinter import *
from tkinter import ttk  # theme
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.filedialog import *

############################## CSV Files ##################################


def write_csv(datalist):
    with open('cartype_data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)


def read_csv():
    with open('cartype_data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

# data = readcsv()
# print(data)
# data = ['Americano',55,'8.00 น.']
# write_csv(data)


############################# Save Button ###################################

def savedata():
    engine_type = selected_engine.get()
    fuel_type = selected_fuel.get()
    sunroof_type = selected_sunroof.get()
    wheel_type = selected_wheel.get()
    text_accept = 'บันทึกสำเร็จ'

    print(f'Engine Type: {engine_type}')
    print(f'Fuel Type: {fuel_type}')
    print(f'Sunroof Type: {sunroof_type}')
    print(f'Wheel Type: {wheel_type}')
    messagebox.showinfo('Notification', text_accept)


############################## GUI CARTYPE ##################################
GUI = Tk()
GUI.title('ตรวจสอบชนิดของรถ')
GUI.geometry('800x600')

Font1 = ('Helvetica', 18)
Font2 = ('Helvetica', 16)


############################## Engine type ##################################
engine_label1 = ttk.Label(GUI, text='Engine Type', font=Font1)
engine_label1.pack()

selected_engine = StringVar()
engine_cb = ttk.Combobox(
    GUI, textvariable=selected_engine, font=Font1, width=15)
engine_cb['values'] = ['Diesel', 'Gasoline']
engine_cb['state'] = 'readonly'
engine_cb.pack()

############################## Fuel type  #################################
fuel_label2 = ttk.Label(GUI, text='Fuel Type', font=Font1)
fuel_label2.pack()

selected_fuel = StringVar()
fuel_cb = ttk.Combobox(GUI, textvariable=selected_fuel, font=Font1, width=15)
fuel_cb['values'] = ['Diesel', 'Gasohol']
fuel_cb['state'] = 'readonly'
fuel_cb.pack()

##############################  Sunroof  ##################################
sunroof_label3 = ttk.Label(GUI, text='Sunroof', font=Font1)
sunroof_label3.pack()

selected_sunroof = StringVar()
sunroof_cb = ttk.Combobox(
    GUI, textvariable=selected_sunroof, font=Font1, width=15)
sunroof_cb['values'] = ['Yes', 'No']
sunroof_cb['state'] = 'readonly'
sunroof_cb.pack()

##############################  Wheel type  ##################################
wheel_label4 = ttk.Label(GUI, text='Wheel Type', font=Font1)
wheel_label4.pack()

selected_wheel = StringVar()
wheel_cb = ttk.Combobox(GUI, textvariable=selected_wheel, font=Font1, width=15)
wheel_cb['values'] = ['2WD', '4WD']
wheel_cb['state'] = 'readonly'
wheel_cb.pack()

############################## Button  #################################


def endProgram():
    GUI.destroy()


def selectFile():
    fileopen = askopenfilename()
    fileContent = open(fileopen)
    myLabel1 = Label(text=fileContent.read()).pack()


def checkType():
    engine_type = selected_engine.get()
    fuel_type = selected_fuel.get()
    sunroof_type = selected_sunroof.get()
    wheel_type = selected_wheel.get()
    # text_accept =

    cartype_checked = ct.Cartype(engine_type, fuel_type, sunroof_type, wheel_type)
    messagebox.showinfo('Notification', '{}'.format(cartype_checked.type_check()))


B1 = ttk.Button(GUI, text='Save', command=savedata)
B1.pack(ipadx=20, ipady=20)

B2 = ttk.Button(text='Browse', command=selectFile)
B2.pack(ipadx=20, ipady=20)

buttonC = ttk.Button(GUI, text='Check', command=checkType)
buttonC.pack(ipadx=20, ipady=20)

buttonQ = ttk.Button(GUI, text="Quit", command=endProgram)
buttonQ.pack(ipadx=20, ipady=20)


#############################################################################


GUI.mainloop()
#############################################################################
engine_type = selected_engine.get()
fuel_type = selected_fuel.get()
sunroof_type = selected_sunroof.get()
wheel_type = selected_wheel.get()

data = [engine_type, fuel_type, sunroof_type, wheel_type]
write_csv(data)
cartype01 = ct.Cartype(engine_type, fuel_type, sunroof_type, wheel_type)
cartype01.type_check()
