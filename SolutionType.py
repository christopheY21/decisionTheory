# abstract base class work 
from abc import ABC, abstractmethod
import numpy as np

from HelperClass import Expertise, InformationControl, InfrastructureComplexity, OnPrem, Proxy, ServerCost, TagManager 


class ClientPreference():
    def __init__(self,
                 expertise:int,
                 numberOfDataSources:int,
                 numberOfthirdParty:int=None,
                 numberOfTags:int=None,
                 numberOfTagsPII:int=None,
                 numberOfUsers:int=None,
                 numberOfEvents:int=None,
                 ):
        self.data = {
            #DATA QUALITY
            "inconsistent Data":"How much",
            "unnecessary Data":"How much",
            "expertise":expertise,
            #OPS
            "numberOfDataSources":numberOfDataSources,
            "numberOfThirdParty":numberOfthirdParty,
            "numberOfTags":numberOfTags,
            "numberOfTagsPII":numberOfTagsPII,
            "numberOfUsers":numberOfUsers,
            "numberofEvents":numberOfEvents,

        }

class SolutionType(ABC):
    def __init__(self,clientPreference: ClientPreference):
        self.clientPreference = clientPreference
        self.informationControl = None #informationControl()
        self.adBlockerBypass = None #False
        self.componentsNumber = None# int0
        self.serverCost = None # dict
        self.serverSideHelp = None #0 or 1 true or false
        self.consentBanner = None #true or false
        #NEW
        self.transferCost = 0 # int
        #criteria
        self.criteria = {
            "solutionName":__class__.__name__,
            "dataQuality":None,#
            "installationGrade":None,#
            "maintenanceCost":None,#
            "userExperience":None,#
            "privacy":None#
        }

    ####CALCULATE CRITERIA######
    def calculateDataQuality(self):
        self.criteria["dataQuality"]=self.informationControl.calculateInformationControl()*0.7+self.adBlockerBypass*0.3

    def calculateInstallationGrade(self):
        self.criteria["installationGrade"]=InfrastructureComplexity(self.componentsNumber,self.clientPreference.data["expertise"],self.transferCost).getInfrastructureComplexity()

    def calculateMaintenanceCost(self):
        self.criteria["maintenanceCost"]=ServerCost(self.serverCost,
                                                    self.clientPreference.data["numberOfThirdParty"],
                                                    self.clientPreference.data["numberOfDataSources"],
                                                    self.clientPreference.data["numberOfTags"],
                                                    self.clientPreference.data["numberOfUsers"],
                                                    self.clientPreference.data["numberofEvents"]
                                                    ).calculateServerCost()
    def calculateUserExperience(self):
        if(self.serverSideHelp):
            userExperience = self.clientPreference.data["numberOfTags"]*0.1
        else:
            userExperience = self.clientPreference.data["numberOfTags"]*0.1*self.clientPreference.data["numberOfThirdParty"]
        if(self.consentBanner):
            userExperience += 1
        self.criteria["userExperience"] = userExperience
    def calculatePrivacy(self):
        PIIrisks = self.clientPreference.data["numberOfTagsPII"]/self.clientPreference.data["numberOfTags"]
        informationControl = self.informationControl.calculateInformationControl()

        self.criteria["privacy"] = np.exp((1-informationControl)+PIIrisks)
    def getCriterias(self):
        self.calculateDataQuality()
        self.calculateInstallationGrade()
        self.calculateMaintenanceCost()
        self.calculatePrivacy()
        self.calculateUserExperience()
        return self.criteria
    ### END CALCULATION CRITERIA
    #dataQuality
    def getAdBlocker(self) -> bool:
        pass
    def getInformationcontrol(self) -> bool:
        pass
    #installationGrade
    def getInfrastructureComplexity(self) -> float:
        pass
    #maintenanceCost
    def getInfrastructureComplexity(self) -> int:
        pass
    def getDeveloperCost(self) -> int:
        pass
    def getNumberOfServer(self) -> int:
        pass
    def getBrowserExperience(self) -> float:
        pass
    def getPIIRisks(self) -> float:
        pass
