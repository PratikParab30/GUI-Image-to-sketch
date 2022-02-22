from tkinter import *
from tkinter import Tk
import cv2
import os
import re

tk=Tk()
tk.geometry("800x800")
tk.title("ImageToSketchConverter")
tk.config(bg="#a83285")
folpath=StringVar()

labl1=Label(tk,text="Please peovide path:")
labl1.grid(row=1,column=1)
fpg=Entry(tk,textvariable=folpath)
fpg.grid(row=1,column=2)
    
def fun2():
    labl2=Label(tk,text="This is not  valid folder,try again!")
    labl2.grid(row=3,column=1)
    
def fun3():
    labl3=Label(tk,text=f"Total {flct} file are created")
    labl3.grid(row=5,column=1)
    
def fun4():
    labl4=Label(tk,text="Zero file created,please check original file location")
    labl4.grid(row=7,column=1)

tk.mainloop()

def imgcvt(path,nf):
    imr=cv2.imread(path)
    gray=cv2.cvtColor(imr,cv2.COLOR_BGR2GRAY)
    gray2=255-gray
    blr=cv2.GaussianBlur(gray2,(21,21),0) 
    blr2=255-blr 
    sketch=cv2.divide(gray,blr2,scale=256.0)
    svpath=nf+"/"+path
    cv2.imwrite(svpath,sketch)

while True:
    fun1()
    if os.path.isdir(folpath.get()):
        break
    else:
        fun2()
        
os.chdir(folpath.get())
nf="MySketch"
os.mkdir(nf)
dirr=os.listdir()
flct=0
for path in dirr:
    if os.path.isfile(path):
            if (re.match(".*.jpg",path) or re.match(".*.png",path)):
                imgcvt(path,nf)
                flct+=1
                
if flct !=0:
    fun3()
else:
    fun4()

