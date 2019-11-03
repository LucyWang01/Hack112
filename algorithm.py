RecipientList = []

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
    def __init__(self, name, xcor, ycor, items):
        super().__init__(name, xcor, ycor, items)

class Goods(object):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def giveGoods(self, quantity):
        self.quantity -= quantity

    def __eq__(self, other):
        return isinstance(other, Goods) and self.name == other.name

G1 = Goods("food", 3)
G2 = Goods("water", 1)
G3 = Goods("clothes", 5)

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
r20 = Recipients("r20", 10, 11, ["clothes"])
r21 = Recipients("r21", 11, 11, ["food", "water"])

RecipientList = [r21, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

def findRecipient(volunteer, recipientLst):
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

def giveRecipient(volunteer, recipient):
    index = 0
    while index < len(volunteer.items):
        if volunteer.items[index] in recipient.items:
            recipient.items.remove(volunteer.items[index])
            volunteer.items.pop(index)
            volunteer.x = recipient.x
            volunteer.y = recipient.y
        else:
            index += 1
    #return (len(volunteer.items) > 0) # return True if still has left to give

def test(volunteer, recipientLst):
    while len(volunteer.items) > 0:
        print("volunteer before: ", volunteer)
        recipient = findRecipient(volunteer, recipientLst)
        print("recipient: ", recipient)
        giveRecipient(volunteer, recipient)
        print("volunteer: ", volunteer)

v1 = Individuals("rick", 11, 11, ["water", "food", "clothes"])
#print(findRecipient(v1, RecipientList))
test(v1, RecipientList)

#########################################################
# Recipient methods
#########################################################
o1 = Organizations("o1", -50, 100, ["food", "water", "clothes"])
o2 = Organizations("o2", -25, 60, ["water", "clothes"])
o3 = Organizations("o3", -2, 10, [])
o4 = Organizations("o4", 63, 15, ["food"])
o5 = Organizations("o5", 64, 38, ["food", "water"])
o6 = Organizations("o6", -30, 19, ["clothes"])
o7 = Organizations("o7", 24, 56, ["food", "water"])
o8 = Organizations("o8", 80, -100, ["water", "food"])
o9 = Organizations("o9", 24, 73, ["water", "clothes"])
o10 = Organizations("o10", 19, 10, ["water", "food"])

orgs = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10]

def findOrg(recipient, orgs):
    potential = dict()
    for item in recipient.items:
        for org in orgs:
            if item in org.items:
                if org in potential:
                    potential[org] += 1
                else:
                    potential[org] = 1
    bestOrg = None
    bestCount = 0
    bestDistance = 10**9
    for org in potential:
        if potential[org] > bestCount:
            bestOrg = org
            bestCount = potential[org]
            bestDistance = org.getDistance(recipient)
        elif potential[org] == bestCount and org.getDistance(recipient) < bestDistance:
            bestOrg = org
            bestCount = potential[org]
            bestDistance = org.getDistance(recipient)
    return bestOrg

R1 = Recipients("R1", 19, 10, ["water", "food"])

print(findOrg(R1, orgs))









