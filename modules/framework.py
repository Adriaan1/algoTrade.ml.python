import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


#***********************************************************
# Function loadFile()
#***********************************************************
# Description
# Load File
# https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-list-in-python
#***********************************************************
def loadFile():
    # Ask user to browse for filename and return filename to program
    filename = filedialog.askopenfilename()
    # Load file
    file = open(filename,"r")
    content = file.read()
    # Prepare message to dislplay on message box
    message = "File " + filename + " loaded into memory"
    # Show message box
    messagebox.showinfo("Loading File", message)
    # Show content
    messagebox.showinfo("File Content", content)
    # Try to convert to list
    content_list = content.split(",")
    for value in content_list :
        if not value.isnumeric() :
            messagebox.showerror("Error", "File contents are not in correct format")
            messagebox.showinfo("Tip", "File contents must contain a numberic list such as 20,33,2,506")
            break
    

#***********************************************************
# Function showWindow
#***********************************************************
# Description
# p_window      Window name
#***********************************************************
def showWindow(p_window):
    if p_window == "main":
        # Create the window
        window = tk.Tk()   
        # Log to console                             
        print('The type of variable window is ' + str(type(window)))     
        # Change window title  
        window.title("Forex Quantitative Analysis")   
        # Create button   
        button1 = tk.Button(text="Load File", 
                            foreground="black",
                            background="#34A2FE",
                            width=20,
                            command = loadFile)
        # Add button to window
        button1.pack()
        window.mainloop()                               # Call the mainloop to keep window visible