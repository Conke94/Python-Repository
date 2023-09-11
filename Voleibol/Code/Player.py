class Player:
#CONSTRUCTORS & DESTRUCTORS#
    def __init__(self, name, position, age, gender):
        self.name = name
        self.position = position
        self.age = age
        self.gender = gender

        self.totalSets = 0
        self.rightSets = 0

#SETTERS & GETTERS#
    def getPlayerName (self):
        return self.name   
    def getPlayerPosition(self):
        return self.position  
    def getPlayerAge(self):
        return self.age   
    def getPlayerGender(self):
        return self.gender
    def getTotalSets (self):
        return self.totalSets
    def getRightSets(self):
        return self.rightSets


#METHOD#
    def addSets (self, right, total):
        self.totalSets+=total
        self.rightSets+=right
        
        