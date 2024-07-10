from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
paused = False
circle_list = []
speed=0.1
def circle(radius,center):
    d=1-radius
    x=0
    y=radius 
    circlepoints(x,y,center)
    while(x<y):
        if(d<0):
            d=d+ 2*x + 3
            x+=1
        else:
            d= d+ 2*x - 2*y + 5 
            x+=1
            y-=1
        circlepoints(x,y,center)       
def circlepoints(x,y,center):
    glColor3f(1,0,0)
    glBegin(GL_POINTS)
    
    x0=x/250
    y0=y/250
    ax=center[0]/250
    ay=center[1]/250
    glVertex2f(x0+ax,y0+ay)
    glVertex2f(y0+ax,x0+ay)
    glVertex2f(y0+ax,-x0+ay)
    glVertex2f(x0+ax,-y0+ay)
    glVertex2f(-x0+ax,-y0+ay)
    glVertex2f(-y0+ax,-x0+ay)
    glVertex2f(-y0+ax,x0+ay)
    glVertex2f(-x0+ax,y0+ay)
    glEnd()
def showScreen():
    global circle_list
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glPointSize(2)
   
    for circle_data in circle_list:
        circle(circle_data[2],(circle_data[0],circle_data[1]))
        
    glutSwapBuffers()
    
def mouseFunc(button, state, x, y):
    global circle_list,paused
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if not paused:
            center_x=x -(500/2)
            center_y=(500/2)-y
            circle_list.append([center_x,center_y, 5])    
    glutPostRedisplay()                   
def update_circles(value):
    global circle_list,paused,speed
    if paused==False:
        glutTimerFunc(16, update_circles, 0)    
        
        for cd in circle_list:
            cd[2] += speed 
            a=cd[2]+cd[1]
            b=cd[2]+cd[0]
            c=cd[0]-cd[2] 
            d=cd[1]-cd[2]
            if a>250 or b>250 or c<-250 or d<-250:
                circle_list.remove(cd)
                if circle_list==[]:
                    glColor3f(0,0,0)
                    glBegin(GL_POINTS)
                    glVertex2f(0,0)
                    glEnd()
        
    glutPostRedisplay()
def specialKeyListener(key,x, y):
    global speed
    if key== GLUT_KEY_LEFT:
        speed *= 2
    if key== GLUT_KEY_RIGHT:
        speed = max(speed/ 2, 0.005)
    glutPostRedisplay()    
def keyboardListener(key, x,y):
    global paused
    if key== b' ':
        paused= not paused
    if paused==False:
        glutTimerFunc(16, update_circles, 0)        
    glutPostRedisplay()                     
def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,1,1,1000.0)
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500) 
glutInitWindowPosition(0,0)
wind =glutCreateWindow(b"LAB3") 
init()
glutDisplayFunc(showScreen)
glutMouseFunc(mouseFunc)
glutTimerFunc(16,update_circles, 0) 
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()