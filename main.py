from tkinter import *


root=Tk()

root.title("Ball and Bar")
root.geometry("500x500")
canvas=Canvas(root,width=500,height=500,background="black")
canvas.place(x=0,y=0)
flag=False

class Ball:
    def __init__(self,root,x,y,r):
        self.tempx=-1
        self.tempy=-1
        self.dirx=-1/(self.tempx**2+self.tempy**2)
        self.diry=-1/(self.tempx**2+self.tempy**2)
        self.barLength=100
        self.magnitude=5
        self.x=x
        self.y=y
        self.r=r

        self.ballposx=0
        self.speed=20
        
        self.x1=self.x
        self.y1=self.y
        self.root=root
        self.ball=canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill="white")      
        self.bar=canvas.create_line(self.x,self.y,self.x+self.barLength/2,self.y,fill="white",width=5)
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
        print("moving ball")
        self.posx=self.dirx*self.magnitude+self.posx
        self.posy=self.diry*self.magnitude+self.posy
        if(self.posx<-225+2*self.r):
            self.dirx=1
            print("a")
        
        if(self.posy>50-2*self.r):
            self.diry=-1
            print("b")
            self.ballposx=self.posx-225
            flag=False
            self.isReady()
            return

        if(self.posx>250+2*self.r):

            self.dirx=-1   
            print("c")

        if(self.posy<-450+2*self.r):
            self.diry=1
            print("d")
        if (self.posx+225)> self.x  and  (self.posx+225)<self.x+self.barLength and  self.posy+self.r==0:
            self.tempx=self.dirx
            self.tempy=self.diry
            self.dirx=-1
            self.diry=-1
            print("e")

        print(self.posx+275+2*self.r,self.x,self.x+50,self.posy)
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
        self.ballMovement()

    
    def start(self,e):
        global flag
        if flag==False:
            flag=True




ball=Ball(root,225,450,5)



root.mainloop()