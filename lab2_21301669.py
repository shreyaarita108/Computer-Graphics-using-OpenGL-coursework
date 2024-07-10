from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

catcher_x= 0
diamond_x=random.uniform(-400, 400)
diamond_y=400
score=0
diamond_speed=5
catcher_speed= 10
game_over=False
game_paused=False
re=False
color = (random.uniform(0.4,1),random.uniform(0.4,1),random.uniform(0.4,1))
catcher_color=(1.0,1.0, 1.0)
def findzone(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>abs(dy):
        if(dx>=0 and dy>=0):
            zone=0
        elif(dx<=0 and dy>=0):
            zone=3
        elif(dx<=0 and dy<=0):
            zone=4
        elif(dx>=0 and dy<=0):
            zone=7
    else:
        if(dx>=0 and dy>=0):
            zone=1
        elif(dx<=0 and dy>=0):
            zone=2
        elif(dx<=0 and dy<=0):
            zone=5
        elif(dx>=0 and dy<=0):
            zone=6
    return zone        
def zone0(zone,x,y):
    if zone==0:
        x1=x
        y1=y
    elif zone==1: 
        x1=y 
        y1=x 
    elif zone==2:    
        x1=y 
        y1=-x    
    elif zone==3: 
        x1=-x
        y1=y
    elif zone==4: 
        x1=-x
        y1=-y
    elif zone==5: 
        x1=-y
        y1=-x
    elif zone==6:    
        x1=-y
        y1=x    
    elif zone==7:     
        x1=x
        y1=-y
    return (x1,y1)
def originalzone(zone,x,y):
    if zone==0:
        x1=x
        y1=y
    elif zone==1:
        x1=y
        y1=x
    elif zone==2:
        x1=-y
        y1=x
    elif zone==3:
        x1=-x
        y1=y
    elif zone==4:
        x1=-x
        y1=-y
    elif zone==5:
        x1=-y
        y1=-x
    elif zone==6:
        x1=y
        y1=-x
    elif zone==7:
        x1=x
        y1=-y
    return (x1,y1)            
def draw_line(x1,y1,x2,y2):
    zone=findzone(x1,y1,x2,y2)
    x1,y1=zone0(zone,x1,y1)
    x2,y2=zone0(zone,x2,y2)
    dx=x2 -x1
    dy=y2 -y1
    d= 2*dy -dx
    x=x1
    y=y1
    glBegin(GL_POINTS)
    while x <x2:
        xo,yo= originalzone(zone,x,y)
        glVertex2f(xo/500.0, yo/500.0) #
        x +=1
        if d<0:
            d+=2*dy
        else:
            d+=2*(dy- dx)
            y+=1
    glEnd()
def showScreen():
    global diamond_y,diamond_x,color
    glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_catcher()   
    draw_diamond(diamond_x,diamond_y ,color)
    diamond_y -=diamond_speed
    #ARROW
    glColor3f(0, 123, 122)
    draw_line(-450,450,-370,450)
    draw_line(-450,450,-410,470)
    draw_line(-450,450,-410,430)
    #PAUSE
    if game_paused:
        glColor3f(1,0.85,0)
        draw_line(-20,470,-20,420)
        draw_line(-20,470,30,445)
        draw_line(-20,420,30,445)
    else:    
        glColor3f(1,0.85,0)
        draw_line(10,470,10,430)
        draw_line(-10,470,-10,430)
    #cross
    glColor3f(1,0,0)
    draw_line(400,430,450,470)
    draw_line(450,430,400,470)
    glutSwapBuffers()
def draw_catcher():
    global catcher_color
    glColor3f(catcher_color[0],catcher_color[1],catcher_color[2])
    catcher_length = 100
    draw_line(catcher_x-catcher_length , -480,catcher_x+ catcher_length,-480)
    draw_line(catcher_x -catcher_length,-480, catcher_x -catcher_length-20,-460)
    draw_line(catcher_x+catcher_length,-480,catcher_x +catcher_length+20, -460)
    draw_line(catcher_x-catcher_length-20 ,-460,catcher_x+catcher_length+20,  -460)
def update_catcher_position(key,x, y):
    global catcher_x,diamond_y, diamond_speed, game_over, game_paused,catcher_speed
    if key == GLUT_KEY_LEFT and catcher_x > -370 and not game_over and not game_paused:
        catcher_x -= catcher_speed
    elif key == GLUT_KEY_RIGHT and catcher_x < 370 and not game_over and not game_paused:
        catcher_x += catcher_speed
    diamond_y += diamond_speed    
    glutPostRedisplay()
def handle_click(button, state,x, y):
    global score, diamond_speed, game_over, game_paused,re
    if button ==GLUT_LEFT_BUTTON and state ==GLUT_DOWN:
        if 21<= x<=60 and 20<=y<=40:
            game_paused=False
            if not game_over:
                print(f"Game Over! Score: {score}")
            restart_game()
            print("Starting Over!")

        elif 215<=x<=230 and 16<= y<= 45:
            game_paused= not game_paused
            if not game_paused:
                glutPostRedisplay()
        elif 405 <=x<=430 and 20<= y<= 40:
            print("Goodbye! Score:",score)
            glutLeaveMainLoop()
def restart_game():
    global re, score, diamond_speed, game_over, game_paused, catcher_x, diamond_x, diamond_y, catcher_color
    score =0
    game_over=False
    game_paused=False
    diamond_speed=5
    catcher_x=0
    diamond_x=random.uniform(-400, 400)
    diamond_y=400
    catcher_color=(1.0, 1.0, 1.0)
    glutPostRedisplay()    
def draw_diamond(x, y,color1):
    global color
    glColor3f(color[0],color[1],color[2])  
    diamond_size = 20
    draw_line(x-diamond_size,y,x,y+diamond_size)
    draw_line(x,y+ diamond_size,x+diamond_size, y)
    draw_line(x+diamond_size,y,x,y- diamond_size)
    draw_line(x,y -diamond_size,x-diamond_size, y)
def hasCollided(box1, box2):
    return (
        box1.x < box2.x + box2.width
        and box1.x + box1.width > box2.x
        and box1.y < box2.y + box2.height
        and box1.y + box1.height > box2.y)
class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
catcher=Box(catcher_x-100-20,-480,240, 20)  #250,30
diamond=Box(diamond_x-20, diamond_y-20,40, 40) 
def update_game_state(value):
    global re,score,diamond_speed,game_over,catcher_x,diamond_y,diamond_x,color,catcher_color,catcher_speed
    glutTimerFunc(100, update_game_state, 0) 
    if not game_paused:
        diamond_y -=diamond_speed  
        glutPostRedisplay()
        catcher=Box(catcher_x-100-20,-480,240, 20)  
        diamond=Box(diamond_x- 20, diamond_y-20, 40, 40) 
        if hasCollided(catcher,diamond):
            score+= 1
            print(f"Score: {score}")
            diamond_y=400
            diamond_x=random.uniform(-400,400)
            diamond_speed+=1
            catcher_speed+=1
            color = (random.uniform(0.4,1),random.uniform(0.4,1),random.uniform(0.4,1))
            draw_diamond(diamond_x,diamond_y,color)
        elif  diamond.y+diamond.height<-460 and not game_over:
            game_over=True 
            catcher_color=(1,0,0)
            print(f"Game Over! Score: {score}") 
            
    elif not game_paused and game_over:           
        print(f"Game Over! Score: {score}")         
def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,1,1,1000.0)
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(450,600) 
glutInitWindowPosition(800,0)
wind =glutCreateWindow(b"Catch the Diamonds!") 
init()
glutDisplayFunc(showScreen)
glutSpecialFunc(update_catcher_position)
glutTimerFunc(100,update_game_state,0) 
glutMouseFunc(handle_click)
glutMainLoop()