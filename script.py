import numpy as np
import math
from random import randrange
from tkinter import* 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from random import randrange


# initialisation of a basic window with minimize button ...

angle = 0
speed = 20
WIDTH = 500
HEIGHT = 500
X1rec = WIDTH/2 - 20
Y1rec = HEIGHT/2 - 20
X2rec = X1rec + 20
Y2rec = Y1rec + 20
X1Line = 0
Y1Line = 0
X2Line = 0
Y2Line = 0
Name = str()
test = "vh"
button = False
## calculate the coorrdenate of the pool stick
def calculateLinePosition():
    global X1Line
    X1Line = X1rec +(X2rec - X1rec)/2
    global Y1Line
    Y1Line = Y1rec +(Y2rec - Y1rec)/2
    global X2Line
    X2Line = X1Line + 100*math.sin(angle*math.pi/180)
    global Y2Line
    Y2Line = Y1Line + 100*math.cos(angle*math.pi/180)

    
calculateLinePosition()

def evaluateimpact():
    global Name 
   
    
    if  Y1rec - float(speed)*math.cos(angle*math.pi/180) > HEIGHT - 60:#when the ball hits the downside side 
        Name=Name+ test[1] 
    if  Y1rec - float(speed)*math.cos(angle*math.pi/180) <=0:#when the ball hits the upperside side
        Name=Name+ test[1]
     
    if X1rec - float(speed)*math.sin(angle*math.pi/180) > WIDTH - 20:#when the ball hits the rightside side
        Name=Name+ test[0]
    if X1rec - float(speed)*math.sin(angle*math.pi/180) <=0:#when the ball hits the leftside side
        Name=Name+ test[0]
evaluateimpact()



root = Tk()#creating and openning a window
root.title("Billard Simulation")
#root.iconbitmap(r'C:\Users\AMGHAR MED CHERIF\Desktop\logo.ico')
root.geometry("800x600")#size of the window 
#creatin a frame for the buttons in th bottom

bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

#giv a name to our window

thelabel=Label(root,text="square case billard simulation") 
thelabel.pack()

#creating buttons (pause and restart buttons )
def pause(event):#function of the button 
    global button
    button = False
    
Pause=Button(bottomFrame,text="Pause",fg="Blue")
Pause.bind(" <Button-1>",pause)
Pause.pack(fill=X)
def Start(event):#function of the button
    global button
    button = True
restart=Button(bottomFrame,text="Start",fg="Green")
restart.bind("<Button-1>",Start)
restart.pack(fill=X)

#creating entries ( angle)

label1=Label(root,text="please choose an angle to start with then press enter")#title of the entry
label1.pack()

#obtaining data from our entry  

def evaluateangle(event):
    print("Evaluatin angle " )
    global angle
    
    
    entry = entrySpace.get()
    if entry :
        angle = float(entry)
        ans.configure(text="Your angle is " +str(angle))
        ans.pack()
        calculateLinePosition()
        canvas.delete('all')
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT,fill="Green",outline='Brown')
        canvas.create_oval(X1rec, Y1rec, X2rec, Y2rec , width = 0, fill = 'blue')
        canvas.create_line(X1Line, Y1Line, X2Line, Y2Line, width= 2,fill = 'brown')
        canvas.pack()
    
entrySpace=Entry(root)#creating an entry space    
entrySpace.bind("<Return>",evaluateangle)
entrySpace.pack()
ans=Label(root)
ans.configure(text="Your initial angle is " +  str(angle))
ans.pack()


canvas=Canvas(root,width=WIDTH,height=HEIGHT)
canvas.pack()
canvas.create_rectangle(0,0,WIDTH,HEIGHT,fill="Green",outline="brown")
canvas.create_oval(X1rec, Y1rec, X2rec, Y2rec , width = 0, fill = 'blue')
#canvas.create_line(X1Line, Y1Line, X2Line, Y2Line, width= 2,fill = 'brown')
canvas.pack()
def refresh():
    if(button):
        global X1rec
        global X2rec
        global Y1rec
        global Y2rec
        global speed
        global angle
        global HEIGHT
        global WIDTH
        global Name
        global v 
        global h
        if X1rec - float(speed)*math.sin(angle*math.pi/180) >= 0 :
            if X1rec - float(speed)*math.sin(angle*math.pi/180) > WIDTH - 20:
                if angle%360 >= 90 :
                    angle = (360 - angle)%360
                else :
                    angle = (angle + 270)%360
            X1rec = X1rec - float(speed)*math.sin(angle*math.pi/180)
            X2rec = X1rec + 20
               
        else :
            if angle%360 >= 90 :
                angle = (360 - angle)%360
            else :
                angle = (angle + 270)%360
            X1rec = X1rec - float(speed)*math.sin(angle*math.pi/180)
            X2rec = X1rec + 20
        if Y1rec - float(speed)*math.cos(angle*math.pi/180) >= 0:
            if Y1rec - float(speed)*math.cos(angle*math.pi/180) > HEIGHT - 60:
                if angle%360 <= 180 :
                    angle = (360 + 180 - angle)%360
                else :
                    angle = (180 - angle)%360
            Y1rec = Y1rec - float(speed)*math.cos(angle*math.pi/180)
            Y2rec = Y1rec + 20
        else :
            if angle %360<= 90 :
                angle = (180 - angle)%360
            else :
                angle = (angle + 270)%360
            Y1rec = Y1rec - float(speed)*math.cos(angle*math.pi/180)
            Y2rec = Y1rec + 20
    
        ans.configure(text="Your angle is " +str(angle))
        ans.pack()
        calculateLinePosition()
        #canvas.delete('all')
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="Green",outline="brown")
        canvas.create_oval(X1rec, Y1rec, X2rec, Y2rec , width = 0, fill = 'blue')
        #canvas.create_line(X1Line, Y1Line, X2Line, Y2Line, width= 2,fill = 'brown')
        canvas.pack()
        
    #canvas.after(1000,refresh)
    canvas.after(100,refresh)
    evaluateimpact()
    ans.configure(text="The result name is" +  str( Name))
    ans.pack()
canvas.after(1,refresh)
root.mainloop()#to maintain the window open
print(angle)
if  len(Name)<2000:
    print(Name)
#if  len(Name)>20:
## statistics  
V=0 #number of the letter v in the name 
H=0 #number of the letter H in the name
for i in range(len(Name)):
    if Name[i]=='v':
       V=V+1
    else :
        H=H+1
data=[angle,V,H]
print(data)
#if len(Name)>10:
    #break