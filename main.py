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
        stringItems = ""
        for item in self.items:
            stringItems += item + ", "
        stringItems = stringItems[:-2]
        return f"{self.name}: Location: ({self.x}, {self.y}). Items: {stringItems}"

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

    def __repr__(self):
        stringItems = ""
        for item in self.items:
            stringItems += item + ", "
        stringItems = stringItems[:-2]
        return f"{self.name}: Location: ({self.x}, {self.y}). Items: {stringItems}. Time: {self.time}"

r1 = Recipients("Rick", -50, 100, ["bedding", "clothes", 'electronics'])
r2 = Recipients("Kelly", -25, 60, ["produce"])
r3 = Recipients("Dan", -2, 10, [])
r4 = Recipients("Naldo", 63, 15, ["nonperishables"])
r5 = Recipients("Ashley", 64, 38, ["produce", "nonperishables"])
r6 = Recipients("Annabel", -30, 19, [])
r7 = Recipients("Danny", 24, 56, ["nonperishables", "water"])
r8 = Recipients("Alice", 6, 8, ['stationaries', "nonperishables", 'electronics'])
r9 = Recipients("Gaby", 24, 73, ["clothes"])
r10 = Recipients("Izzy", 19, 10, ["clothes", 'electronics'])
r11 = Recipients("Michael", 35, 90, ["bedding", "hygiene"])
r12 = Recipients("Cal", 0, 0, ["stationaries", "hygiene"])
r13 = Recipients("Sabina", 99, 2, ["nonperishables", "bedding", 'stationaries'])
r14 = Recipients("Kevin", 2, 30, ["produce"])
r15 = Recipients("Luke", 0, 3, ['electronics'])
r16 = Recipients("Sam", -48, 0, ["toys", "books"])
r17 = Recipients("Alex", -43, 2, ["books", "medicines"])
r18 = Recipients("Jasmine", -90, -11, ["clothes", "bedding"])
r19 = Recipients("Lori", 45, 23, ["toys", "clothes"])
r20 = Recipients("Thomas", 10, 11, ["bedding"])
recipientList = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

o1 = Organizations("Papa John's", -50, 100, ["hygiene", "electronics", "bedding"], "14:30")
o2 = Organizations("Giant Eagle", -25, 60, ["stationaries", "medicines"], "12:00")
o3 = Organizations("Whole Foods", -2, 10, ["electronics", "nonperishables", "clothes"], "15:00")
o4 = Organizations("Key Food", 63, 15, ["produce", 'medicines'], "16:00")
o5 = Organizations("A Giving Heart", 64, 38, ["produce", 'books'], "9:00")
o6 = Organizations("Family Links", -30, 19, ["toys"], "10:00")
o7 = Organizations("Bethlehem Heaven", 24, 56, ["hygiene", "clothes", "nonperishables"], "17:00")
o8 = Organizations("Homeless Children's Education Fund", 80, -100, ["toys", "produce"], "18:30")
o9 = Organizations("Veterans Place", 24, 73, ["stationaries", "clothes", "medicines", "clothes"], "8:00")
o10 = Organizations("Salvation Army", 19, 10, ["electronics", "produce", "stationaries", 'books'], "11:30")

orgsList = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10]

def rgbString(red, green, blue):
    # Don't worry about how this code works yet.
    return "#%02x%02x%02x" % (red, green, blue)

