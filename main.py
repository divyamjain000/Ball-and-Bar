from tkinter import *


root=Tk()

root.title("Ball and Bar")
root.geometry("500x500")
canvas=Canvas(root,width=500,height=500,background="black")
canvas.place(x=0,y=0)
flag=False

class Ball:
    def __init__(self,root,x,y,r):
        self.dirx=0
        self.diry=-1
        self.magnitude=5
        self.x=x
        self.y=y
        self.r=r
        self.root=root
        self.ball=canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill="white")      
        self.bar=canvas.create_line(self.x,self.y,self.x+50,self.y,fill="white",width=5)
        self.root.bind("<Button-1>",self.start)
        while True:
            self.root.update()
            if flag==True:
                self.startgame()
                break



    def Bar(self,x,y):
        canvas.coords(self.bar,self.x,self.y,self.x+50,self.y)

    def getCoords(self,e):
        global flag
        self.x=e.x
        if(self.x<0):
            self.x=0

        if(self.x>450):
            self.x=450
        self.y=450
        self.Bar(self.x,self.y)
        print(self.x,self.y,flag)
    
    def moveBall(self):
        global flag
       

        self.posx=self.dirx*self.magnitude
        self.posy=self.diry*self.magnitude
        if self.posx<0 or self.posx>500:
            self.dirx=-self.dirx
        if self.posy<0 or self.posy>500:
            self.diry=-self.diry

        if flag==True:
            canvas.move(self.ball,self.posx,self.posy)
            self.root.after(25,self.moveBall)
        else:
            canvas.coords(self.ball,self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r)
    
    def startgame(self):
        self.root.bind("<Motion>",self.getCoords)
        self.moveBall()
    
    def start(self,e):
        global flag
        if flag==False:
            flag=True




ball=Ball(root,225,450,5)



root.mainloop()