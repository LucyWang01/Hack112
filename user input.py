from cmu_112_graphics import *
from tkinter import *

class MyApp(App):
    def appStarted(self):
        self.message = 'Click the mouse to enter your name!'

    def mousePressed(self, event):
        name = self.getUserInput('What is your name?')
        if (name == None):
            self.message = 'You canceled!'
        else:
            self.showMessage('You entered: ' + name)
            self.message = f'Hi, {name}!'

    def redrawAll(self, canvas):
        font = 'Arial 24 bold'
        canvas.create_text(self.width/2,  self.height/2,
                           text=self.message, font=font)

MyApp(width=500, height=300)
