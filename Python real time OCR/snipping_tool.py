from tkinter import *
import pyautogui
import keyboard
import datetime


class Application():
    def __init__(self, master):
        self.master = master
        self.rect = None
        self.x = self.y = 0
        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None
        self.isUsed=False
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
        print("loop again")
        # self.exitButton = Button(
        #     self.buttonBar, width=3, command=self.exit_application, background="red")
        # self.exitButton.pack(expand=YES)

        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "blue")
        self.picture_frame = Frame(self.master_screen, background="blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

    def takeBoundedScreenShot(self, x1, y1, x2, y2):
        im = pyautogui.screenshot(region=(x1, y1, x2, y2))
        # x = datetime.datetime.now()
        # fileName = x.strftime("%f")
        # im.save("capture.png")

    def createScreenCanvas(self):
        if self.isUsed==False:
            self.master_screen = Toplevel(root)
            self.master_screen.withdraw()
            self.master_screen.attributes("-transparent", "blue")
            self.picture_frame = Frame(self.master_screen, background="blue")
            self.picture_frame.pack(fill=BOTH, expand=YES)
            self.master_screen.withdraw()

            self.master_screen.deiconify()
            # root.withdraw()

            # user press key "s" to start screenshot mode
            # self.screenCanvas.destroy()
            # root.deiconify()
            print(self.master_screen.winfo_children())
            self.screenCanvas = Canvas(
                self.picture_frame, cursor="cross", bg="#add123")
            # self.screenCanvas.grid(row=0, column=0, sticky=NWSE)
            self.screenCanvas.pack(fill=BOTH, expand=YES)
            # self.screenCanvas.attributes('-fullscreen',True)
            # bind key "s" to change the background color

            self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)
            self.screenCanvas.bind("<B1-Motion>", self.on_move_press)
            self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)
            # Button(self.master_screen, text="Exit", command=self.display_rectangle).pack()
            self.master_screen.bind("<Escape>", self.exitScreenshotMode)

            self.master_screen.attributes('-fullscreen', True)
            self.master_screen.attributes('-alpha', 0.3)
            self.master_screen.lift()
            self.master_screen.attributes("-topmost", True)
            self.isUsed=True

    def on_button_release(self, event):

        x1 = min(self.start_x,  self.curX)
        y1 = min(self.start_y, self.curY)
        x2 = min(self.start_x,  self.curX)
        y2 = min(self.start_y, self.curY)

        self.takeBoundedScreenShot(
            x1, y1, x2, y2)
        # print(self.rect.winfo_children())

        self.master_screen.bind("<Escape>", self.exitScreenshotMode)
        self.master_screen.bind("<Return>", self.display_rectangle)

        # self.exitScreenshotMode()
        #  if user press key "s" to start screenshot mode
        return event

    def display_rectangle(self, event):
        # self.screenCanvas.destroy()
        # self.screenCanvas = Canvas(
        # self.picture_frame, bg="grey11")
        # self.master_screen.lift()

        # self.screenCanvas.config(state=DISABLED)
        # self.master_screen.config(state=DISABLED)

        self.screenCanvas.unbind("<ButtonPress-1>")
        self.screenCanvas.unbind("<B1-Motion>")
        self.screenCanvas.unbind("<ButtonRelease-1>")
        # self.screenCanvas.config(cursor="star")
        # self.master_screen.withdraw()
        # self.master_screen.attributes("-topmost", True)
        # self.master_screen.wm_attributes("-disabled", True)

        self.master_screen.config(bg='#add123')

        self.master_screen.wm_attributes('-transparentcolor', '#add123')
#  stay on top
        self.master_screen.wm_attributes('-topmost', True)

        # root.deiconify()
        self.master_screen.bind("<Escape>", self.exitScreenshotMode)
        keyboard.add_hotkey('Escape', self.temp)
        print("get in here")
        # root.deiconify()

    def temp(self):
        self.master_screen.update()
        self.screenCanvas.update()
        self.master_screen.bind("<Escape>", self.exitScreenshotMode)

    # def exit(self):
    #     self.screenCanvas.update()
    #     self.screenCanvas.destroy()

    #     # for each in self.master_screen.winfo_children():
    #     #     each.destroy()
    #     # self.master_screen.delete(ALL)

    #     self.master_screen.withdraw()
    #     root.deiconify()

    def exitScreenshotMode(self, event):
        # self.master_screen.wm_attributes('-topmost', False)
        self.isUsed=False
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        root.deiconify()

    def exit_application(self):
        print("Application exit")
        root.quit()

    def on_button_press(self, event):

        if self.rect != None:
            self.screenCanvas.delete(self.rect)
            # self.rect.destroy()
        self.start_x = self.screenCanvas.canvasx(event.x)
        self.start_y = self.screenCanvas.canvasy(event.y)

        self.rect = self.screenCanvas.create_rectangle(
            self.x, self.y, 1, 1, outline='red')
        # self.screenCanvas.delete(self.rect)
        # self.master_screen.config(bg='#add123')

    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.screenCanvas.coords(
            self.rect, self.start_x, self.start_y, self.curX, self.curY)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
