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
        
r1 = Recipients("r1", -50, 100, ["bedding", "clothes", 'electronics'])
r2 = Recipients("r2", -25, 60, ["produce"])
r3 = Recipients("r3", -2, 10, [])
r4 = Recipients("r4", 63, 15, ["nonperishables"])
r5 = Recipients("r5", 64, 38, ["produce", "nonperishables"])
r6 = Recipients("r6", -30, 19, [])
r7 = Recipients("r7", 24, 56, ["nonperishables", "water"])
r8 = Recipients("r8", 80, -100, ['stationaries', "nonperishables", 'electronics'])
r9 = Recipients("r9", 24, 73, ["clothes"])
r10 = Recipients("r10", 19, 10, ["clothes", 'electronics'])
r11 = Recipients("r11", 35, 90, ["bedding", "hygiene"])
r12 = Recipients("r12", 0, 0, ["stationaries", "hygiene"])
r13 = Recipients("r13", 99, 2, ["nonperishables", "bedding", 'stationaries'])
r14 = Recipients("r14", 2, 30, ["produce"])
r15 = Recipients("r15", 44, -87, ["medicines", 'electronics'])
r16 = Recipients("r16", -48, 0, ["toys", "books"])
r17 = Recipients("r17", -43, 2, ["books", "medicines"])
r18 = Recipients("r18", -90, -11, ["clothes", "bedding"])
r19 = Recipients("r19", 45, 23, ["toys", "clothes"])
r20 = Recipients("r20", 10, 11, ["bedding"])
r21 = Recipients("r21", 11, 11, ["bedding", "toys"])
recipientList = [r21, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

o1 = Organizations("o1", -50, 100, ["hygiene", "electronics", "bedding"], "14:30")
o2 = Organizations("o2", -25, 60, ["stationaries", "medicines"], "12:00")
o3 = Organizations("o3", -2, 10, ["electronics", "nonperishables", "clothes"], "15:00")
o4 = Organizations("o4", 63, 15, ["produce", 'medicines'], "16:00")
o5 = Organizations("o5", 64, 38, ["produce", 'books'], "9:00")
o6 = Organizations("o6", -30, 19, ["toys"], "10:00")
o7 = Organizations("o7", 24, 56, ["hygiene", "clothes", "nonperishables"], "17:00")
o8 = Organizations("o8", 80, -100, ["toys", "produce"], "18:30")
o9 = Organizations("o9", 24, 73, ["stationaries", "clothes", "medicines", "clothes"], "8:00")
o10 = Organizations("o10", 19, 10, ["electronics", "produce", "stationaries", 'books'], "11:30")

orgsList = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10]


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
        urlLogo = 'https://i.imgur.com/qocOFHA.png'
        mode.logo = mode.loadImage(urlLogo)
        mode.logo = mode.scaleImage(mode.logo, 1/3)
        print(mode.logo.size)
        #mode.logo = mode.logo.crop((3, 3, 43, 44))
        mode.logoWidth, mode.logoHeight = mode.logo.size
        
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
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = "lightsteelblue")
        canvas.create_image(mode.width - mode.logoWidth / 1.5, mode.logoHeight / 1.5, image = ImageTk.PhotoImage(mode.logo))
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
        self.possibleItems = ['bedding','books','toys', 'clothes', 'medicines', 'hygiene',
                              'stationaries', 'produce', 'nonperishables', 'electronics']
        url = 'https://i.imgur.com/99OnK6m.png'
        self.findRecipientButton = self.loadImage(url)
        self.foundRecipient = Recipients('John', 0,0,[])
        self.drawRecipient = False
        self.giveInstructions = False
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
        if bestRecipient != None:
            self.giveInstructions = True
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
            self.foundRecipient = self.findRecipient(self.volunteer, recipientList)
            self.drawRecipient = True
            print("are you willing to give")
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
        elif (event.key == 'Space'):
            self.giveRecipient(self.foundRecipient)
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
        font = 'futura 15'
        canvas.create_text(self.width / 2, 75, text = 'Your input:')
        canvas.create_text(self.width / 2,100,text = self.stringInput)
        canvas.create_rectangle(self.width / 2 - 50,85,self.width / 2 + 50,115)
        canvas.create_image(self.width / 2,self.height / 2,image = ImageTk.PhotoImage(self.findRecipientButton))
        canvas.create_text(self.width / 2, 125, text = 'Press enter to add item')
        canvas.create_text(self.width / 2, 145, text = 'This is what you have:')
        commaString = ', '.join(self.volunteer.items)
        canvas.create_text(self.width / 2,165,text = commaString)
        if self.giveInstructions:
            canvas.create_text(self.width / 2, 300, text = 'Recipient match found!', font = font)
            canvas.create_text(self.width / 2, 320,
                               text = 'Please press the space key to confirm your donation.',
                               font = font)
        if self.drawRecipient:
            #for i in range(len(self.recipients)):
            canvas.create_text(self.width / 2, 350, text = "This is the potential recipient:", font = font)
            recipientInfo = (str(self.foundRecipient))
            canvas.create_text(self.width / 2, 370,
                                text = recipientInfo, font = font)
        canvas.create_image(53, 32.5, image = ImageTk.PhotoImage(self.backButton))
        # list of possible items
        possibleItems = 'Here are the items you could donate: '
        possibleItems1 = 'bedding, books, toys, clothes, medicines, hygiene,'
        possibleItems2 = 'stationaries, produce, nonperishables, electronics'
        canvas.create_text(self.width / 2, 400, text = possibleItems, font = font)
        canvas.create_text(self.width / 2, 420, text = possibleItems1, font = font)
        canvas.create_text(self.width / 2, 440, text = possibleItems2, font = font)

