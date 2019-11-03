from cmu_112_graphics import *
from tkinter import *
from PIL import Image 
import random

class Users(object):
    def __init__():
        self.x = x
        self.y = y
        

class Volunteers(Users):
    pass
    
    
class Organizations(Volunteers):
    pass
    
class Individuals(Volunteers):
    pass
    
class Recipients(Users):
    def __init__():
        super().__init__()
        pass

class StartMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_rectangle(0, 0, mode.width, mode.height,
                                fill = 'lightblue')
        
    
    ### selection: volunteers, Recipients

'''
    def mousePressed(mode, event):
        if:
            mode.app.setActiveMode(mode.app.VolunteersMode)
        elif:
            mode.app.setActiveMode(mode.app.RecipientsMode)
'''

class MyModalApp(ModalApp):
    def appStarted(app):
        app.StartMode = StartMode()
        app.VolunteersMode = VolunteersMode()
        app.RecipientsMode = RecipientsMode()

        app.setActiveMode(app.StartMode)
        app.timerDelay = 50
    

MyModalApp(width=500, height=500)
    
########

class Goods(object):
    pass
