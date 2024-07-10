from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
raindrops= []
night= False 
rain_direction= 0
screen_color=1

def rains():
    global raindrops
    raindrops=[]
    x=-0.8
    for i in range(30): 
         y=0
         x+=0.05
         for j in range(6):
             y +=0.1
             y+=random.uniform(0.01,0.1)
             raindrops.append((x,y))
    

def move_raindrops():
    global raindrops
    for x,y in raindrops:
        glBegin(GL_LINES)
        glColor3f(0.0, 0.0, 1.0)
        z = random.uniform(0.04, 0.1)
        x1=x
        y1=y
        x2=x + 0.01 * rain_direction
        y2=y -z
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    global screen_color
    if night:
        glClearColor(screen_color,screen_color,screen_color,screen_color)  # Night
    else:
        glClearColor(screen_color,screen_color,screen_color,screen_color)  # Day
    glClear(GL_COLOR_BUFFER_BIT)

    move_raindrops()   
    
    
    #triangle
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(-0.6,0.06)
    glVertex2f(0.6,0.06)
    glVertex2f(0.0,0.3)
    glEnd()

    #SQUARE
    glBegin(GL_LINES)
    glColor4f(1.0,0.5,0.0,0.0)
    glVertex2f(-0.6,0.06)
    glVertex2f(0.6,0.06)
    glEnd()
    glBegin(GL_LINES)
    glColor4f(1.0,0.5, 0.0, 0.0)
    glVertex2f(0.6,0.06)
    glVertex2f(0.6,-0.5)
    glEnd()
    glBegin(GL_LINES)
    glColor4f(1.0,0.5,0.0, 0.0)
    glVertex2f(0.6,-0.5)
    glVertex2f(-0.6, -0.5)
    glEnd()
    glBegin(GL_LINES)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex2f(-0.6, -0.5)
    glVertex2f(-0.6, 0.06)
    glEnd()
    
    #DOOR
    glBegin(GL_LINES)
    glColor4f(1.0,0.5,0.0,0.0)
    glVertex2f(-0.4,-0.1)
    glVertex2f(-0.1,-0.1)
    glEnd()
    glBegin(GL_LINES)
    glColor4f(1.0, 0.5,0.0, 0.0)
    glVertex2f(-0.1,-0.1)
    glVertex2f(-0.1,-0.5)
    glEnd()
    glBegin(GL_LINES)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex2f(-0.1,-0.5)
    glVertex2f(-0.4,-0.5)
    glEnd()
    glBegin(GL_LINES)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex2f(-0.4,-0.5)
    glVertex2f(-0.4,-0.1)
    glEnd()

    glPointSize(6)
    glBegin(GL_POINTS)
    glColor3f(1,0,0)
    glVertex2f(-0.15,-0.3)
    glEnd()

    #WINDOW
    glBegin(GL_LINES)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex2f(0.4,-0.05)
    glVertex2f(0.15, -0.05)
    glEnd()

    glBegin(GL_LINES)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex2f(0.15,-0.05)
    glVertex2f(0.15,-0.25)
    glEnd()

    glBegin(GL_LINES)
    glColor4f(1.0, 0.5,0.0, 0.0)
    glVertex2f(0.15,-0.25)
    glVertex2f(0.4,-0.25)
    glEnd()

    glBegin(GL_LINES)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex2f(0.4,-0.25)
    glVertex2f(0.4,-0.05)
    glEnd()

    glBegin(GL_LINES)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex2f(0.275,-0.05)
    glVertex2f(0.275,-0.25)
    glEnd()

    glBegin(GL_LINES)
    glColor4f(1.0, 0.5, 0.0, 0.0)
    glVertex2f(0.15,-0.15)
    glVertex2f(0.4, -0.15)
    glEnd()


    glutSwapBuffers()
def key_pressed(key, x, y):
    global night,screen_color
    if key==b'n':
        night= True
        screen_color-=0.1
    elif key==b"d":
        night=False    
        screen_color+=0.1
    glutPostRedisplay()
def specialKeyListener(key, x, y):
    global rain_direction
    if key==GLUT_KEY_LEFT:
        rain_direction -=1
        
    elif key==GLUT_KEY_RIGHT:
        rain_direction +=1
        
    glutPostRedisplay()

def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,1,1,1000.0)
       
rains()
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500) 
glutInitWindowPosition(0,0)
wind =glutCreateWindow(b"OpenGL Coding") 
glutDisplayFunc(showScreen)
glutKeyboardFunc(key_pressed) 
glutSpecialFunc(specialKeyListener)
glutMainLoop()