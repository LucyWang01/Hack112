from cmu_112_graphics import *
from tkinter import *
from PIL import Image 
import random

class Users(object):
    def __init__(self, name, xcor, ycor, items):
        self.name = name
        self.x = xcor
        self.y = ycor
        self.items = items

class Volunteers(Users):
    def __init__(self, name, xcor, ycor):
        super().__init__(name, xcor, ycor)
    
class Organizations(Volunteers):
    def __init__(self, name, xcor, ycor):
        super().__init__(name, xcor, ycor)

class Individuals(Volunteers):
    def __init__(self, name, xcor, ycor):
        super.__init__(name, xcor, ycor)

    
class Recipients(Users):
    def __init__(self, name, xcor, ycor):
        super().__init__(name, xcor, ycor)

class StartMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_rectangle(0, 0, mode.width, mode.height,
                                fill = 'lightblue')

class IndividualsMode(Mode):
    def appStarted(mode):
        mode.individual = Individuals()

class OrganizationsMode(Mode):
    def appStarted(mode):
        mode.organization = Organizations()
        
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
