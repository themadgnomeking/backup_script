#choose backup location folder
#choose destination folder including drive
#copy files in the folder to destination folder
#GUI interface to select items
#setup an automated time to backup files or change

from tkinter import filedialog
from tkinter import *
import os


class backup_files:

    def __init__(self):
    #define the window parameters
        root = Tk()
        root.geometry("400x300")
        frame = Frame(root)
        frame.pack()

        label = Label(frame, text = "Backup Controls")
        label_backup_location = Label(frame, text = "Pick a folder to backup", )
        label.pack()
        label_backup_location.pack()
    


    #define parameters of the buttons
        selected_folder = []
        destination_folder = []

        def selectFolder(bool):
            #root = Tk()
            current_drecitory = filedialog.askdirectory()
            file_path = os.path.join(current_drecitory)
            
            if True:
                selected_folder.append(file_path)
                return "You've selected a folder to backup"
            else:
                destination_folder.append(file_path)
                return "You've selected the backup location"
            #selected_folder.append(file_path)
            return file_path

        def backupCommand():
            #copy files from start location
            #paste files to destination location
            #return a message when it's done
            #message will display date and time when it's done
            return "Your files are backed up"
            
        button1 = Button(root, text="Select folder to backup", command = selectFolder(False))
        button1.pack()

        button2 = Button(root, text="Select destination folder", command = selectFolder(True))
        button2.pack()

        root.title("Backup Script")
        root.mainloop()

    #-----------------------------
    selected_folder = []
    destination_folder = []
    #button for select start folders, destination folder, save auto backup, manual backup

    
    def backup_folder_location(self):
        destination_folder = []

    #store the backup folders in an array/list for multiple backup locaitons
    #copy the files in the location
    
    #store the destination folder in an array/list for multiple target locations
    #paste the files in the target locations
    #create a variable of when backups were perfored
    #store them in an array/list
backup_files()