class RecipientMode(Mode):
    def appStarted(self):
        self.stringInput = ''
        self.possibleItems = ['bedding','books','toys', 'clothes', 'medicines', 'hygiene',
                              'stationaries', 'produce', 'nonperishables', 'electronics']
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
        # list of possible items
        possibleItems = 'Please add the items that you need from the items list: '
        possibleItems1 = 'bedding, books, toys, clothes, medicines, hygiene,'
        possibleItems2 = 'stationaries, produce, nonperishables, electronics'
        canvas.create_text(mode.width / 2, 400, text = possibleItems, font = font)
        canvas.create_text(mode.width / 2, 420, text = possibleItems1, font = font)
        canvas.create_text(mode.width / 2, 440, text = possibleItems2, font = font)

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
        self.possibleItems = ['bedding','books','toys', 'clothes', 'medicines', 'hygiene',
                              'stationaries', 'produce', 'nonperishables', 'electronics']
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
                
    def mousePressed(mode, event):
        if event.x >= mode.width / 2 - 47 and event.x <= mode.width / 2 + 47 and event.y >= mode.height / 2 - 17.5 and event.y <= mode.height / 2 + 17.5:
            #do something with to add to your recipient list 
            print('yes')
            newOrganization = Organizations("John", 15,15, ['food'], "00:00")
            orgsList.append(newOrganization)
            print(orgsList)
        if event.x >= 15 and event.x <= 92 and event.y >= 15 and event.y <= 50:
            mode.startScreenMode()
            print('functioning')        
        
    def redrawAll(mode, canvas):
        font = "futura 15"
        if mode.timeBool == False:
            canvas.create_rectangle(mode.width / 2 - 45, 15, mode.width / 2 + 45, 40, fill = "yellow")
            canvas.create_text(mode.width / 2, 25, text = 'Enter items',  font = font)
        else:
            if mode.locationBool == False:
                canvas.create_rectangle(mode.width / 2 - 60, 15, mode.width / 2 + 60, 40, fill = "yellow")
                canvas.create_text(mode.width / 2, 25, text = 'Enter time: "XX:XX"',  font = font)
            else:
                canvas.create_rectangle(mode.width / 2 - 45, 15, mode.width / 2 + 45, 40, fill = "yellow")
                canvas.create_text(mode.width / 2, 25, text = 'Enter location: "X,X"',  font = font)
        canvas.create_text(mode.width / 2, 75, text = 'Your input:',  font = font)
        canvas.create_text(mode.width / 2,100,text = mode.stringInput,  font = font)
        canvas.create_rectangle(mode.width / 2 - 50,85,mode.width / 2 + 50,115)
        canvas.create_image(53, 32.5, image = ImageTk.PhotoImage(mode.backButton))
        canvas.create_image(mode.width / 2,mode.height / 2, image = ImageTk.PhotoImage(mode.submitButton))
        # JUST ADDED
        canvas.create_text(mode.width / 2, 125, text = 'Please press space when you finish entering inputs', font = font)
        # JUST ADDED
        canvas.create_text(mode.width / 2, 145, text = 'This is what you have:', font = font)
        commaString = ', '.join(mode.organization.items)
        canvas.create_text(mode.width / 2, 165,text = commaString,  font = font)
        canvas.create_text(mode.width / 2, 185, text = 'Time available for pickup:',  font = font)
        canvas.create_text(mode.width / 2, 205,text = mode.time,  font = font)
        canvas.create_text(mode.width / 2, 300, text = 'Location:',  font = font)
        canvas.create_text(mode.width / 2,325,text = f'({mode.organization.x},{mode.organization.y})',  font = font)
        # list of possible items
        possibleItems = 'Here are the items you could donate: '
        possibleItems1 = 'bedding, books, toys, clothes, medicines, hygiene,'
        possibleItems2 = 'stationaries, produce, nonperishables, electronics'
        canvas.create_text(mode.width / 2, 400, text = possibleItems, font = font)
        canvas.create_text(mode.width / 2, 420, text = possibleItems1, font = font)
        canvas.create_text(mode.width / 2, 440, text = possibleItems2, font = font)

class MyModalApp(ModalApp):
    def appStarted(app):
        app.startScreenMode = StartMode()
        app.individualMode = IndividualMode()
        app.recipientMode = RecipientMode()
        app.organizationMode = OrganizationMode()
        app.setActiveMode(app.startScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=500, height=500)
