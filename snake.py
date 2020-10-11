import turtle
import time
import random


delay=0.1

#score
score=0
high_score=0


wn = turtle.Screen()
wn.title('snake game')
wn.bgcolor('green')
wn.setup(width=600,height=600)
wn.tracer(0)

#snake head
h=turtle.Turtle()
h.speed(0)
h.shape('square')
h.color('black')
h.penup()
h.goto(0,0)
h.direction ="stop"

#food
f=turtle.Turtle()
f.speed(0)
f.shape('circle')
f.color('red')
f.penup()
f.goto(0,100)

#body
body=[]
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=('courier',24, 'normal') )


#function 
def up():
    if h.direction!= "down":
        h.direction="up"
def down():
    if h.direction!= "up":
        h.direction="down"
def left():
    if h.direction!= "right":
        h.direction="left"
def right():
    if h.direction!= "left":
        h.direction="right"   
def move():    
    if h.direction =="up":
        y= h.ycor()
        h.sety(y+20)
    if h.direction =="down":
        y= h.ycor()
        h.sety(y-20)    
    if h.direction =="right":
        x= h.xcor()
        h.setx(x+20)
    if h.direction =="left":
        x= h.xcor()
        h.setx(x-20)     
#keyword
     
wn.listen()
wn.onkeypress(up,'w')     
wn.onkeypress(down,'s')   
wn.onkeypress(left,'a')   
wn.onkeypress(right,'d') 
# main game loop
while True:
    wn.update()
    # food collision
    if h.distance(f)<20:
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        f.goto(x,y)
        # add body
        new_seg=turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape('square')
        new_seg.color('gray')
        new_seg.penup()
        body.append(new_seg)
        # speed increasing 
        delay-=0.001
        
        #score
        score+=1
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score}",align="center", font=('courier',24, 'normal'))    



    #constaints of game     
    if h.xcor()<-290 or h.xcor()>290 or h.ycor()<-290 or h.ycor()>290:
        time.sleep(1)
        h.goto(0,0)
        h.direction="stop"
        # hiding segment
        for s in body:
            s.goto(1000,1000)
        # clearing body
        body.clear()
        #reset score and delay
        delay=0.1
        score=0
        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score}",align="center", font=('courier',24, 'normal')) 
        

    # move the end segment first in reverse order
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=h.xcor()
        y=h.ycor()
        body[0].goto(x,y)  

    move()
    # body colision
    for a in body:
        if a.distance(h)<20:
             time.sleep(1)
             h.goto(0,0)
             h.direction="stop"
             # hiding segment
             for s in body:
                s.goto(1000,1000)
             # clearing body
             body.clear()
             score=0
             delay=0.1
             
             pen.clear()
             pen.write(f"Score: {score} High Score: {high_score}",align="center", font=('courier',24, 'normal'))
    time.sleep(delay)
    
      
wn.mainloop()