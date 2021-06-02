import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Text
from tkinter import Frame

#***********************************************************
# Class framework
#***********************************************************
# Description
# Basically this is the class for the entire application,
# starting with the basic window and adding widgets
#***********************************************************
class framework:

    # Protected class attributes
    _fileContent = ""   # The content of a file loaded into memory

    #***********************************************************
    # Constructor
    #***********************************************************
    # Description
    # Initialize the application by creating the main window
    # and creating all the widgets
    #***********************************************************
    def __init__(self, p_window):
        if p_window == "main":  
            # Log to console                             
            #print('The type of variable window is ' + str(type(window)))   
            # Create the window
            self.window = tk.Tk()
            # Set default size of the window
            self.window.geometry("800x640")  
            # Change window title  
            self.window.title("Forex Quantitative Analysis")   
            buttonFrame = Frame(self.window)
            buttonFrame.pack()

            # Create button 1   
            button1 = tk.Button(buttonFrame,
                                text="Load File", 
                                foreground="black",
                                background="#34A2FE",
                                width=20,
                                command = self.loadFile)
            # Add button to window
            button1.grid(row=1,column=0)   
            button2 = tk.Button(buttonFrame,
                                text="Calc Median", 
                                foreground="black",
                                background="#34A2FE",
                                width=20,
                                command = self.loadFile)
            # Add button to window
            button2.grid(row=1,column=1)        
            self.textbox = Text(self.window, height = 500, width = 800)     
            self.textbox.pack()                      

    #***********************************************************
    # Private Method __setFileContent(fileContent)
    #***********************************************************
    # Description
    # Set the protected class attribute _fileContent
    #***********************************************************   
    def __setFileContent(self, fileContent):
        self._fileContent = fileContent

    #***********************************************************
    # Private Method __setFileContent(fileContent)
    #***********************************************************
    # Description
    # Set the protected class attribute _fileContent
    #***********************************************************  
    def getFileContent(self):
        return self._fileContent

    #***********************************************************
    # Method loadFile()
    #***********************************************************
    # Description
    # Load File
    # https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-list-in-python
    #***********************************************************
    def loadFile(self):
        # Ask user to browse for filename and return filename to program
        filename = filedialog.askopenfilename()
        # Load file
        file = open(filename,"r")
        content = file.read()
        self.__setFileContent(content)
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
                error = True
                break
        if error is True:
           # Show file inside textbox
            self.textbox.insert(tk.END,self.getFileContent())
            
    
 

#***********************************************************
# Function showWindow
#***********************************************************
# Description
# p_window      Window name
#***********************************************************
def showWindow(p_window):
    fm = framework(p_window)
    # Call the mainloop to keep window visible
    fm.window.mainloop()      