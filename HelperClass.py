from enum import Enum



class Quantity(Enum):
    ALL = 1
    SOME = 2
    NONE = 3

class InformationControl():
    def __init__(self,modify:Quantity,remove:Quantity):
        self.modify = modify
        self.remove = remove
        
        self.informationControlDegree = 0
    def calculateInformationControl(self):
        converter = {
            Quantity.ALL:1,
            Quantity.SOME:0.5,
            Quantity.NONE:0
        }
        self.informationControlDegree = 0
        self.informationControlDegree+= converter[self.modify]
        self.informationControlDegree+= converter[self.remove]

        self.informationControlDegree/=2
        return self.informationControlDegree
    def getInformationcontrol(self):
        return self.informationControlDegree
class Expertise(Enum):
    HARD = 3
    MEDIUM = 2
    EASY = 1

class InfrastructureComplexity():
    def __init__(self,componentsHour:int,developerCostHour:int,transferCost:int):
        self.componentsNumber=componentsHour
        self.developerCostHour=developerCostHour
        self.transferCost = transferCost
        self.InfrastructureComplexity = 0

        self.calculateInfrastructureComplexity()

    def calculateInfrastructureComplexity(self):
        self.InfrastructureComplexity = self.componentsNumber*self.developerCostHour
        self.InfrastructureComplexity+= self.transferCost
        return self.InfrastructureComplexity
    def getInfrastructureComplexity(self):
        return self.InfrastructureComplexity


class ServerCost():
    def __init__(self,
                 pricingServer2:dict={},
                 thirdParty:int=None,
                 dataSources:int=None,
                 numberOfTags:int=None,
                 numberOfUsers:int=None,
                 numberOfEvents:int=None,
                 ):
        self.pricingServer = pricingServer2
        self.thirdParty = thirdParty
        self.dataSources = dataSources
        self.numberOfTags = numberOfTags
        self.numberOfUsers = numberOfUsers
        self.numberOfEvents = numberOfEvents
        if(self.numberOfEvents==None):
            if(self.thirdParty!=None and self.dataSources!=None and self.numberOfTags!=None and self.thirdParty!=None):
                self.numberOfEvents = numberOfTags*0.5*numberOfUsers*0.5*self.dataSources*self.thirdParty*0.5
            else:
                print("Error")
                self.numberOfEvents=0
        self.serverCost=0
    def calculateServerCost(self):
        minServerCostKey = min(key for key in self.pricingServer if key >= self.numberOfEvents)
        self.serverCost = self.pricingServer[minServerCostKey]
        return self.serverCost

    def getServerCost(self):
        return self.calculateServerCost()
class TagManager(Enum):
    GTAG = 1
    GOOGLE_TAG_MANAGER =2
    OTHERS = 3

class Proxy(Enum):
    DOTA_PROXY_SERVER  = 1
    STAPE_PROXY_SERVER = 2
    AUTOMATED_TAG = 3

class OnPrem(Enum):
    ON_PREM  = 1
    CLOUD = 2
    HYBRID = 3

class OnPremProperties():
    def __init__(self,onPremType :OnPrem):
        self.onPremType = onPremType
    def generateAttributes(self):
        if(self.onPremType == OnPrem.ON_PREM):
            pass
        elif(self.onPremType == OnPrem.CLOUD):
            pass
        elif(self.onPremType == OnPrem.HYBRID):
            pass
        