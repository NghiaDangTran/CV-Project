from tkinter import *
# from threading import Thread #no longer needed

import tkinter as tk
class Note(Toplevel):

    # title = "" #this would block the method to override the current title
    message = ""

    def __init__(self, master,  message,timeout=-1):
        Toplevel.__init__(self, master)
        self.nid = 0
        
        self.message = message
        self.display_note_gui()  
        if timeout>=0:
            self.after(timeout, self.destroy)
    def display_note_gui(self):
        '''Tkinter to create a note gui window with parameters '''
        # no window, just self
        self.wm_attributes("-topmost", 1)
        self.wm_attributes("-fullscreen", 1)
        self.wm_attributes("-alpha", 0.5)
        self.wm_attributes("-transparentcolor", "#BAD0EF")
        self.configure(background="#BAD0EF")
       
        textArea = Label(self, text=self.message, wraplength=self.winfo_screenwidth()/3,bg="#BAD0EF",fg="#BAD0EF",font = ("Bahnschrift", 14))
      
        textArea.place(x=self.winfo_screenwidth()-500, y=0)

        self.update()

        print(textArea.winfo_width())
        print(textArea.winfo_height())

        x=textArea.winfo_width()
        y=textArea.winfo_height()
        textArea.destroy()
        textArea = Label(self, text=self.message, wraplength=self.winfo_screenwidth()/3,bg="#BAD0EF",fg="red",font = ("Times New Roman", 14, "bold"))
        # textArea.place(x=self.winfo_screenwidth()-x, y=self.winfo_screenheight()-y)  #bot right
        # textArea.place(x=0, y=0)# top left
        textArea.place(x=0, y=self.winfo_screenheight()-y) # bot left
        # textArea.place(x=self.winfo_screenwidth()/2-x/2, y=0) # mid top#
        # textArea.place(x=self.winfo_screenwidth()/2-x/2, y=self.winfo_screenheight()-y) # mid bot


    def run(self):
        self.display_note_gui()