class StartMode(Mode):
    def appStarted(mode):
        url = ('https://i.imgur.com/ixiXl1y.png')
        mode.recipient = mode.loadImage(url)
        #mode.recipient = mode.scaleImage(mode.recipient)
        url1 = 'https://i.imgur.com/2DJtPdC.png'
        mode.individual = mode.loadImage(url1)
        url2 = 'https://i.imgur.com/X39FwYu.png'
        mode.organization = mode.loadImage(url2)
        #print(mode.width)
        urlLogo = 'https://i.imgur.com/iDXbi93.png'
        mode.logo = mode.loadImage(urlLogo)
        mode.logo = mode.scaleImage(mode.logo, 2/5)
        print(mode.logo.size)
        mode.logoWidth, mode.logoHeight = mode.logo.size
        urlBanner = "https://i.imgur.com/RjrRtaQ.png"
        mode.banner = mode.loadImage(urlBanner)
        #mode.banner = mode.
        
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
        canvas.create_image(mode.width / 2, mode.height / 4, image = ImageTk.PhotoImage(mode.banner))
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
        self.volunteer = Volunteers('', 0, 0,[])
        self.possibleItems = ['bedding','books','toys', 'clothes', 'medicines', 'hygiene',
                              'stationaries', 'produce', 'nonperishables', 'electronics']
        url = 'https://i.imgur.com/mzWpb17.png'
        self.findRecipientButton = self.loadImage(url)
        self.foundRecipient = Recipients('John', 0,0,[])
        self.drawRecipient = False
        self.giveInstructions = False
        self.nameBool = False
        self.locationBool = False
        url1 = 'https://i.imgur.com/gYNj5KB.png'
        self.backButton = self.loadImage(url1)
        urlItems = 'https://i.imgur.com/ICizG3j.png'
        self.itemImage = self.loadImage(urlItems)
        self.itemImage = self.scaleImage(self.itemImage, .9)
        urlLogo = 'https://i.imgur.com/iDXbi93.png'
        self.logo = self.loadImage(urlLogo)
        self.logo = self.scaleImage(self.logo, 2/5)
        self.logoWidth, self.logoHeight = self.logo.size

        
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
        if event.x >= self.width / 2 - 76 and event.x <= self.width / 2 + 76 and event.y >= self.height / 2 - 85 and event.y <= self.height / 2 - 50:
            self.foundRecipient = self.findRecipient(self.volunteer, recipientList)
            self.drawRecipient = True
            print("are you willing to give")
        if event.x >= 15 and event.x <= 92 and event.y >= 15 and event.y <= 50:
            self.startScreenMode()
            self.appStarted()
            print('functioning')
        
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
        elif (event.key == ','):
            self.stringInput += ','
        elif (event.key == 'Space'):
            if not self.nameBool:
                self.stringInput += ' '
            elif not self.locationBool:
                self.locationBool = True
            elif self.locationBool:
                self.giveRecipient(self.foundRecipient)
