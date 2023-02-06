from tkinter import *
from public.fileReading import *


root=Tk()

root.title("Ball and Bar")
root.geometry("700x700")
canvas=Canvas(root,width=500,height=500,background="black")
canvas.place(x=100,y=100)
flag=False
a=300
s="Time: "+str(a)
pauseTimer=False
class Ball:
    def __init__(self,root,x,y,r):
        self.tempx=-1
        self.tempy=-1
        self.dirx=1/(self.tempx**2+self.tempy**2)
        self.diry=1/(self.tempx**2+self.tempy**2)
        self.barLength=100
        self.magnitude=1
        self.x=x
        self.y=y
        self.r=r
        self.label=Label(root,text=s)
        self.label.place(x=100,y=50)

        self.pausetimer=pauseTimer

        self.ballposx=0
        self.speed=4
        
        self.x1=self.x
        self.y1=self.y
        self.root=root
        self.quitButton()
        self.ball=canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill="white")      
        self.bar=canvas.create_line(self.x,self.y,self.x+self.barLength/2,self.y,fill="white",width=5)
        self.lines=returnList()
        self.createBlocks()
        while flag==False:
            self.root.update()
            self.isReady()


    def isReady(self):
        self.root.bind("<Motion>",self.getCoords)
        canvas.coords(self.ball,self.x-self.r+self.barLength/2,self.y-2*self.r,self.x+self.r+self.barLength/2,self.y)
        self.root.bind("<Button-1>",self.start)
        while True:
            self.root.update()
            if flag==True:
                self.startgame()
                break


    def Bar(self,x,y):
        canvas.coords(self.bar,self.x,self.y,self.x+self.barLength,self.y)

    def getCoords(self,e):
        global flag
        self.x=e.x
        if(self.x<0):
            self.x=0

        if(self.x>500-self.barLength):
            self.x=500-self.barLength
        self.y=450
        self.Bar(self.x,self.y)
        if flag==False:
            canvas.coords(self.ball,self.x-self.r+self.barLength/2,self.y-2*self.r,self.x+self.r+self.barLength/2,self.y)
            self.ballposx=self.x-225
    
    def ballMovement(self):
        global flag
        self.posx=self.dirx*self.magnitude+self.posx
        self.posy=self.diry*self.magnitude+self.posy
        if(self.posx<-225+2*self.r):
            self.dirx=1
        
        if(self.posy>50-2*self.r):
            self.diry=-1
            self.ballposx=self.posx-225
            flag=False
            self.pausetimer=True
            self.isReady()
            return

        if(self.posx>250+2*self.r):
            self.dirx=-1   

        if(self.posy<-450+2*self.r):
            self.diry=1

        if (self.posx+225)> self.x  and  (self.posx+225)<self.x+self.barLength and  self.posy+self.r==0:
            self.tempx=self.dirx
            self.tempy=self.diry
            self.diry=-1

        if flag==True:
            canvas.coords(self.ball,self.x1-self.r+self.posx,self.y1-self.r+self.posy,self.x1+self.r+self.posx,self.y1+self.r+self.posy)
            self.root.after(self.speed,self.ballMovement)
        else:
            canvas.coords(self.ball,self.x-self.r+self.barLength/2,self.y-2*self.r,self.x+self.r+self.barLength/2,self.y)
    
    def startgame(self):
        global flag
        flag=True
        self.posx=self.ballposx
        self.posy=0
        self.dirx=-1
        self.diry=-1
        self.timer()
        self.ballMovement()

    
    def start(self,e):
        global flag
        if flag==False:
            flag=True
            self.pausetimer=False

    def createBlocks(self):
        print(len(self.lines[0]))
        for j in range (len(self.lines)):
            for i in range(len(self.lines[j])):
                if(self.lines[j][i]=="1"):
                    canvas.create_rectangle(20*i+10,20*j+10,20*i+27,20*j+27,fill="green")
                elif self.lines[j][i]=="2":
                    canvas.create_rectangle(20*i+10,20*j+10,20*i+27,20*j+27,fill="grey")
    def quitButton(self):
        self.button=Button(root,height=1,width=3,text="Quit",command=quit)
        self.button.place(x=550,y=50)

    def timer(self):
        global a
        global s
        if self.pausetimer==False:
            a=a-1
            s="Time: "+str(a)
            self.label.config(text=s)
            canvas.after(1000,self.timer)
    
    





ball=Ball(root,225,450,5)



root.mainloop()