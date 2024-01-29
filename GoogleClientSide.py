from HelperClass import Expertise, InformationControl, Quantity, ServerCost
from SolutionType import ClientPreference, SolutionType






class GoogleClientSide(SolutionType):
    pricingServer = {
    55_000:1,#hits per month
    100_000:1,
    300_000:1,
    600_000:1,
    1_000_000:1,
    2_000_000:1,
    5_000_000:1,
    10_000_000:1,
    25_000_000:1,
    50_000_000:1,
    100_000_000:1
}
    def __init__(self,clientPreference: ClientPreference):
        self.clientPreference = clientPreference
        self.informationControl = InformationControl(Quantity.NONE,Quantity.NONE) #informationControl()
        self.adBlockerBypass = False #False
        self.componentsNumber = 1# int0
        self.serverCost = GoogleClientSide.pricingServer # dict
        self.serverSideHelp = False #true or false
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



clienpref = ClientPreference(15,1,1,10,5,100,1000)

gg = GoogleClientSide(clienpref)

print(gg.getCriterias())