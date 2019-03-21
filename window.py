from tkinter import *
from tkinter import filedialog
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text = "Quit", command = self.client_exit)
        quitButton.place(x=0,y=0)
        choose_file = Button(self, text = "Select file", command = self.askopenfilename)
        choose_file.place(x=50, y=0)
        # my_file = filedialog.askopenfilename(parent=root, title = "Choose a file")
        # print(my_file)

    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()