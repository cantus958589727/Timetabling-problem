from tkinter import *
import tkinter as tk

class GUI:
    frame = tk.Tk()

    def __init__(self,  TempList):
        self.frame.geometry("300x450")

        #-----------------------DEPARTMENT------------------------------
        Label(self.frame, text="What Department").grid(row = 0, sticky = W)

        selectedDepartment = tk.IntVar()

        STRadioButton = Radiobutton(self.frame, variable = selectedDepartment, value = 0, text = "CS - ST", command = lambda: print(selectedDepartment.get()))
        STRadioButton.grid(row = 1, sticky = W)
        NERadioButton = Radiobutton(self.frame, variable = selectedDepartment, value = 1, text = "CS - NE", command = lambda: print(selectedDepartment.get()))
        NERadioButton.grid(row = 2, sticky = W)
        CSERadioButton = Radiobutton(self.frame, variable = selectedDepartment, value = 2, text = "CS - CSE", command = lambda: print(selectedDepartment.get()))
        CSERadioButton.grid(row = 3, sticky = W)
        ITRadioButton = Radiobutton(self.frame, variable = selectedDepartment, value = 3, text = "IT", command = lambda: print(selectedDepartment.get()))
        ITRadioButton.grid( row = 4, sticky = W)
        ALLDepRadioButton = Radiobutton(self.frame, variable = selectedDepartment, value = 4, text = "ALL DEPARTMENT", command = lambda: print(selectedDepartment.get()))
        ALLDepRadioButton.grid( row = 5, sticky = W)


        #----------------------TERM------------------------------------------
        Label(self.frame, text = "What Term").grid(row = 0, column = 1, padx = 4)
        selectedTerm = tk.IntVar()
        TermOneRadioButton = Radiobutton(self.frame, variable = selectedTerm, value = 1, text = "Term 1", command = lambda: print(selectedTerm.get())).grid(row = 1, column = 1, padx = 4)
        TermTwoRadioButton = Radiobutton(self.frame, variable = selectedTerm, value = 2,text = "Term 2", command = lambda: print(selectedTerm.get())).grid(row = 2, column = 1, padx = 4)
        TermThreeRadioButton = Radiobutton(self.frame, variable = selectedTerm, value = 3,text = "Term 3", command = lambda: print(selectedTerm.get())).grid(row = 3, column = 1, padx = 4)

        #----------------------YEAR-----------------------------------------
        Label(self.frame, text = "What Year").grid(row = 0, column = 2, padx = 4)
        selectedYear = tk.IntVar()
        YearOneRadioButton = Radiobutton(self.frame, variable = selectedYear, value = 2015, text = "Year 2015", command = lambda: print(selectedYear.get())).grid(row = 1, column = 2, padx = 4)
        YearTwoRadioButton = Radiobutton(self.frame, variable = selectedYear, value = 2016,text = "Year 2016", command = lambda: print(selectedYear.get())).grid(row = 2, column = 2, padx = 4)
        YearThreeRadioButton = Radiobutton(self.frame, variable = selectedYear, value = 2017,text = "Year 2017", command = lambda: print(selectedYear.get())).grid(row = 3, column = 2, padx = 4)

        
        Button(self.frame, text = "Submit", command = lambda: self.ReturnTheList(selectedDepartment, selectedTerm, selectedYear, TempList )).grid(row = 6)
        
        self.frame.mainloop()

    def ReturnTheList(self, selectedDepartment, selectedTerm, selectedYear,TempList ):
        TempList.append(selectedDepartment.get())
        TempList.append( selectedTerm.get())
        TempList.append(selectedYear.get())
        self.frame.quit()
        self.frame.destroy()
    