#            else:
#                self.giveRecipient(self.foundRecipient)
        elif(event.key == 'Delete'):
            if len(self.stringInput) >= 1:
                self.stringInput = self.stringInput[:len(self.stringInput) - 1]
        elif (event.key == 'Enter'):
            if self.nameBool == False:
                self.volunteer.name = self.stringInput
                self.nameBool = True
                self.stringInput = ''
                print('name work')
            elif self.locationBool == False:
                if self.stringInput not in self.possibleItems:
                    print('not valid')
                    self.stringInput = ''
                else:
                    self.volunteer.items.append(self.stringInput)
                    print(self.stringInput)
                    self.stringInput = ''
                    print(self.volunteer.items)
            else:
                for index in range(0, len(self.stringInput)):
                    if self.stringInput[index] == ',':
                        commaIndex = index
                print(commaIndex)
                self.volunteer.x = int(self.stringInput[0:index-1])
                self.volunteer.y = int(self.stringInput[index:])
                self.stringInput = ''
                print('successfully entered location of volunteer')
            
            

    def timerFired(self):
        #self.spriteCounter = (1 + self.spriteCounter) % len(self.sprites)
        pass

    #this function redraws everything
    def redrawAll(self, canvas):
        customBlue = rgbString(46, 70, 139)
        canvas.create_rectangle(0, 0, self.width, self.height, fill = "lightsteelblue")
        canvas.create_image(self.width - self.logoWidth / 1.5, self.logoHeight / 1.5, image = ImageTk.PhotoImage(self.logo))
        font = 'futura 16'
        if self.nameBool == False:
            canvas.create_rectangle(self.width / 2 - 100, 13, self.width / 2 + 100, 75, fill = customBlue)
            canvas.create_text(self.width / 2, 100, text = "Please press enter to confirm name", font = font, fill = "white")
            canvas.create_text(self.width / 2, 25, text = 'Enter Name:', font = font, fill = "white")
        else:
            if self.locationBool == False:
                canvas.create_rectangle(self.width / 2 - 100, 13, self.width / 2 + 100, 75, fill = customBlue)
                canvas.create_text(self.width / 2, 100, text = 'Please press space when you finish entering inputs', font = font, fill = "white")
                canvas.create_text(self.width / 2, 25, text = 'Enter items:', font = font, fill = "white")
                canvas.create_image(self.width / 2, self.height * 3 / 4, image = ImageTk.PhotoImage(self.itemImage))
            else:
                canvas.create_rectangle(self.width / 2 - 100, 13, self.width / 2 + 100, 75, fill = customBlue)
                canvas.create_text(self.width / 2, 100, text = "Please press enter to confirm location", font = font, fill = "white")
                canvas.create_text(self.width / 2, 25, text = 'Enter location: "X,Y"', font = font, fill = "white")
        canvas.create_text(53, 100, text = 'Name:', font = font, fill = "white" )
        canvas.create_text(53,125,text = self.volunteer.name, font = font, fill = "white")
        #canvas.create_image(self.width / 2, self.height * 3 / 4, image = ImageTk.PhotoImage(self.itemImage))
        #canvas.create_text(self.width / 2, 75, text = 'Your input:')
        canvas.create_text(self.width / 2,53,text = self.stringInput, font = font, fill = "white")
        canvas.create_rectangle(self.width / 2 - 75, 40,self.width / 2 + 75,65, outline = "white")
        canvas.create_image(self.width / 2,self.height / 2 - 67.5,image = ImageTk.PhotoImage(self.findRecipientButton))
        #canvas.create_text(self.width / 2, 125, text = 'Press enter to add item', font = font, fill = "white")
        canvas.create_text(self.width / 2, 125, text = 'This is what you have:', font = font, fill = "white")
        commaString = ', '.join(self.volunteer.items)
        canvas.create_text(self.width / 2,150,text = commaString, font = font, fill = "white")
        canvas.create_text(self.width / 2, 175, text = 'Location:', font = font, fill = "white")
        canvas.create_text(self.width / 2,200,text = f'({self.volunteer.x},{self.volunteer.y})', font = font, fill = "white")
        if self.giveInstructions:
            canvas.create_text(self.width / 2, 300, text = 'Recipient match found!', font = font, fill = "white")
            canvas.create_text(self.width / 2, 320,
                               text = 'Please press the space key to confirm your donation.',
                               font = font, fill = "white")
        if self.drawRecipient:
            #for i in range(len(self.recipients)):
            canvas.create_text(self.width / 2, 350, text = "This is the potential recipient:", font = font, fill = "white")
            recipientInfo = (str(self.foundRecipient))
            canvas.create_text(self.width / 2, 370,
                                text = recipientInfo, font = font, fill = "white")
        canvas.create_image(53, 32.5, image = ImageTk.PhotoImage(self.backButton))

