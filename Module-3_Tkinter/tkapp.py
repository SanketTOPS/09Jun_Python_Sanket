import tkinter
from tkinter import Button, ttk, messagebox

screen=tkinter.Tk()
screen.title("FirstApp")
screen.config(bg='lightblue')
screen.geometry("500x600")

#tkinter.Label(text="Firstname:",bg='lightblue',font='Candara 15').pack()
#tkinter.Label(text="Lastname:",bg='lightblue',font='Candara 15').pack()

#tkinter.Label(text="Firstname:",bg='lightblue',font='Candara 15').place(x=0,y=0)
#tkinter.Label(text="Lastname:",bg='lightblue',font='Candara 15').place(x=0,y=30)

tkinter.Label(text="Firstname:",bg='lightblue',font='Candara 15').grid(row=0,column=0,sticky='W')
tkinter.Label(text="Lastname:",bg='lightblue',font='Candara 15').grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1)
tkinter.Entry().grid(row=1,column=1)

tkinter.Radiobutton(text='Male',value=0,bg='lightblue',font='Candara 15').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(text='Female',value=1,bg='lightblue',font='Candara 15').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text="Python",bg='lightblue',font='Candara 15').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text="iOS",bg='lightblue',font='Candara 15').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text="JAVA",bg='lightblue',font='Candara 15').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text="PHP",bg='lightblue',font='Candara 15').grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Surat','Baroda','Jamnagar','Bhavnagar']
ttk.Combobox(values=city).grid(row=7,column=0)

def btnclick():
    #print("Button is clicked!")
    #messagebox.showerror("Error","Somthing went wrong...Try again!")
    #messagebox.showwarning("Warning","Your disk is full!")
    #messagebox.showinfo("Success","Your account has been created!")

    #messagebox.askokcancel("Download","Do you want to continue?")
    #messagebox.askyesno("Download","Do you want to continue?")
    #messagebox.askquestion("Download","Do you want to continue?")
    #messagebox.askretrycancel("Download","Do you want to continue?")
    messagebox.askyesnocancel("Download","Do you want to continue?")


tkinter.Button(text="Submit",font='Candara 15',command=btnclick).place(x=200,y=300)

screen.mainloop()