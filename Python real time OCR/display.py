
from tkinter import *
from deep_translator import GoogleTranslator
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter as tk

import pyautogui
import keyboard
import cv2
import numpy as np
from PIL import ImageGrab
from display import Note
import pytesseract








pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Application():
    shortKey = [ 'ctrl + shift +t', 'ctrl + shift +y', 'ctrl + shift +u','ctrl + shift +i']
    # menu construction and 
    def __init__(self, master):
        self.master = master
        self.rect = None
        self.x = self.y = 0
        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None
        self.isUsed = False
        self.screenCanvas = None
        self.note = None

        root.attributes("-transparent", "blue")

        

        # menu construction
        self.master.title("OCR")
        self.master.resizable(0,0)
        Label(self.master,text="Setting",font='Helvetica 10 bold').grid(row=0,column=0,padx=10,pady=10,sticky=W,columnspan=2)
        Label(self.master,text="Engine Using").grid(row=1,column=0,padx=10,pady=10,sticky=W)
        Label(self.master,text="Original Language").grid(row=2,column=0,padx=10,pady=10,sticky=W)
        Label(self.master,text="Short Cut").grid(row=3,column=0,padx=10,pady=10,sticky=W)



        Label(self.master,text="Rearl Time Translate",font='Helvetica 10 bold').grid(row=4,column=0,padx=10,pady=10,sticky=W,columnspan=2)
        Label(self.master,text="Scan every ").grid(row=5,column=0,padx=10,pady=10,sticky=W)
        Label(self.master,text="Disaper Time ").grid(row=6,column=0,padx=10,pady=10,sticky=W)

        # engine
        Engine=Combobox(value=('Cong', 'Tru', 'Nhan', 'Chia'), width=20, state="readonly")

        Engine.grid(row=1,column=2,padx=10,pady=15,sticky=EW,columnspan=2)
        Engine.current(0)


        # languae
        languae=Combobox(value=('English', 'Vietnamese', 'Chinese', 'Japanese'), width=20, state="readonly")
        languae.grid(row=2,column=2,padx=10,pady=15,sticky=EW,columnspan=2)
        languae.current(0)



        # short cut
        short_cut=Combobox(value=('Ctrl+Shift+I', 'Ctrl+Shift+T', 'Ctrl+Shift+Y', 'Ctrl+Shift+U'), width=20, state="readonly")
        short_cut.grid(row=3,column=2,padx=10,pady=15,sticky=EW,columnspan=2)
        short_cut.current(0)









        # SCAN TIME
        current_value = tk.DoubleVar()
        def get_current_value():
            return str(int(100+((int(current_value.get())-0)*(3000-100))/100))+"ms"


        def slider_changed(event):
            
          
            slider_scan.configure(text=get_current_value())
            
           
        def callback():
            return slider_changed()


        slider = ttk.Scale(
            self.master,
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

        slider_scan=Label(self.master,text=str(get_current_value()))
        slider_scan.grid(row=5,column=2,padx=10,pady=10,sticky=W)




        # dISAPER TIME
        current_value2=tk.DoubleVar()
        def get_current_value2():
            return str(int(0+((int(current_value2.get())-0)*(5000-0))/100))+"ms"
        def slider_changed2(event):
            slider_disaper.configure(text=get_current_value2())
        slider2 = ttk.Scale(
            self.master,
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
        slider_disaper=Label(self.master,text=str(get_current_value2()))
        slider_disaper.grid(row=6,column=2,padx=10,pady=10,sticky=W)





        Label(self.master,text="Subtitle",font='Helvetica 10 bold').grid(row=0,column=4,padx=10,pady=10,sticky=W,columnspan=2)

        Label(self.master,text="Position").grid(row=1,column=4,padx=10,pady=10,sticky=W)
        Label(self.master,text="Font").grid(row=2,column=4,padx=10,pady=10,sticky=W)
        Label(self.master,text="Size").grid(row=3,column=4,padx=10,pady=10,sticky=W)
        Label(self.master,text="Color").grid(row=4,column=4,padx=10,pady=10,sticky=W)
        Label(self.master,text="Outline Color").grid(row=5,column=4,padx=10,pady=10,sticky=W)
        Label(self.master,text="Opacity").grid(row=6,column=4,padx=10,pady=10,sticky=W)


        # position
        position_up_down=Combobox(value=('Upper Half','Lower Half'), width=10, state="readonly")

        position_up_down.grid(row=1,column=5,padx=10,pady=15,sticky=W,columnspan=2)
        position_up_down.current(0)

        font=Combobox(value=('Arial', 'Times New Roman', 'Courier New', 'Comic Sans MS'), width=20, state="readonly")
        font.grid(row=2,column=5,padx=10,pady=15,sticky=W,columnspan=2)
        font.current(0)

        #left rigt

        position_left_right=Combobox(value=('Left', 'Mid', 'Right'), width=10, state="readonly")

        position_left_right.grid(row=1,column=6,padx=10,pady=15,sticky=E,columnspan=2)
        position_left_right.current(0)







        # keyboard.add_hotkey('ctrl + shift + a', self.createScreenCanvas)







        # font







        current_value3=tk.DoubleVar()
        def get_current_value3():
            return str(int(10+((int(current_value3.get())-0)*(30-10))/100))+"px"
        def slider_changed3(event):
            slider_font_size.configure(text=get_current_value3())
        slider3 = ttk.Scale(
            self.master,
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
        slider_font_size=Label(self.master,text=str(get_current_value3()))
        slider_font_size.grid(row=3,column=5,padx=10,pady=10,sticky=W)


        color=Combobox(value=('Red', 'Black', 'Blue', 'Yellow','Green','White'), width=20, state="readonly")
        color.grid(row=4,column=5,padx=10,pady=15,sticky=W,columnspan=2)
        color.current(0)





        outline=Combobox(value=('Red', 'Black', 'Blue', 'Yellow','Green','White'), width=20, state="readonly")
        outline.grid(row=5,column=5,padx=10,pady=15,sticky=W,columnspan=2)
        outline.current(0)





        current_value4=tk.DoubleVar()
        def get_current_value4():
            return str(int(0+((int(current_value4.get())-0)*(100-0))/100))+"%"
        def slider_changed4(event):
            opacity.configure(text=get_current_value4())
        slider4 = ttk.Scale(
            self.master,
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
        opacity=Label(self.master,text=str(get_current_value4()))
        opacity.grid(row=6,column=5,padx=10,pady=10,sticky=W)
        # print(opacity)


        
        def Setpreview():
            
            
            self.opacity=opacity.cget("text")[:-1]
            self.outline=outline.get()
            self.color=color.get()
            self.font=font.get()
            self.position_left_right=position_left_right.get()
            self.position_up_down=position_up_down.get()
            
            self.font_size=slider_font_size.cget("text")[:-2]
            self.disaper_time=slider_disaper.cget("text")[:-2]
            self.scan_time=slider_scan.cget("text")[:-2]
           
        def call_preview():
            Setpreview()
            self.preview()
        def call_save():
            Setpreview()
            # 
        def call_print():
            Setpreview()
            self.createScreenCanvas()


        keyboard.add_hotkey('ctrl + shift + p', call_print)
        
        


            

        Button(text="Priview", command=call_preview).grid(row=7,column=5,padx=10,pady=10,sticky=W)
        Button(text="Save",command=call_save).grid(row=7,column=6,padx=10,pady=10,sticky=E)

    
    def preview(self):
        print("Preview")
        
        
        if self.note!=None:
            self.note.destroy()
            
        # self.note=Note(root,"...[THIS IS THE PREVIEW TEXT]...",self.disaper_time,self.position_up_down,self.position_left_right,self.font_size,self.font,self.color,self.outline)

        self.note=Note(root,"...[THIS IS THE PREVIEW TEXT]...",int(self.disaper_time),self.position_up_down,self.position_left_right,self.font_size,self.font,self.color,self.outline)
        # print all the root children
        

        root.update()


     

    def Translate(self, x1, y1, x2, y2):
        if self.note!=None:
            self.note.destroy()
            
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        capture = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        cv2.imshow("image", capture)


        translated = GoogleTranslator(source='auto', target='english').translate(text=pytesseract.image_to_string(img))
        print(translated)

        # print(translated)
        # if root has note then delete it
        
        print("postion:",self.position_up_down,self.position_left_right)
        self.note=Note(root,translated,10000,self.position_up_down,self.position_left_right,self.font_size,self.font,self.color,self.outline)
        # print all the root children
        

        root.update()
        self.master_screen.bind("<Return>", self.display_rectangle)

        # for data in root.winfo_children:
        #     print(data)
            
        

    def createScreenCanvas(self):
      
        if self.isUsed == False:
            # for child in root.winfo_children():
            #     # if child.winfo_class() == "Note":
            #     print(child)
            #     if child==".!note":
            #         child.destroy()
            self.master_screen = Toplevel(root)
            # self.master_screen.withdraw()
            self.master_screen.attributes("-transparent", "blue")
            self.picture_frame = Frame(self.master_screen, background="blue")
            self.picture_frame.pack(fill=BOTH, expand=YES)
            self.master_screen.withdraw()

            self.master_screen.deiconify()



            print(self.master_screen.winfo_children())
            self.screenCanvas = Canvas(
                self.picture_frame, cursor="cross", bg="grey11")
            
            self.screenCanvas.pack(fill=BOTH, expand=YES)


            self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)
            self.screenCanvas.bind("<B1-Motion>", self.on_move_press)
            self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)
            keyboard.add_hotkey('esc', self.exit)
            # keyboard.on_press(self.temp)

            self.master_screen.attributes('-fullscreen', True)
            self.master_screen.attributes('-alpha', 0.3)
            self.master_screen.lift()
            self.master_screen.attributes("-topmost", True)
            self.isUsed = True


    def on_button_release(self, event):
        

        self.master_screen.bind("<Return>", self.display_rectangle)
        self.master_screen.bind("<Return>", self.display_rectangle)
        # keyboard.on_press(self.temp)
        keyboard.add_hotkey('esc', self.exit)
        # keyboard.on_press(self.display_rectangle)
       


        x1 = min(self.start_x, self.curX)
        y1 = min(self.start_y, self.curY)
        x2 = max(self.start_x,self.curX)
        y2 = max(self.start_y, self.curY)
        self.Translate(x1, y1, x2, y2)
        # self.master_screen.lift()
        # self.master_screen.withdraw()
        self.master_screen.attributes("-topmost", True)

        self.master_screen.bind("<Return>", self.display_rectangle)
        self.master_screen.bind("<Return>", self.display_rectangle)
        # self.bind("<Return>", self.display_rectangle)
        # keyboard.on_press(self.display_rectangle)

        

        # return event

  
    def display_rectangle(self, event=None):
        # for child in root.winfo_children():
        #         if child==Note:
        #             child.destroy()
        self.screenCanvas.unbind("<ButtonPress-1>")
        self.screenCanvas.unbind("<B1-Motion>")
        self.screenCanvas.unbind("<ButtonRelease-1>")

        self.screenCanvas.config(bg='#add123')

        self.master_screen.wm_attributes('-transparentcolor', '#add123')
        self.master_screen.wm_attributes('-topmost', True)

        # keyboard.on_press(self.temp)
        keyboard.add_hotkey('esc', self.exit)

        print("get in here")

   
    def exit(self):
        self.isUsed = False
        self.master_screen.update()
        self.screenCanvas.update()
        self.screenCanvas.destroy()
        self.master_screen.withdraw()

        root.deiconify()

    def exit_application(self):
        print("Application exit")
        root.quit()

    def on_button_press(self, event):

        if self.rect != None:
            self.screenCanvas.delete(self.rect)
        self.start_x = self.screenCanvas.canvasx(event.x)
        self.start_y = self.screenCanvas.canvasy(event.y)
        self.rect = self.screenCanvas.create_rectangle(
            self.x, self.y, 2, 2, outline='red',width=5)
        self.screenCanvas.tag_raise(self.rect)
        # for child in root.winfo_children():
        #         # if child.winfo_class() == "Note":
        #         print(child)
        #         if child==".!note":
        #             child.destroy()

    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        self.screenCanvas.coords(
            self.rect, self.start_x, self.start_y, self.curX, self.curY)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()