class RecipientMode(Mode):
    def appStarted(self):
        self.stringInput = ''
        self.possibleItems = ['bedding','books','toys', 'clothes', 'medicines', 'hygiene',
                              'stationaries', 'produce', 'nonperishables', 'electronics']
        self.locationBool = False
        self.recipient = Recipients('', 0,0,[])
        url1 = 'https://i.imgur.com/gYNj5KB.png'
        self.backButton = self.loadImage(url1)
        url = 'https://i.imgur.com/9atRWrO.png'
        self.submitButton = self.loadImage(url)
        self.time = '00:00'
        self.nameBool = False
        self.orgListBool = False
        self.backBool = False
        self.submittedBool = False
        urlItems = 'https://i.imgur.com/ICizG3j.png'
        self.itemImage = self.loadImage(urlItems)
        self.itemImage = self.scaleImage(self.itemImage, .9)
        urlLogo = 'https://i.imgur.com/iDXbi93.png'
        self.logo = self.loadImage(urlLogo)
        self.logo = self.scaleImage(self.logo, 2/5)
        self.logoWidth, self.logoHeight = self.logo.size
        self.bestOrgs = orgsList

        
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
            if self.nameBool != True:
                self.stringInput += ' '
            else:
                self.locationBool = True
        elif (event.key == ','):
            self.stringInput += ','
        elif(event.key == 'Delete'):
            if len(self.stringInput) >= 1:
                self.stringInput = self.stringInput[:len(self.stringInput) - 1]
        elif (event.key == 'Enter'):
            if self.nameBool == False:
                self.recipient.name = self.stringInput
                self.nameBool = True
                self.stringInput = ''
                print('name work')
            else:
                if self.locationBool == False:
                    if self.stringInput not in self.possibleItems:
                        print('not valid2')
                        self.stringInput = ''
                    else: 
                        self.recipient.items.append(self.stringInput)
                        self.stringInput = ''
                else: 
                    for index in range(0,len(self.stringInput)):
                        if self.stringInput[index] == ',':
                            commaIndex = index
                    print(commaIndex)
                    self.recipient.x = int(self.stringInput[0:index-1])
                    self.recipient.y = int(self.stringInput[index:])
                    self.stringInput = ''
                    print('successfully entered location')
                
    def mousePressed(mode, event):
        if event.x >= mode.width / 2 - 47 and event.x <= mode.width / 2 + 47 and event.y >= mode.height / 2 - 17.5 - 35 and event.y <= mode.height / 2 + 17.5 - 35:
            newRecipient = Recipients(mode.recipient.name, mode.recipient.x,mode.recipient.y, mode.recipient.items)
            recipientList.append(newRecipient)
            mode.orgListBool = True
            print(recipientList)
            mode.submittedBool = True
        if event.x >= 15 and event.x <= 92 and event.y >= 15 and event.y <= 50:
            mode.startScreenMode()
            mode.app.recipientMode
            mode.backBool = True
            if mode.backBool and mode.submittedBool:
                mode.appStarted()

    def redrawAll(mode, canvas):
        customBlue = rgbString(46, 70, 139)
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = "lightsteelblue")
        canvas.create_image(mode.width - mode.logoWidth / 1.5, mode.logoHeight / 1.5, image = ImageTk.PhotoImage(mode.logo))
        font = "futura 16"
        if mode.nameBool == False:
            canvas.create_rectangle(mode.width / 2 - 100, 13, mode.width / 2 + 100, 75, fill = customBlue)
            canvas.create_text(mode.width / 2, 100, text = "Please press enter to confirm name", font = font, fill = "white")
            canvas.create_text(mode.width / 2, 25, text = 'Enter Name:', font = font, fill = "white")
        else:
            if mode.locationBool == False:
                canvas.create_rectangle(mode.width / 2 - 100, 13, mode.width / 2 + 100, 75, fill = customBlue)
                canvas.create_text(mode.width / 2, 100, text = 'Please press space when you finish entering inputs', font = font, fill = "white")
                canvas.create_text(mode.width / 2, 25, text = 'Enter items:', font = font, fill = "white")
                canvas.create_image(mode.width / 2, mode.height * 3 / 4, image = ImageTk.PhotoImage(mode.itemImage))
            else:
                canvas.create_rectangle(mode.width / 2 - 100, 13, mode.width / 2 + 100, 75, fill = customBlue)
                canvas.create_text(mode.width / 2, 100, text = "Please press enter to confirm location", font = font, fill = "white")
                canvas.create_text(mode.width / 2, 25, text = 'Enter location: "X,Y"', font = font, fill = "white")
        canvas.create_text(53, 100, text = 'Name:', font = font, fill = "white" )
        canvas.create_text(53,125,text = mode.recipient.name, font = font, fill = "white")
        #canvas.create_text(mode.width / 2, 75, text = 'Your input:')
        canvas.create_text(mode.width / 2,53,text = mode.stringInput, font = font, fill = "white")
        canvas.create_rectangle(mode.width / 2 - 75, 40,mode.width / 2 + 75,65, outline = "white")
        canvas.create_image(53, 32.5, image = ImageTk.PhotoImage(mode.backButton))
        canvas.create_image(mode.width / 2,mode.height / 2 - 35, image = ImageTk.PhotoImage(mode.submitButton))
        canvas.create_text(mode.width / 2, 125, text = 'This is what you need:', font = font, fill = "white")
        commaString = ', '.join(mode.recipient.items)
        canvas.create_text(mode.width / 2,150,text = commaString, font = font, fill = "white")
        canvas.create_text(mode.width / 2, 175, text = 'Location:', font = font, fill = "white")
        canvas.create_text(mode.width / 2,200,text = f'({mode.recipient.x},{mode.recipient.y})', font = font, fill = "white")
        #goes back to game mode after any key is pressed while in the help mode
        if mode.orgListBool:
            for index in range(len(orgsList)):
                canvas.create_text(25, mode.height / 2 + 30 + 20 * index, text = str(orgsList[index]), anchor = "nw", font = "futura 12", fill = "white")
