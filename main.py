import tkinter as tk
import pyautogui
import time
import random
import sys


class spambot():

    def __init__(self,message,amount,timestart):
        self.message = message
        self.amount = amount
        self.timestart = timestart
        self.count = 0

    def human(self):
        time.sleep(int(self.timestart))
        while self.count < int(self.amount):
            pyautogui.typewrite(str(self.message))
            pyautogui.press("enter")
            time.sleep(1.5)
            self.count += 1

    def nuker(self):
        time.sleep(int(self.timestart))
        for i in range(int(self.amount)):
            pyautogui.typewrite(self.message + '\n')
            time.sleep(0.5)

    def serverraper(self):
        time.sleep(int(self.timestart))
        for i in range(int(self.amount)):
            pyautogui.typewrite(self.message + '\n')



class gui():
    def __init__(self):
        ### STYLE ###
        self.color1 = "Green"
        self.color2 = "lightgreen"
        self.color3 = "Black"

        ### SPAMBOT ###
        self.message = "TEST"
        self.amount = 10
        self.timestart = 1



        ### DROPDOWN ###
        self.Methods = [
            "Tech Support",
            "2FastForFurious",
            "xXTheRxperXx"]
        self.method = 0

        self.Amounts = [10,25,50,100]

        ### GUI ###
        self.window = tk.Tk()
        self.window.title("Spambot v1 by Serpent")
        self.window.geometry("600x800")
        self.window['bg'] = "black"

        self.variable = tk.StringVar(self.window)
        self.variable.set(self.Methods[0])

        self.variable1 = tk.IntVar(self.window)
        self.variable1.set(self.Amounts[0])

        ### SUBTITLE ###
        self.subt = tk.Label(self.window, text="~SERP SPAMBOT~", bg=self.color3, fg=self.color2, font="Arial 25")
        self.subt2 = tk.Label(self.window, text="YOUTUBE : S3rp3nt", bg=self.color3, fg=self.color2, font="Arial 10")
        self.subt3 = tk.Label(self.window, text=" GITHUB  : serpent33", bg=self.color3, fg=self.color2, font="Arial 10")

        ### METHOD ###
        self.mthdsl = tk.Label(self.window, text="Method: ", bg=self.color3, fg=self.color2, font="Arial 13")
        self.mthds = tk.OptionMenu(self.window, self.variable, *self.Methods, command=self.mthdchange)
        self.mthds.config(width=13, font=('Helvetica', 12), highlightbackground=self.color1, highlightcolor=self.color1, bg="Black",fg="lightGreen")
        self.mthds["menu"].config(bg="Black", fg="lightGreen")

        ### AMOUNT ###
        self.amnts = tk.Label(self.window, text="Amount: ", bg=self.color3, fg=self.color2, font="Arial 13")
        self.amnt = tk.OptionMenu(self.window, self.variable1, *self.Amounts, command=self.amntchange)
        self.amnt.config(width=13, font=('Helvetica', 12), highlightbackground=self.color1, highlightcolor=self.color1, bg="Black",fg="lightGreen")
        self.amnt["menu"].config(bg="Black", fg="lightGreen")

        ### MESSAGE ###
        self.msgs = tk.Label(self.window, text="Message: ", bg=self.color3, fg=self.color2, font="Arial 13")
        self.msg = tk.Entry(self.window, bg=self.color3, fg=self.color2)
        self.msg.config(highlightbackground=self.color1, highlightcolor=self.color1)

        ### START ###
        self.btnstart = tk.Button(self.window, text="START", command=self.start, bg=self.color3, fg=self.color2)
        self.btnstart.config(highlightbackground=self.color1, highlightcolor=self.color1, width=30)

        ### EXIT ###
        self.btnexit = tk.Button(self.window, text="Exit", command=exit, bg=self.color3, fg=self.color2)
        self.btnexit.config(highlightbackground=self.color1, highlightcolor=self.color1)

        ### Version ###
        self.subt4 = tk.Label(self.window, text="Version : 1.0", bg=self.color3, fg=self.color2, font="Arial 10")

        ### PLACE ###
        self.subt.place(anchor="c", relx=.5, rely=0.035)
        self.subt2.place(anchor="c", relx=.5, rely=0.1)
        self.subt3.place(anchor="c", relx=.5, rely=0.12)
        self.mthdsl.place(anchor="c", relx=.4, rely=0.3)
        self.mthds.place(anchor="c", relx=.625, rely=0.3)
        self.amnts.place(anchor="c", relx=.4, rely=0.4)
        self.amnt.place(anchor="c", relx=.625, rely=0.4)
        self.msgs.place(anchor="c", relx=.4, rely=0.5)
        self.msg.place(anchor="c", relx=.625, rely=0.5)
        self.btnstart.place(anchor="c", relx=.5, rely=0.7)
        self.btnexit.place(anchor="c", relx=.5, rely=0.90)
        self.subt4.place(anchor="c", relx=.5, rely=0.96)

        self.window.mainloop()

    def start(self):
        self.message = self.msg.get()

        self.spam = spambot(self.message, self.amount,self.timestart)
        if self.method == 0:
            self.spam.human()
        if self.method == 1:
            self.spam.nuker()
        if self.method == 2:
            self.spam.serverraper()

    def mthdchange(self, value):
        if value == self.Methods[0]:
            self.method = 0
        elif value == self.Methods[1]:
            self.method = 1
        elif value == self.Methods[2]:
            self.method = 2

    def amntchange(self,value):
        self.amount = value

    def exit(self):
        sys.exit()



if __name__ == '__main__':
    gui = gui()