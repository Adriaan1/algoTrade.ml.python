import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Text
from tkinter import Frame
from tkinter import Scrollbar
from tkinter import Label
import numpy
from scipy import stats

#***********************************************************************************
#***********************************************************************************
# CLASS main
#***********************************************************************************
# Description
# Basically this is the class for the main window,
# starting with the basic window and adding widgets
#***********************************************************************************
#***********************************************************************************
class main:

    # Protected class attributes
    _fileContent = ""   # The content of a file loaded into memory
    _contentList = []   # The content of the file in list format loading into memory

    #*******************************************************************************
    # Constructor
    #*******************************************************************************
    # Description
    # Initialize the application by creating the main window
    # and creating all the widgets
    #*******************************************************************************
    def __init__(self): 
        # Log to console                             
        # print('The type of variable window is ' + str(type(window)))   

        # Create the window
        self.window = tk.Tk()

        # Set default size of the window
        self.window.geometry("800x640")  

        # Change window title  
        self.window.title("Forex Quantitative Analysis")   

        # Create a button Frame
        buttonFrame = Frame(self.window)
        # Add the button frame to the window
        buttonFrame.pack()

        # Create button 1   
        self.button1 = tk.Button(buttonFrame,
                            text="Load File", 
                            foreground="black",
                            background="#34A2FE",
                            width=20,
                            command = self.loadFile)
        # Add button to button frame
        self.button1.grid(row=1,column=0)   

        # Create button 2
        self.button2 = tk.Button(buttonFrame,
                            text="Calc Mean", 
                            foreground="black",
                            background="#34A2FE",
                            width=20,
                            state='disabled',
                            command = self.calcMean)

        # Add button to button frame
        self.button2.grid(row=1,column=1)   

        # Create a textbox frame for the first textbox
        textboxFrame1 = Frame(self.window, height = 600, width = 800)
        # Add the frame to the window below the previous widgets
        textboxFrame1.pack()

        # Create scrollbar for first textbox in the first textbox frame
        scroll1 = Scrollbar(textboxFrame1)   
        # Add scrollbar to the textbox frame, keeping it to the right
        scroll1.pack(side='right',fill='y')

        # Create first textbox to be in the first textbox frame
        self.textbox1 = Text(textboxFrame1, height = 30, width = 80, wrap='word', yscrollcommand=scroll1.set)     
        # Place the textbox into the textbox frame, keeping it the left
        self.textbox1.pack(side='left')           
        # Configure the scrollbar
        scroll1.config(command=self.textbox1.yview)

        # Create a frame for the label
        labelFrame = Frame(self.window, height = 20, width = 800)
        labelFrame.pack()

        # Create a label and add it to the window next.
        terminalLabel = Label(labelFrame, text='Terminal')
        terminalLabel.place(x=70,y=1)

        # Create a textbox frame for the second textbox
        textboxFrame2 = Frame(self.window, height = 200, width = 800)
        # Add the frame to the window below the previous widgets
        textboxFrame2.pack()

        # Create scrollbar for second textbox in the second textbox frame
        scroll2 = Scrollbar(textboxFrame2)   
        # Add scrollbar to the textbox frame, keeping it to the right
        scroll2.pack(side='right',fill='y')

        # Create second textbox to be in the second textbox frame
        self.textbox2 = Text(textboxFrame2, height = 5, width = 80,  wrap='word', yscrollcommand=scroll2.set)     
        # Place the textbox into the textbox frame, keeping it the left
        self.textbox2.pack(side='left')           
        # Configure the scrollbar
        scroll2.config(command=self.textbox2.yview)
        # Insert first terminal prompt
        self.textbox2.insert(tk.END,'> ')
        self.textbox2.configure(state="disabled") # Don't allow user to change

    #*******************************************************************************
    # Private Method __setFileContent(fileContent)
    #*******************************************************************************
    # Description
    # Set the protected class attribute _fileContent
    #*******************************************************************************   
    def __setFileContent(self, fileContent):
        self._fileContent = fileContent

    #*******************************************************************************
    # Private Method __setContentList(contentList)
    #*******************************************************************************
    # Description
    # Set the protected class attribute _contentList
    #*******************************************************************************   
    def __setContentList(self, contentList):
        self._contentList = [float(i) for i in contentList]

    #*******************************************************************************
    # Public Method getFileContent
    #*******************************************************************************
    # Description
    # Get the protected class attribute _fileContent
    #*******************************************************************************  
    def getFileContent(self):
        return self._fileContent

    #*******************************************************************************
    # Public Method getContentList
    #*******************************************************************************
    # Description
    # Get the protected class attribute _contentList
    #*******************************************************************************  
    def getContentList(self):
        return self._contentList

    #*******************************************************************************
    # Public Method validateContent
    #*******************************************************************************
    # Description
    # Validates that the content of a string is CSV and also only has numeric values.
    #*******************************************************************************  
    def validateContent(self,contentString):
        valid = True
        contentList = contentString.split(",")
        for value in contentList :
            if not value.isnumeric() :
                valid = False
                break
        if valid:
            self.__setFileContent(contentString)
            self.__setContentList(contentList)
        return valid

    #*******************************************************************************
    # Public Method loadFile()
    #*******************************************************************************
    # Description
    # Load File
    # https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-list-in-python
    #*******************************************************************************
    def loadFile(self):
        
        # Ask user to browse for filename and return filename to program
        filename = filedialog.askopenfilename()
        # Load file
        file = open(filename,"r")
        content = file.read()
        # Prepare message to dislplay on message box
        message = "File " + filename + " loaded into memory"
        # Show message box
        #messagebox.showinfo("Loading File", message)
        if (self.validateContent(content)) :

            # Show file inside textbox
            self.textbox1.delete(1.0,tk.END) # Clear contents
            self.textbox1.insert(tk.END,self.getFileContent()) # Insert file contents

            # Show info in terminal window
            self.textbox2.configure(state='normal') # Enable temporarily to show info
            self.textbox2.insert(tk.END,"Loading file...\n")
            self.textbox2.insert(tk.END, "> ")
            self.textbox2.insert(tk.END,message)
            self.textbox2.insert(tk.END, "\n> ")
            self.textbox2.configure(state="disabled") # Don't allow user to change
            self.button2.configure(state='normal')

        else:
            messagebox.showerror("Error", "File contents are not in correct format")
            messagebox.showinfo("Tip", "File contents must contain a numberic list such as 20,33,2,506")

    #*******************************************************************************
    # Public Method calcMean()
    #*******************************************************************************
    # Description
    # Calculate the mean value
    #*******************************************************************************
    def calcMean(self):
        contentList = self.getContentList()
        mean = numpy.mean(contentList)
        self.textbox2.configure(state='normal') # Enable temporarily to show info
        self.textbox2.insert(tk.END,"Calculating mean value...\n> ")
        self.textbox2.insert(tk.END,"Mean value is: ")
        self.textbox2.insert(tk.END,mean)
        self.textbox2.insert(tk.END,"\n> ")


