
from HelperClass import Expertise, InformationControl, Quantity
from SolutionType import ClientPreference, SolutionType





class Matomo(SolutionType):
    pricingServer = {
    55_000:19,#hits per month
    100_000:35,
    300_000:69,
    600_000:109,
    1_000_000:159,
    2_000_000:309,
    5_000_000:790,
    10_000_000:1490,
    25_000_000:3690,
    50_000_000:7290,
    100_000_000:13900
}
    def __init__(self,clientPreference: ClientPreference):
        self.clientPreference = clientPreference
        self.informationControl = InformationControl(Quantity.SOME,Quantity.SOME) #informationControl()
        self.adBlockerBypass = True #False,
        self.componentsNumber = 5# int0
        self.serverCost = Matomo.pricingServer # dict
        self.serverSideHelp = True #true or false
        self.consentBanner = False
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

gg = Matomo(clienpref)

print(gg.getCriterias())
