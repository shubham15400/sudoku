from tkinter import *
import pathlib
import os
import pickle
from subprocess import call
class Account:
    def __init__(self,no,name,typ,amt):
        self.accno=no
        self.name=name
        self.type=typ
        self.amt=amt


def depo():
    flag=False
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accno == int(e1.get()) :
                amount = int(e2.get())
                item.amt += amount
                flag=True
    else :
        call(["python","noaccountfound.py"])
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    if(flag):
        call(["python","accountupdate.py"])
        ROOT.destroy()
    
ROOT= Tk()
Label(ROOT,text='Account No').grid(row=0)
Label(ROOT,text = 'Amount').grid(row=1)
e1=Entry(ROOT)
e1.grid(row=0,column=1)
e2=Entry(ROOT)
e2.grid(row=1,column=1)
Button(ROOT,text = 'Deposit',width=20,command = depo).grid(row=2)
Button(ROOT,text = 'Exit' ,width=20,command = ROOT.destroy).grid(row=2,column=1)


ROOT.mainloop()