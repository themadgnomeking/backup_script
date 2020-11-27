# from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askopenfilename

'''
Tk().withdraw()
filename = askopenfilename()
print(filename)
'''

startFolderLocation = []
backupFolderLocation = []


root = Tk()
root.geometry("400x300")
frame = Frame(root)
frame.pack()
 
leftframe = Frame(root)
leftframe.pack(side=LEFT)
 
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
 
label = Label(frame, text = "Backup Controls")
label.pack()
 
button1 = Button(leftframe, text = "Start Folder")
button1.pack(padx = 3, pady = 3)
button2 = Button(rightframe, text = "Destination Folder")
button2.pack(padx = 3, pady = 3)
 
root.title("Backup Script")
root.mainloop()


