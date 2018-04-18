#!/usr/bin/python

import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
    import Tkinter as tk
    import Tkinter as ttk
else:
    from tkinter import *
    import tkinter as tk

from pswebcam import getface, gettakePicture 
from psfingerprintcheck import checkFingerImage
Large_Font = ("Verdana", 18)
Small_Font = ("Verdana", 12)

act = '12'
pin = '12'
actNum ='default'


class ATM(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "ATM Simulator")

        #tk.Tk.iconbitmap(self, default = "atm.ico")
	self.var=StringVar()
	self.var.set("defaultt")
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
    
    def setVar(self,vari):
	self.var.set(vari)
	#self.update_idletasks()


    def getVar(self):
	return self.var.get()

class LogIn(tk.Frame):
    def __init__(self, parent, controller):

        global actEntry
        global pinEntry
	self.controller = controller
        tk.Frame.__init__(self, parent)

        logLabel = ttk.Label(self, text = "Login With Your Account Number and Pin", font = Large_Font)
        logLabel.pack(side = TOP, anchor = N, expand = YES)


        actLabel = Label(self, text = 'Account Number:')
        pinLabel = Label(self, text = 'Name : ')

        actEntry = Entry(self)
        pinEntry = Entry(self)

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
	self.controller.setVar(pinNum)
#        if actNum == act and pinNum == pin:
	self.controller.show_frame(WelcomePage)


class WelcomePage(tk.Frame):

    #Welcome Page Window

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Welcome to the ATM Simulator", font = Large_Font)
        label.pack(pady=100, padx=100)
	self.controller = controller
	label2 = ttk.Label(self, textvariable=self.controller.getVar(),font=Large_Font)

        label.pack(pady=100, padx=100)


        checkButton = ttk.Button(self, text = "Take Picture", 
                             command = self.talkPic )
        checkButton.pack()
        quitButton = ttk.Button(self, text = "End Transaction", command = self.client_exit)
        quitButton.pack()

    def client_exit(self):
        exit()
    
    def talkPic(self):
	gettakePicture(self.controller.getVar())
	if ( getface(self.controller.getVar()) == True ):
		self.controller.show_frame(Savings)
	else:
		self.controller.show_frame(Login)
    
class Checking(tk.Frame):

    #Checking Account Window

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "successfully Authenticated to  Account", font = Large_Font)
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
        label = ttk.Label(self, text = "Fingerprint Auth", font = Large_Font)
        label.pack(pady=100, padx=100)
	
        homeButton = ttk.Button(self, text = "Finger printAuth", 
                             command = self.fingerAuth() )   
        homeButton.pack()
        quitButton = ttk.Button(self, text = "End Transaction", command = quit)
        quitButton.pack()

    def fingerAuth(self):
	if( checkFingerImage(self.controller.getVar()) == True ):
		self.controller.show_frame(Checking)
	else:
		self.controller.show_frame(Login)

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
