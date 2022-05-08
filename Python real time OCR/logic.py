
from tkinter import *
from deep_translator import GoogleTranslator

import pyautogui
import keyboard
import cv2
import numpy as np
from PIL import ImageGrab
from display import Note
import pytesseract








pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Application():
    shortKey = {"s": 83, "t": 84, "u": 85, "y": 89}

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

        root.attributes("-transparent", "blue")
        root.geometry('400x50+200+200')  # set new geometry
        root.title('Lil Snippy')
        self.menu_frame = Frame(master, bg="blue")
        self.menu_frame.pack(fill=BOTH, expand=YES)

        self.buttonBar = Frame(self.menu_frame, bg="")
        self.buttonBar.pack(fill=BOTH, expand=YES)

        self.snipButton = Button(
            self.buttonBar, width=3, command=self.createScreenCanvas, background="red")
        self.snipButton.pack(expand=YES)
        

    def Translate(self, x1, y1, x2, y2):
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        capture = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        cv2.imshow("image", capture)


        translated = GoogleTranslator(source='vi', target='en').translate(text=pytesseract.image_to_string(img))

        print(translated)
        Note(root,translated,5000)
        # root have note widget in it kill it
        root.update()
        self.master_screen.bind("<Return>", self.display_rectangle)

        # for data in root.winfo_children:
        #     print(data)
            
        

    def createScreenCanvas(self,event=None):
        if self.isUsed == False:
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
            keyboard.on_press(self.temp)

            self.master_screen.attributes('-fullscreen', True)
            self.master_screen.attributes('-alpha', 0.3)
            self.master_screen.lift()
            self.master_screen.attributes("-topmost", True)
            self.isUsed = True


    def on_button_release(self, event):
        

        self.master_screen.bind("<Return>", self.display_rectangle)
        self.master_screen.bind("<Return>", self.display_rectangle)
        keyboard.on_press(self.temp)
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

        self.screenCanvas.unbind("<ButtonPress-1>")
        self.screenCanvas.unbind("<B1-Motion>")
        self.screenCanvas.unbind("<ButtonRelease-1>")

        self.screenCanvas.config(bg='#add123')

        self.master_screen.wm_attributes('-transparentcolor', '#add123')
        self.master_screen.wm_attributes('-topmost', True)

        keyboard.on_press(self.temp)

        print("get in here")

    def temp(self, event):
        if event.name == "esc":
            self.exit()

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

    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        self.screenCanvas.coords(
            self.rect, self.start_x, self.start_y, self.curX, self.curY)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()


