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
    def appStarted(mode):
        mode.indiOG = mode.loadImage('Individual.png')
        mode.indi = mode.scaleImage(mode.indiOG, 1/2)
 
        mode.orgOG = mode.loadImage('Organizations.jpg')
        
        mode.org = mode.scaleImage(mode.orgOG, 2/3)
 
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_rectangle(0, 0, mode.width, mode.height,
                                fill = 'lightblue')
        canvas.create_image(200, 300, image=ImageTk.PhotoImage(mode.indi))
        canvas.create_image(500, 300, image=ImageTk.PhotoImage(mode.org))


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
        app.IndividualsMode = IndividualsMode()
        app.OrganizationsMode = OrganizationsMode()
        #app.RecipientsMode = RecipientsMode()

        app.setActiveMode(app.StartMode)
        app.timerDelay = 50
    

MyModalApp(width=500, height=500)
    
########

class Goods(object):
    pass
