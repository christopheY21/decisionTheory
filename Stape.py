from HelperClass import Expertise, InformationControl, Quantity
from SolutionType import ClientPreference, SolutionType





class Stape(SolutionType):
    pricingServer = {
    10_000:0,
    500_000:20,
    2_000_000:50,
    5_000_000:100,
    10_000_000:150,
    20_000_000:200,
    50_000_000:300
}    
    def __init__(self,clientPreference: ClientPreference):
        self.clientPreference = clientPreference
        self.informationControl = InformationControl(Quantity.SOME,Quantity.SOME) #informationControl()
        self.adBlockerBypass = True #False
        self.componentsNumber = 5# int0
        self.serverCost = Stape.pricingServer # dict
        self.serverSideHelp = True #true or false
        self.consentBanner = True
        self.transferCost = 0

        #criteria
        self.criteria = {
            "solutionName":__class__.__name__,
            "dataQuality":None,#
            "installationGrade":None,#
            "maintenanceCost":None,#
            "userExperience":None,#
            "privacy":None#
        }



clienpref = ClientPreference(15,1,1,20,5,100,1000)

gg = Stape(clienpref)

print(gg.getCriterias())



