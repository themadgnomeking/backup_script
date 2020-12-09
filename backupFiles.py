#choose backup location folder
#choose destination folder including drive
#copy files in the folder to destination folder
#GUI interface to select items
#setup an automated time to backup files or change

from tkinter import filedialog
from tkinter import *
import os
import shutil


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
        selected_folder = ""
        destination_folder = ""

        def selectFolder():
            #root = Tk()
            current_directory = filedialog.askdirectory()
            selected_folder = os.path.join(current_directory)
            #selected_folder.append(file_path)
            return selected_folder
        
        def selectDestinationFolder():
            current_directory = filedialog.askdirectory()
            destination_folder = os.path.join(current_directory)
            return destination_folder + "you have selected the destination folder"

        def backupCommand():
            #copy files from start location
            #paste files to destination location
            #return a message when it's done
            #message will display date and time when it's done
            

            return "Your files are backed up"
            
        button1 = Button(root, text="Select folder to backup", command = selectFolder)
        button1.pack()

        button2 = Button(root, text="Select destination folder", command = selectDestinationFolder)
        button2.pack()

        root.title("Backup Script")
        root.mainloop()

    #-----------------------------
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