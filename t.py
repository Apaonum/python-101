#แจ่้งขอส่งสินค้ารอบพิเศษ

from tkinter import *
from tkinter import ttk #theme
from tkinter import messagebox

GUI = Tk()
GUI.title('แจ้งขอส่งสินค้ารอบพิเศษ')
GUI.geometry('800x700')

Font1 = ('Helvetica', 18)
Font2 = ('Helvetica', 16) 


############################# Customer Name ###################################
L1 = ttk.Label(GUI,text='ชื่อลูกค้า',font=Font1)
#L1.grid(row=0, column=0)
L1.pack()

v_cusname= StringVar()
E1 = ttk.Entry(GUI, textvariable=v_cusname, font=Font1, width=30)
E1.pack()

############################# CV Number ###################################
L2 = ttk.Label(GUI,text='CV',font=Font1)
#L1.grid(row=0, column=0)
L2.pack()

v_cvnum= StringVar()
E2 = ttk.Entry(GUI, textvariable=v_cvnum, font=Font1, width=30)
E2.pack()

############################# Ship to No. ##################################
L3 = ttk.Label(GUI,text='Ship to No.',font=Font1)
#L1.grid(row=0, column=0)
L3.pack()

v_shipnum= StringVar()
E3 = ttk.Entry(GUI,textvariable=v_shipnum,font=Font1,width=30)
E3.pack()

############################# จุดจ่ายสินค้า(คลังสินค้า/โรงงาน) ###################################
L4 = ttk.Label(GUI,text='จุดจ่ายสินค้า(คลังสินค้า/โรงงาน)',font=Font1)
#L1.grid(row=0, column=0)
L4.pack()

v_shipplace= StringVar()
E4 = ttk.Entry(GUI,textvariable=v_shipplace,font=Font1,width=30)
E4.pack()

############################# เวลาเข้ารับสินค้าที่โรงงาน ###################################
L5 = ttk.Label(GUI,text='เวลาเข้ารับสินค้าที่โรงงาน',font=Font1)
#L1.grid(row=0, column=0)
L5.pack()

v_tin= StringVar()
E5 = ttk.Entry(GUI,textvariable=v_tin,font=Font1,width=30)
E5.pack()

############################# Date ship ###################################
L6 = ttk.Label(GUI,text='วันที่ส่งสินค้า',font=Font1)
#L1.grid(row=0, column=0)
L6.pack()

v_dateship= StringVar()
E6 = ttk.Entry(GUI,textvariable=v_dateship,font=Font1,width=30)
E6.pack()

############################# Time Recieve ###################################
L7 = ttk.Label(GUI,text='เวลาที่ลูกค้าต้องการรับสินค้า',font=Font1)
#L1.grid(row=0, column=0)
L7.pack()

v_tget= StringVar()
E7 = ttk.Entry(GUI,textvariable=v_tget,font=Font1,width=30)
E7.pack()

############################# Tel No. ###################################
L8 = ttk.Label(GUI,text='เบอร์ติดต่อ ผู้รับสินค้า',font=Font1)
#L1.grid(row=0, column=0)
L8.pack()

v_telnum= StringVar()
E8 = ttk.Entry(GUI,textvariable=v_telnum,font=Font1,width=30)
E8.pack()

############################# Order details ###################################
L9 = ttk.Label(GUI,text='รายการสินค้า,จำนวนสินค้า',font=Font1)
#L1.grid(row=0, column=0)
L9.pack()

v_order= StringVar()
E9 = ttk.Entry(GUI,textvariable=v_order,font=Font1,width=30)
E9.pack()

############################# Temporature ###################################
L10 = ttk.Label(GUI,text='อุณหภูมิจัดส่ง',font=Font1)
#L1.grid(row=0, column=0)
L10.pack()

v_temp= StringVar()
E10 = ttk.Entry(GUI,textvariable=v_temp,font=Font1,width=30)
E10.pack()

############################# SO No. ###################################
L11 = ttk.Label(GUI,text='เลขที่ SO',font=Font1)
#L1.grid(row=0, column=0)
L11.pack()

v_sonum= StringVar()
E11 = ttk.Entry(GUI,textvariable=v_sonum,font=Font1,width=30)
E11.pack()

############################# Button ###################################

def SaveOrder():
    Cus_name = v_cusname.get()
    Cv_num = v_cvnum.get()
    Ship_to = v_shipnum.get()
    Ship_place = v_shipplace.get()
    Time_in = v_tin.get()
    Date = v_dateship.get()
    Time_get = v_tget.get()
    Tel_num = v_telnum.get()
    Order = v_order.get()
    Temp = v_temp.get()
    So_num = v_sonum.get()
    text_accept = 'บันทึกสำเร็จ'

    print('ชื่อลูกค้า : {}'.format(Cus_name))
    print('CV No. : {}'.format(Cv_num))
    print('Ship to : {}'.format(Ship_to))
    print('จุดจ่ายสินค้า(คลังสินค้า/โรงงาน) : {}'.format(Ship_place))
    print('เวลาเข้ารับสินค้าที่โรงงาน : {}'.format(Time_in))
    print('วันที่ส่งสินค้า : {}'.format(Date))
    print('เวลาที่ลูกค้าต้องการรับสินค้า : {}'.format(Time_get))
    print('เบอร์ติดต่อ ผู้รับสินค้า : {}'.format(Tel_num))
    print('รายการสินค้า,จำนวนสินค้า : {}'.format(Order))
    print('อุณหภูมิจัดส่ง: {}'.format(Temp))
    print('เลขที่ SO : {}'.format(So_num))
    print('--------------------------------------------------------') 
    messagebox.showinfo('Notification', text_accept)




B1 = ttk.Button(GUI,text='Save', command=SaveOrder)
B1.pack(ipadx=40, ipady=40)







GUI.mainloop()
