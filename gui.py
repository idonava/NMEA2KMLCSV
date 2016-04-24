#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

class Radiobar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.var = StringVar()
        for pick in picks:
            rad = Radiobutton(self, text=pick, value=pick, variable=self.var)
            rad.pack(side=side, anchor=anchor, expand=YES)
    def state(self):
        return self.var.get()
class Checkbar(Frame):



    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
def state(self):
    return map((lambda var: var.get()), self.vars)


def allstates():
    print(list(lng.state()), list(tgl.state()))


def chooseFoler():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(filename)


def callback():
    name = askopenfilename()
    print(name)


def chooseFile():
    Tk().withdraw()
    file_path = filedialog.askopenfilename()
    print(file_path)


if __name__ == '__main__':

   root = Tk()
   root.title('NMEA to KML/CSV - By R.I.O')
   fileButton = Button(text='Select File', command=callback).pack(side=LEFT)
   T = Text(root, height=1, width=30)
   T.pack()
   T.insert(END, "Select File ot Folder\n")

   Button(text='Select Folder', command=callback, height=1, width=30).pack(side=RIGHT)

   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)

   lng = Checkbar(root, ['Time', 'Latitude', 'Longtitude', 'Quality', 'NOS', 'HDOP', 'HOG', 'Speed', 'date'])
   tgl = Checkbar(root, ['CSV','KML'])
   lng.pack(side=TOP,  fill=X)
   tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)
   gui = Radiobar(root, ['File', 'Folder'], side=LEFT)

   gui.pack(side=LEFT, fill=Y)
   gui.config(relief=GROOVE, bd=2)
   errmsg = 'Error!'
   root.mainloop()
