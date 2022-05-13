from tkinter import *
# from threading import Thread #no longer needed

import tkinter as tk
class Note(Toplevel):

    # title = "" #this would block the method to override the current title
    message = ""

    def __init__(self, master,  message,disaper_time,Pos_x,Pos_y,font_size,font,color,bg_color):
        Toplevel.__init__(self, master)
        self.nid = 0
        
        self.message = message
        self.display_note_gui(Pos_x,Pos_y,font_size,font,color,bg_color)  
        
        self.after(disaper_time, self.destroy)
    def display_note_gui(self,Pos_x,Pos_y,font_size,font,color,bg_color):
        '''Tkinter to create a note gui window with parameters '''
        self.wm_attributes("-topmost", 1)
        self.wm_attributes("-fullscreen", 1)
        self.wm_attributes("-alpha", 0.5)
        self.wm_attributes("-transparentcolor", "#BAD0EF")
        self.configure(background="#BAD0EF")
       
        textArea = Label(self, text=self.message, wraplength=self.winfo_screenwidth()/3,bg="#BAD0EF",fg="#BAD0EF",font = ("Bahnschrift", 14))
      
        textArea.place(x=self.winfo_screenwidth()-500, y=0)

        self.update()

       

        x=textArea.winfo_width()
        y=textArea.winfo_height()
        textArea.destroy()
        textArea = Label(self, text=self.message, wraplength=self.winfo_screenwidth()/3,bg=bg_color.lower(),fg=color.lower(),font = (font, int(font_size), "bold"))
      
     

        x_pos=0
        y_pos=0
        if Pos_x=="Upper Half" :
            y_pos=0
        else: 
            y_pos=self.winfo_screenheight()-y
        if Pos_y=="Left" :
            x_pos=0
        elif Pos_y=="Mid" :
            x_pos=self.winfo_screenwidth()/2-x/2
        else:
            x_pos=self.winfo_screenwidth()-x
        print(x_pos,y_pos)
        textArea.place(x=x_pos, y=y_pos)  #bot right
       

    def run(self):
        self.display_note_gui()
