__author__ = 'linuxsagar'
from Tkinter import *
import os
from easygui import msgbox
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.init_window()

    def init_window(self):
        self.grid()
        #self.instruction = Label(self,text="Enter Video URL")
        #self.instruction.grid(row=0,columnspan=2,sticky=W)

        self.urlLabel = Label(self,text="Video URL")
        self.urlLabel.grid(row=1,column=0,sticky=W)

        display = StringVar()
        self.url = Entry(self, relief=FLAT, textvariable=display, justify='left',bd=2,bg='white',width=45)
        self.url.grid(row=1,column=2,sticky=W,padx=2,pady=2)

        self.downloadButton = Button(self,text="Download",command=self.startDownload)
        self.downloadButton.grid(row=2,column=2,sticky=NSEW,padx=2,pady=2)

        self.quitButton = Button(self,text="Quit",command=lambda: self.quit())
        self.quitButton.grid(row=3,column=2,sticky=E,padx=2,pady=2)

    def startDownload(self):
        vUrl = self.url.get()
        if vUrl != "" and vUrl.startswith("https://youtube.com"):
            command = "youtube-dl "+vUrl
            os.system(command)
            msgbox("Download Started")
        else:
            msgbox("Enter valid url")
    # def quitApp(self):
    #     exit()


if __name__ == "__main__":
    root = Tk()
    root.title("Downloader")
    root.geometry("450x95")
    root.resizable(0, 0)
    app = Window(root)
    root.mainloop()
