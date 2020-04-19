from tkinter import *
from tkinter import ttk
from tkinter import messagebox,dialog
import os, shutil
root = Tk()
root.geometry("800x550")
root.configure(pady = 60,bg = "grey")
root.title("DirectoryMaker")
root.wm_iconbitmap("icon.ico")

# functionality
def submit():
    extension_direc = {
        "audios": {".mp3", ".m4a", ".wav", ".flac"},
        "videos": {"mp4", ".mkv", ".MKV", ".flv", ".mpeg"},
        "documents": {".doc", ".pdf", ".txt"},
        "pictures": {".jpg", ".jpeg", ".jfif", ".gif", ".png"},
        "compress": {".rar", ".zip", ".sitx"},
        "applications": {".exe"}
    }
    if stringvar.get() != "":
        folderpath = stringvar.get()

        def file_finder(folder_path, file_extension):
            files = []
            for file in os.listdir(folder_path):
                for extension in file_extension:
                    if file.endswith(extension):
                        files.append(file)

            return files

    # print(file_finder(folderpath,extension_direc["audios"]))

        for extension_name, extension_type in extension_direc.items():
            c = file_finder(folderpath, extension_type)
            if len(c) > 0:
                folder_name = extension_name
                folder_path = os.path.join(folderpath, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                for item in file_finder(folderpath, extension_type):
                    item_path = os.path.join(folderpath, item)
                    item_new_path = os.path.join(folder_path, item)
                    shutil.move(item_path, item_new_path)

    else:
        messagebox.showerror("Directorymaker","Please Enter Path")


    return exit()






# frames
frame1 = Frame(bg = "#00bcd4")
frame1.pack()
frame2 = Frame(bg = "white")
frame2.pack()


#icon
image_icon = PhotoImage(file = "icons2/2.png")
submit_ = PhotoImage(file = "icons2/ok.png")
folder_icon = PhotoImage(file = "icons2/open.png")

#labels
label1 = Label(frame1,image = image_icon)
label2 = Label(frame2,text = "Enter folder name",font = "Helvetica 13 bold")
stringvar = StringVar()
label3 = Entry(frame2,width = 30,textvariable = stringvar,relief = "sunken",bd = 2)

# buttons
submit_button = Button(frame2,image = submit_,command = submit)
# folder_button = Button(frame2,image = folder_icon,command ="folder")

# lables pack
label1.pack(pady = 20,padx = 100)
label2.pack(pady = 30,padx = 50)
label3.pack(pady = 30)

# buttons pack
# folder_button.pack(side = "left",padx = 50)
submit_button.pack(pady = 10)



root.mainloop()