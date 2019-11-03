class Users(object):
    def __init__():
        self.x = x
        self.y = y
        

class Volunteers(Users):
    
    
class Organizations(Volunteers):
    
class Individuals(Volunteers):
    
class Recipients(Users):
    def __init__():
        super().__init__()
        self

class StartMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_rectangle(0, 0, mode.width, mode.height,
                                fill = 'lightblue')
        canvas.create_text(mode.width/2, 150, text='Are you a', font=font)
    
    ### selection: volunteers, Recipients

    def mousePressed(mode, event):
        if:
            mode.app.setActiveMode(mode.app.VolunteersMode)
        elif:
            mode.app.setActiveMode(mode.app.RecipientsMode)


class MyModalApp(ModalApp):
    def appStarted(app):
        app.StartMode = StartMode()
        app.VolunteersMode = VolunteersMode()
        app.RecipientsMode = RecipientsMode()

        app.setActiveMode(app.StartMode)
        app.timerDelay = 50
    
    
########

class Goods(object):
