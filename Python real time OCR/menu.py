

from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import *
from turtle import width
import PySimpleGUI as sg
root = tk.Tk()
# root.update() 
# root.iconbitmap('Sms.ico')

root.geometry("680x400")
root.title("OCR")
root.resizable(0,0)
Label(root,text="Setting",font='Helvetica 10 bold').grid(row=0,column=0,padx=10,pady=10,sticky=W,columnspan=2)
Label(root,text="Engine Using").grid(row=1,column=0,padx=10,pady=10,sticky=W)
Label(root,text="Original Language").grid(row=2,column=0,padx=10,pady=10,sticky=W)
Label(root,text="Short Cut").grid(row=3,column=0,padx=10,pady=10,sticky=W)



Label(root,text="Rearl Time Translate",font='Helvetica 10 bold').grid(row=4,column=0,padx=10,pady=10,sticky=W,columnspan=2)
Label(root,text="Scan every ").grid(row=5,column=0,padx=10,pady=10,sticky=W)
Label(root,text="Disaper Time ").grid(row=6,column=0,padx=10,pady=10,sticky=W)

# engine
combo=Combobox(value=('Cong', 'Tru', 'Nhan', 'Chia'), width=20, state="readonly")

combo.grid(row=1,column=2,padx=10,pady=15,sticky=EW,columnspan=2)
combo.current(0)


# languae
languae=Combobox(value=('English', 'Vietnamese', 'Chinese', 'Japanese'), width=20, state="readonly")
languae.grid(row=2,column=2,padx=10,pady=15,sticky=EW,columnspan=2)
languae.current(0)



# short cut
short_cut=Combobox(value=('Ctrl+Shift+S', 'Ctrl+Shift+T', 'Ctrl+Shift+Y', 'Ctrl+Shift+U'), width=20, state="readonly")
short_cut.grid(row=3,column=2,padx=10,pady=15,sticky=EW,columnspan=2)
short_cut.current(0)









# SCAN TIME
current_value = tk.DoubleVar()
def get_current_value():
    return str(int(100+((int(current_value.get())-0)*(3000-100))/100))+"ms"


def slider_changed(event):
    
    #get_current_value()==0 return = 100
    #get_current_value()==100 return = 3000
    # 100+get_current_value()*3000
    #MAP VALUE TO SCALE
    slider1Value.configure(text=get_current_value())
    
    # print(get_current_value())

    # print(str(int())
def callback():
    return slider_changed()


slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
    , length=100
    )

slider.grid(
    column=3,
    row=5,
     padx=10,pady=15,
    sticky=E
)

slider1Value=Label(root,text=str(get_current_value()))
slider1Value.grid(row=5,column=2,padx=10,pady=10,sticky=W)




# dISAPER TIME
current_value2=tk.DoubleVar()
def get_current_value2():
    return str(int(0+((int(current_value2.get())-0)*(5000-0))/100))+"ms"
def slider_changed2(event):
    slider2Value.configure(text=get_current_value2())
slider2 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed2,
    variable=current_value2
   
)
slider2.grid(
    column=3,
    row=6,
     padx=10,pady=15,
    sticky=EW
)
slider2Value=Label(root,text=str(get_current_value2()))
slider2Value.grid(row=6,column=2,padx=10,pady=10,sticky=W)





Label(root,text="Subtitle",font='Helvetica 10 bold').grid(row=0,column=4,padx=10,pady=10,sticky=W,columnspan=2)

Label(root,text="Position").grid(row=1,column=4,padx=10,pady=10,sticky=W)
Label(root,text="Font").grid(row=2,column=4,padx=10,pady=10,sticky=W)
Label(root,text="Size").grid(row=3,column=4,padx=10,pady=10,sticky=W)
Label(root,text="Color").grid(row=4,column=4,padx=10,pady=10,sticky=W)
Label(root,text="Outline Color").grid(row=5,column=4,padx=10,pady=10,sticky=W)
Label(root,text="Opacity").grid(row=6,column=4,padx=10,pady=10,sticky=W)


# position
combo=Combobox(value=('Upper Half','Lower Half'), width=10, state="readonly")

combo.grid(row=1,column=5,padx=10,pady=15,sticky=W,columnspan=2)
combo.current(0)

combo=Combobox(value=('Arial', 'Times New Roman', 'Courier New', 'Comic Sans MS'), width=20, state="readonly")
combo.grid(row=2,column=5,padx=10,pady=15,sticky=W,columnspan=2)
combo.current(0)

#left rigt

combo=Combobox(value=('Left', 'Mid', 'Right'), width=10, state="readonly")

combo.grid(row=1,column=6,padx=10,pady=15,sticky=E,columnspan=2)
combo.current(0)







# font







current_value3=tk.DoubleVar()
def get_current_value3():
    return str(int(10+((int(current_value3.get())-0)*(30-10))/100))+"px"
def slider_changed3(event):
    slider3Value.configure(text=get_current_value3())
slider3 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed3,
    variable=current_value3
   
)
slider3.grid(
    column=6,
    row=3,
     padx=10,pady=15,
    sticky=EW
)
slider3Value=Label(root,text=str(get_current_value3()))
slider3Value.grid(row=3,column=5,padx=10,pady=10,sticky=W)


combo=Combobox(value=('Red', 'Black', 'Blue', 'Yellow','Green','White'), width=20, state="readonly")
combo.grid(row=4,column=5,padx=10,pady=15,sticky=W,columnspan=2)
combo.current(0)

# set the default color to red
# entry.configure(fg='red')

# entry.bind("<Return>", callback)

combo=Combobox(value=('Red', 'Black', 'Blue', 'Yellow','Green','White'), width=20, state="readonly")
combo.grid(row=5,column=5,padx=10,pady=15,sticky=W,columnspan=2)
combo.current(0)




current_value4=tk.DoubleVar()
def get_current_value4():
    return str(int(0+((int(current_value4.get())-0)*(100-0))/100))+"%"
def slider_changed4(event):
    slider4Value.configure(text=get_current_value4())
slider4 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed4,
    variable=current_value4
   
)
slider4.grid(
    column=6,
    row=6,
     padx=10,pady=15,
    sticky=EW
)
slider4Value=Label(root,text=str(get_current_value4()))
slider4Value.grid(row=6,column=5,padx=10,pady=10,sticky=W)


Button(text="Priview").grid(row=7,column=5,padx=10,pady=10,sticky=W)#, command=got_clicked
Button(text="Save").grid(row=7,column=6,padx=10,pady=10,sticky=E)#, command=got_clicked



root.mainloop()