'''
    def findOrg(mode):
        potential = dict()
        for item in mode.recipient.items:
            for org in orgsList:
                if item in orgsList:
                    if org in potential:
                        potential[org] += 1
                    else:
                        potential[org] = 1
        bestOrgs = []
        for org in potential:
            bestOrgs += [org]
        return bestOrgs
'''
class OrganizationMode(Mode):
    def appStarted(self):
        self.stringInput = ''
        self.possibleItems = ['bedding','books','toys', 'clothes', 'medicines', 'hygiene',
                              'stationaries', 'produce', 'nonperishables', 'electronics']
        self.timeBool = False
        self.locationBool = False
        self.organization = Organizations('', 0,0,[],'00:00')
        url1 = 'https://i.imgur.com/gYNj5KB.png'
        self.backButton = self.loadImage(url1)
        url = 'https://i.imgur.com/9atRWrO.png'
        self.submitButton = self.loadImage(url)
        self.time = '00:00'
        self.name = ''
        self.nameBool = False
        urlItems = 'https://i.imgur.com/ICizG3j.png'
        self.itemImage = self.loadImage(urlItems)
        self.itemImage = self.scaleImage(self.itemImage, .9)
        urlLogo = 'https://i.imgur.com/iDXbi93.png'
        self.logo = self.loadImage(urlLogo)
        self.logo = self.scaleImage(self.logo, 2/5)
        self.logoWidth, self.logoHeight = self.logo.size

        
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
            if self.nameBool == True:
                self.timeBool = True
            else:
                self.stringInput += ' '
        elif (event.key == ','):
            self.stringInput += ','
        elif(event.key == 'Delete'):
            if len(self.stringInput) >= 1:
                self.stringInput = self.stringInput[:len(self.stringInput) - 1]
        elif (event.key == 'Enter'):
            if self.nameBool == False:
                self.organization.name = self.stringInput
                self.nameBool = True
                self.stringInput = ''
                print('name work')
            else:
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
                        self.organization.time = self.stringInput
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
            newOrganization = Organizations(mode.organization.name, mode.organization.x,mode.organization.y, mode.organization.items, mode.organization.time)
            orgsList.append(newOrganization)
            mode.startScreenMode()
            print(orgsList)
        if event.x >= 15 and event.x <= 92 and event.y >= 15 and event.y <= 50:
            mode.startScreenMode()
            mode.appStarted()
            print('functioning')
        
    def redrawAll(mode, canvas):
        customBlue = rgbString(46, 70, 139)
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = "lightsteelblue")
        canvas.create_image(mode.width - mode.logoWidth / 1.5, mode.logoHeight / 1.5, image = ImageTk.PhotoImage(mode.logo))
        font = "futura 16"
        if mode.nameBool == False:
            canvas.create_rectangle(mode.width / 2 - 100, 13, mode.width / 2 + 100, 75, fill = customBlue)
            canvas.create_text(mode.width / 2, 100, text = "Please press enter to confirm name", font = font, fill = "white")
            canvas.create_text(mode.width / 2, 25, text = 'Enter Name:', font = font, fill = "white")
        else:
            if mode.timeBool == False:
                canvas.create_rectangle(mode.width / 2 - 100, 13, mode.width / 2 + 100, 75, fill = customBlue)
                canvas.create_text(mode.width / 2, 100, text = 'Please press space when you finish entering inputs', font = font, fill = "white")
                canvas.create_text(mode.width / 2, 25, text = 'Enter items:', font = font, fill = "white")
                canvas.create_image(mode.width / 2, mode.height * 3 / 4, image = ImageTk.PhotoImage(mode.itemImage))
            else:
                if mode.locationBool == False:
                    canvas.create_rectangle(mode.width / 2 - 100, 13, mode.width / 2 + 100, 75, fill = customBlue)
                    canvas.create_text(mode.width / 2, 100, text = "Please press enter to confirm time", font = font, fill = "white")
                    canvas.create_text(mode.width / 2, 25, text = 'Enter time: "XX:XX"', font = font, fill = "white")
                else:
                    canvas.create_rectangle(mode.width / 2 - 100, 13, mode.width / 2 + 100, 75, fill = customBlue)
                    canvas.create_text(mode.width / 2, 100, text = "Please press enter to confirm location", font = font, fill = "white")
                    canvas.create_text(mode.width / 2, 25, text = 'Enter location: "X,Y"', font = font, fill = "white")
        canvas.create_text(53, 75, text = 'Name:', font = font, fill = "white")
        canvas.create_text(53,100,text = mode.organization.name, font = font, fill = "white")
        #canvas.create_text(mode.width / 2, 75, text = 'Your input:', font = font, fill = "white")
        canvas.create_text(mode.width / 2,53,text = mode.stringInput, font = font, fill = "white")
        canvas.create_rectangle(mode.width / 2 - 75, 40,mode.width / 2 + 75,65, outline = "white")
        canvas.create_image(53, 32.5, image = ImageTk.PhotoImage(mode.backButton))
        canvas.create_image(mode.width / 2,mode.height / 2, image = ImageTk.PhotoImage(mode.submitButton))
        canvas.create_text(mode.width / 2, 130, text = 'This is what you have:', font = font, fill = "white")
        commaString = ', '.join(mode.organization.items)
        canvas.create_text(mode.width / 2,150,text = commaString, font = font, fill = "white")
        canvas.create_text(mode.width / 2, 185, text = 'Time available for pickup:', font = font, fill = "white")
        canvas.create_text(mode.width / 2, 205, text = mode.organization.time, font = font, fill = "white")
        canvas.create_text(mode.width / 2, 240, text = 'Location:', font = font, fill = "white")
        canvas.create_text(mode.width / 2,260,text = f'({mode.organization.x},{mode.organization.y})', font = font, fill = "white")

class MyModalApp(ModalApp):
    def appStarted(app):
        app.startScreenMode = StartMode()
        app.individualMode = IndividualMode()
        app.recipientMode = RecipientMode()
        app.organizationMode = OrganizationMode()
        app.setActiveMode(app.startScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=650, height=650)
