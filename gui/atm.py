#!/usr/bin/python

import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
    import Tkinter as tk
    import Tkinter as ttk
else:
    from tkinter import *
    import tkinter as tk

Large_Font = ("Verdana", 18)
Small_Font = ("Verdana", 12)

act = '12'
pin = '12'


class ATM(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "ATM Simulator")

        #tk.Tk.iconbitmap(self, default = "atm.ico")

        container = tk.Frame(self)
        container.pack(side = "top", fill ="both", expand =True)
        container.grid_rowconfigure(100, weight=1)
        container.grid_columnconfigure(100, weight=1)

        self.frames = {}

        for i in (LogIn, WelcomePage, Checking, Savings, Transfer):

            frame = i(container, self)
            self.frames[i] = frame 
            frame.grid(row= 100, column = 100, sticky= "nsew")

        self.show_frame(LogIn)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LogIn(tk.Frame):
    def __init__(self, parent, controller):

        global actEntry
        global pinEntry

        tk.Frame.__init__(self, parent)

        logLabel = ttk.Label(self, text = "Login With Your Account Number and Pin", font = Large_Font)
        logLabel.pack(side = TOP, anchor = N, expand = YES)


        actLabel = Label(self, text = 'Account Number:')
        pinLabel = Label(self, text = 'PIN Number: ')

        actEntry = Entry(self)
        pinEntry = Entry(self, show ="*")

        actLabel.pack(pady =10, padx = 10, side = TOP, anchor = N)
        pinLabel.pack(pady =5, padx = 10, side = TOP, anchor  = S)

        actEntry.pack(pady =10, padx = 10, side = TOP, anchor = N)
        pinEntry.pack(pady =5, padx = 10, side = TOP, anchor  = S)

        #  runs the 'LoginCheck' function

        logInButton = ttk.Button(self, text = "Enter",
                                 command = self.LogInCheck)
        logInButton.pack(side = TOP, anchor = S)

        quitButton = ttk.Button(self, text = "Quit", command = quit)
        quitButton.pack(side = BOTTOM, anchor = S)

    def LogInCheck(self):
        actNum = actEntry.get()
        pinNum = pinEntry.get()

        if actNum == act and pinNum == pin:
            self.show_frame(WelcomePage)
        else: 
            return
            self.show_frame(LogIn)


class WelcomePage(tk.Frame):

    #Welcome Page Window

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Welcome to the ATM Simulator", font = Large_Font)
        label.pack(pady=100, padx=100)

        checkButton = ttk.Button(self, text = "Checking Account", 
                             command = lambda: controller.show_frame(Checking))
        checkButton.pack()

        saveButton = ttk.Button(self, text = "Savings Account", 
                            command = lambda: controller.show_frame(Savings))
        saveButton.pack()

        transButton = ttk.Button(self, text = "Transfer Funds", 
                            command = lambda: controller.show_frame(Transfer))
        transButton.pack()

        quitButton = ttk.Button(self, text = "End Transaction", command = self.client_exit)
        quitButton.pack()

    def client_exit(self):
        exit()

class Checking(tk.Frame):

    #Checking Account Window

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Checking Account", font = Large_Font)
        label.pack(pady=100, padx=100)

        homeButton = ttk.Button(self, text = "Back to Home Page", 
                             command = lambda: controller.show_frame(WelcomePage))   
        homeButton.pack()
        quitButton = ttk.Button(self, text = "End Transaction", command = quit)
        quitButton.pack()


class Savings(tk.Frame):

    #Savings Account Window

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text = "Savings Account", font = Large_Font)
        label.pack(pady=100, padx=100)

        homeButton = ttk.Button(self, text = "Back to Home Page", 
                             command = lambda: controller.show_frame(WelcomePage))   
        homeButton.pack()
        quitButton = ttk.Button(self, text = "End Transaction", command = quit)
        quitButton.pack()


class Transfer(tk.Frame):

    #Transfer Funds Window

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text = "Transfer Funds", font = Large_Font)
        label.pack(pady=100, padx=100)

        homeButton = ttk.Button(self, text = "Back to Home Page", 
                             command = lambda: controller.show_frame(WelcomePage))   
        homeButton.pack()
        quitButton = ttk.Button(self, text = "End Transaction", command = quit)
        quitButton.pack()

atm = ATM()
atm.mainloop()    
