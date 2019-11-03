'''from cmu_112_graphics import *
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
'''
def mousePressed(mode, event):
        if:
            mode.app.setActiveMode(mode.app.VolunteersMode)
        elif:
            mode.app.setActiveMode(mode.app.RecipientsMode)
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
'''
from cmu_112_graphics import *
from tkinter import *
import random

class Users(object):
    def __init__(self, name, xcor, ycor, items):
        self.name = name
        self.x = xcor
        self.y = ycor
        self.items = items

    def getDistance(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5

    def __repr__(self):
        return f"Name: {self.name}, xcor: {self.x}, ycor: {self.y}, items: {self.items}"

class Recipients(Users):
    def __init__(self, name, xcor, ycor, items):
        super().__init__(name, xcor, ycor, items)

class Volunteers(Users):
    def __init__(self, name, xcor, ycor, items):
        super().__init__(name, xcor, ycor, items)
        
class Individuals(Volunteers):
     def __init__(self, name, xcor, ycor, items):
        super().__init__(name, xcor, ycor, items)

class Organizations(Volunteers):
    def __init__(self, name, xcor, ycor, items, time):
        super().__init__(name, xcor, ycor, items)
        self.time = time

r1 = Recipients("r1", -50, 100, ["food", "water"])
r2 = Recipients("r2", -25, 60, ["water"])
r3 = Recipients("r3", -2, 10, [])
r4 = Recipients("r4", 63, 15, ["food"])
r5 = Recipients("r5", 64, 38, ["food", "water"])
r6 = Recipients("r6", -30, 19, [])
r7 = Recipients("r7", 24, 56, ["food", "water"])
r8 = Recipients("r8", 80, -100, ["water", "food"])
r9 = Recipients("r9", 24, 73, ["water"])
r10 = Recipients("r10", 19, 10, ["water"])
r11 = Recipients("r11", 35, 90, ["food", "water"])
r12 = Recipients("r12", 0, 0, ["water", "food"])
r13 = Recipients("r13", 99, 2, ["water", "food"])
r14 = Recipients("r14", 2, 30, ["food"])
r15 = Recipients("r15", 44, -87, ["food"])
r16 = Recipients("r16", -48, 0, ["food"])
r17 = Recipients("r17", -43, 2, ["water"])
r18 = Recipients("r18", -90, -11, ["water"])
r19 = Recipients("r19", 45, 23, ["water"])
r20 = Recipients("r20", 10, 11, ["blankets"])
r21 = Recipients("r21", 11, 11, ["food", "water"])
recipientList = [r21, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]




class StartMode(Mode):
    def appStarted(mode):
        url = ('https://i.imgur.com/DeQra6t.png')
        mode.recipient = mode.loadImage(url)
        #mode.recipient = mode.scaleImage(mode.recipient)
        url1 = 'https://i.imgur.com/xgPSthb.png'
        mode.individual = mode.loadImage(url1)
        url2 = 'https://i.imgur.com/Tg3crtx.png'
        mode.organization = mode.loadImage(url2)
        #print(mode.width)
        
    def recipientMode(mode):
        print("activated")
        mode.app.setActiveMode(mode.app.recipientMode)
        
    def individualMode(mode):
        print("other activated")
        mode.app.setActiveMode(mode.app.individualMode)
        
    def organizationMode(mode):
        print('organization mode activated')
        mode.app.setActiveMode(mode.app.organizationMode)
        
    def redrawAll(mode, canvas):
        canvas.create_image(mode.width / 2,mode.height / 2, image=ImageTk.PhotoImage(mode.recipient))
        canvas.create_image(mode.width / 2,mode.height / 2 + 50, image = ImageTk.PhotoImage(mode.individual))
        canvas.create_image(mode.width / 2, mode.height / 2 - 50, image = ImageTk.PhotoImage(mode.organization))
        
        
    def mousePressed(mode, event):
        if event.x >= mode.width / 2 - 57 and event.x <= mode.width / 2 + 57 and event.y >= mode.height / 2 - 17.5 and event.y <= mode.height / 2 + 17.5:
            mode.recipientMode()
        elif event.x >= mode.width / 2 - 57.5 and event.x <= mode.width / 2 + 57.5 and event.y >= mode.height / 2 + 50 - 17.5 and event.y <= mode.height / 2 + 50 + 17.5:
            mode.individualMode()
        elif event.x >= mode.width / 2 - 70 and event.x <= mode.width / 2 + 70 and event.y >= mode.height / 2 - 50 - 17.5 and event.y <= mode.height / 2 - 50 + 17.5:
            mode.organizationMode()

class IndividualMode(Mode):
    def appStarted(self):
        self.stringInput = ''
        self.volunteer = Volunteers('John', 10, 11,[])
        self.possibleItems = ['food','water','blankets']
        url = 'https://i.imgur.com/99OnK6m.png'
        self.findRecipientButton = self.loadImage(url)
        self.foundRecipient = Recipients('John', 0,0,[])
        url1 = 'https://i.imgur.com/1N4h7mW.png'
        self.backButton = self.loadImage(url1)
        
    def startScreenMode(mode):
        print("activated")
        mode.app.setActiveMode(mode.app.startScreenMode)
        
    def findRecipient(self, volunteer, recipientLst):
        potential = dict()
        for item in volunteer.items:
            for recipient in recipientLst:
                if item in recipient.items:
                    if recipient in potential:
                        potential[recipient] += 1
                    else:
                        potential[recipient] = 1
        bestRecipient = None
        bestCount = 0
        bestDistance = 10**9
        for recipient in potential:
            if potential[recipient] > bestCount:
                bestRecipient = recipient
                bestCount = potential[recipient]
                bestDistance = recipient.getDistance(volunteer)
            elif potential[recipient] == bestCount and recipient.getDistance(volunteer) < bestDistance:
                bestRecipient = recipient
                bestCount = potential[recipient]
                bestDistance = recipient.getDistance(volunteer)
        return bestRecipient

    def giveRecipient(self, recipient):
        index = 0
        while index < len(self.volunteer.items):
            if self.volunteer.items[index] in recipient.items:
                recipient.items.remove(self.volunteer.items[index])
                self.volunteer.items.pop(index)
                self.volunteer.x = recipient.x
                self.volunteer.y = recipient.y
            else:
                index += 1
                
    def mousePressed(self, event):
        if event.x >= self.width / 2 - 76 and event.x <= self.width / 2 + 76 and event.y >= self.height / 2 - 17.5 and event.y <= self.height / 2 + 17.5:
            while len(self.volunteer.items) > 0:
                self.foundRecipient = self.findRecipient(self.volunteer, recipientList)
                self.giveRecipient(self.foundRecipient)
                #self.volunteer.items = []
                print(self.foundRecipient)
                #print('hi')
        if event.x >= 15 and event.x <= 92 and event.y >= 15 and event.y <= 50:
            self.startScreenMode()
            print('functioning')
        
    def keyPressed(self, event):
        if (event.key == "a"):  
            self.stringInput += 'a'
        elif (event.key == "b"):
            self.stringInput += 'b'
        elif (event.key == "c"):
            self.stringInput += 'c'
        elif (event.key == 'd'):
            self.stringInput += 'd'
        elif (event.key == 'e'):
            self.stringInput += 'e'
        elif (event.key == 'f'):
            self.stringInput += 'f'
        elif (event.key == 'g'):
            self.stringInput += 'g'
        elif (event.key == 'h'):
            self.stringInput += 'h'
        elif (event.key == 'i'):
            self.stringInput += 'i'
        elif (event.key == 'j'):
            self.stringInput += 'j'
        elif (event.key == 'k'):
            self.stringInput += 'k'
        elif (event.key == 'l'):
            self.stringInput += 'l'
        elif (event.key == 'm'):
            self.stringInput += 'm'
        elif (event.key == 'n'):
            self.stringInput += 'n'
        elif (event.key == 'o'):
            self.stringInput += 'o'
        elif (event.key == 'p'):
            self.stringInput += 'p'
        elif (event.key == 'q'):
            self.stringInput += 'q'
        elif (event.key == 'r'):
            self.stringInput += 'r'
        elif (event.key == 's'):
            self.stringInput += 's'
        elif (event.key == 't'):
            self.stringInput += 't'
        elif (event.key == 'u'):
            self.stringInput += 'u'
        elif (event.key == 'v'):
            self.stringInput += 'v'
        elif (event.key == 'w'):
            self.stringInput += 'w'
        elif (event.key == 'x'):
            self.stringInput += 'x'
        elif (event.key == 'y'):
            self.stringInput += 'y'
        elif (event.key == 'z'):
            self.stringInput += 'z'
        elif (event.key == 'Enter'):
            if self.stringInput not in self.possibleItems:
                print('not valid')
                self.stringInput = ''
            else:
                self.volunteer.items.append(self.stringInput)
                print(self.stringInput)
                self.stringInput = ''
                print(self.volunteer.items)
            

    def timerFired(self):
        #self.spriteCounter = (1 + self.spriteCounter) % len(self.sprites)
        pass

    #this function redraws everything
    def redrawAll(self, canvas):
        canvas.create_text(self.width / 2, 75, text = 'Your input:')
        canvas.create_text(self.width / 2,100,text = self.stringInput)
        canvas.create_rectangle(self.width / 2 - 50,85,self.width / 2 + 50,115)
        canvas.create_image(self.width / 2,self.height / 2,image = ImageTk.PhotoImage(self.findRecipientButton))
        canvas.create_text(self.width / 2, 125, text = 'This is what you have:')
        commaString = ', '.join(self.volunteer.items)
        canvas.create_text(self.width / 2,150,text = commaString)
        canvas.create_image(53, 32.5, image = ImageTk.PhotoImage(self.backButton))

class RecipientMode(Mode):
    def appStarted(self):
        self.stringInput = ''
        self.possibleItems = ['food','water','blankets']
        url = 'https://i.imgur.com/9cRy6y4.png'
        self.submitButton = self.loadImage(url)
        url1 = 'https://i.imgur.com/1N4h7mW.png'
        self.backButton = self.loadImage(url1)
        
    def startScreenMode(mode):
        print("activated")
        mode.app.setActiveMode(mode.app.startScreenMode)
                
    
    def redrawAll(mode, canvas):
        font = 'Arial 15 bold'
        canvas.create_image(53, 32.5, image = ImageTk.PhotoImage(mode.backButton))
        canvas.create_image(mode.width / 2,mode.height / 2, image = ImageTk.PhotoImage(mode.submitButton))
        

    #goes back to game mode after any key is pressed while in the help mode
    def mousePressed(mode, event):
        if event.x >= mode.width / 2 - 47 and event.x <= mode.width / 2 + 47 and event.y >= mode.height / 2 - 17.5 and event.y <= mode.height / 2 + 17.5:
            #do something with to add to your recipient list 
            print('yes')
            newRecipient = Recipients("John", 15,15, ['food'])
            recipientList.append(newRecipient)
            print(recipientList)
        if event.x >= 15 and event.x <= 92 and event.y >= 15 and event.y <= 50:
            mode.startScreenMode()
            print('functioning')

class OrganizationMode(Mode):
    def appStarted(self):
        self.stringInput = ''
        self.possibleItems = ['food','water','blankets']
        self.timeBool = False
        self.locationBool = False
        self.organization = Organizations('initial', 0,0,[],'00:00')
        url1 = 'https://i.imgur.com/1N4h7mW.png'
        self.backButton = self.loadImage(url1)
        url = 'https://i.imgur.com/9cRy6y4.png'
        self.submitButton = self.loadImage(url)
        self.time = '00:00'
        
    def startScreenMode(mode):
        print("activated")
        mode.app.setActiveMode(mode.app.startScreenMode)
        
    def keyPressed(self, event):
        commaIndex = 0
        if (event.key == "a"):  
            self.stringInput += 'a'
        elif (event.key == "b"):
            self.stringInput += 'b'
        elif (event.key == "c"):
            self.stringInput += 'c'
        elif (event.key == 'd'):
            self.stringInput += 'd'
        elif (event.key == 'e'):
            self.stringInput += 'e'
        elif (event.key == 'f'):
            self.stringInput += 'f'
        elif (event.key == 'g'):
            self.stringInput += 'g'
        elif (event.key == 'h'):
            self.stringInput += 'h'
        elif (event.key == 'i'):
            self.stringInput += 'i'
        elif (event.key == 'j'):
            self.stringInput += 'j'
        elif (event.key == 'k'):
            self.stringInput += 'k'
        elif (event.key == 'l'):
            self.stringInput += 'l'
        elif (event.key == 'm'):
            self.stringInput += 'm'
        elif (event.key == 'n'):
            self.stringInput += 'n'
        elif (event.key == 'o'):
            self.stringInput += 'o'
        elif (event.key == 'p'):
            self.stringInput += 'p'
        elif (event.key == 'q'):
            self.stringInput += 'q'
        elif (event.key == 'r'):
            self.stringInput += 'r'
        elif (event.key == 's'):
            self.stringInput += 's'
        elif (event.key == 't'):
            self.stringInput += 't'
        elif (event.key == 'u'):
            self.stringInput += 'u'
        elif (event.key == 'v'):
            self.stringInput += 'v'
        elif (event.key == 'w'):
            self.stringInput += 'w'
        elif (event.key == 'x'):
            self.stringInput += 'x'
        elif (event.key == 'y'):
            self.stringInput += 'y'
        elif (event.key == 'z'):
            self.stringInput += 'z'
        elif (event.key == '1'):
            self.stringInput += '1'
        elif (event.key == '2'):
            self.stringInput += '2'
        elif (event.key == '3'):
            self.stringInput += '3'
        elif (event.key == '4'):
            self.stringInput += '4'
        elif (event.key == '5'):
            self.stringInput += '5'
        elif (event.key == '6'):
            self.stringInput += '6'
        elif (event.key == '7'):
            self.stringInput += '7'
        elif (event.key == '8'):
            self.stringInput += '8'
        elif (event.key == '9'):
            self.stringInput += '9'
        elif (event.key == '0'):
            self.stringInput += '0'
        elif (event.key == ':'):
            self.stringInput += ':'
        elif (event.key == 'Space'):
            self.timeBool = True
        elif (event.key == ','):
            self.stringInput += ','
        elif (event.key == 'Enter'):
            if self.timeBool == False:
                if self.stringInput not in self.possibleItems:
                    print('not valid2')
                    self.stringInput = ''
                else: 
                    self.organization.items.append(self.stringInput)
                    self.stringInput = ''
            elif self.timeBool == True and not self.locationBool:
                print(self.stringInput)
                print(self.stringInput[2])
                if self.stringInput[2] == ':' and self.stringInput[:1].isdigit():
                    self.time = self.stringInput
                    print('successfully entered time')
                    self.stringInput = ''
                    self.locationBool = True
                else:
                    print('not valid1')
                    print(self.stringInput)
                    self.stringInput = ''
                    print(self.stringInput)
            else: 
                for index in range(0,len(self.stringInput)):
                    if self.stringInput[index] == ',':
                        commaIndex = index
                print(commaIndex)
                self.organization.x = int(self.stringInput[0:index-1])
                self.organization.y = int(self.stringInput[index:])
                self.stringInput = ''
                print('successfully entered location')
                
            
        
    def redrawAll(mode, canvas):
        if mode.timeBool == False:
            canvas.create_text(mode.width / 2, 25, text = 'Enter items')
        else:
            if mode.locationBool == False:
                canvas.create_text(mode.width / 2, 25, text = 'Enter time: "XX:XX"')
            else:
                canvas.create_text(mode.width / 2, 25, text = 'Enter location: "X,X"')
        canvas.create_text(mode.width / 2, 75, text = 'Your input:')
        canvas.create_text(mode.width / 2,100,text = mode.stringInput)
        canvas.create_rectangle(mode.width / 2 - 50,85,mode.width / 2 + 50,115)
        canvas.create_image(53, 32.5, image = ImageTk.PhotoImage(mode.backButton))
        canvas.create_image(mode.width / 2,mode.height / 2, image = ImageTk.PhotoImage(mode.submitButton))
        canvas.create_text(mode.width / 2, 125, text = 'This is what you have:')
        commaString = ', '.join(mode.organization.items)
        canvas.create_text(mode.width / 2,150,text = commaString)
        canvas.create_text(mode.width / 2, 175, text = 'Time available for pickup:')
        canvas.create_text(mode.width / 2,200,text = mode.time)
        canvas.create_text(mode.width / 2, 300, text = 'Location:')
        canvas.create_text(mode.width / 2,325,text = f'({mode.organization.x},{mode.organization.y})')

class MyModalApp(ModalApp):
    def appStarted(app):
        app.startScreenMode = StartMode()
        app.individualMode = IndividualMode()
        app.recipientMode = RecipientMode()
        app.organizationMode = OrganizationMode()
        app.setActiveMode(app.startScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=500, height=500)
