__author__ = 'linuxsagar'
from Tkinter import *
import os
from easygui import msgbox
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.init_window()

    def init_window(self):
        #self.instruction = Label(self,text="Enter Video URL")
        #self.instruction.grid(row=0,columnspan=2,sticky=W)

        self.urlLabel = Label(self,text="URL")
        self.urlLabel.grid(row=1,column=0,sticky=W)

        display = StringVar()
        self.url = Entry(self, relief=FLAT, textvariable=display, justify='left',bd=2,bg='white')
        self.url.grid(row=1,column=2,sticky=W)

        self.downloadButton = Button(self,text="Download",command=self.startDownload)
        self.downloadButton.grid(row=2,column=0,sticky=W)

        self.cancleButton = Button(self,text="Quit",command=self.quitApp)
        self.cancleButton.grid(row=3,column=2,sticky=W)
    
    def startDownload(self):
        vUrl = self.url.get()
        if vUrl != "":
            command = "youtube-dl "+vUrl
            os.system(command)
        else:
            msgbox("Download Started")
    def quitApp(self):
        exit()


if __name__ == "__main__":
    root = Tk()
    root.title("Downloader")
    root.geometry("500x80")
    root.resizable(0, 0)
    app = Window(root)
    root.mainloop()
