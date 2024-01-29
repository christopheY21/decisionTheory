
from HelperClass import Expertise, InformationControl, Quantity
from SolutionType import ClientPreference, SolutionType

#https://developers.google.com/tag-platform/tag-manager/server-side/cloud-run-setup-guide?provisioning=manual
class GoogleServerSide(SolutionType):
    pricingServer = {
    55_000:98,#hits per month
    100_000:98,
    300_000:98,
    600_000:99,
    1_000_000:100,
    2_000_000:109,
    5_000_000:106,
    10_000_000:115,
    25_000_000:140,
    50_000_000:183,
    100_000_000:267
}
    def __init__(self,clientPreference: ClientPreference):
        self.clientPreference = clientPreference
        self.informationControl = InformationControl(Quantity.NONE,Quantity.NONE) #informationControl()
        self.adBlockerBypass = True #False
        self.componentsNumber = 5# int0
        self.serverCost = GoogleServerSide.pricingServer # dict
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



clienpref = ClientPreference(15,1,1,10,5,100,1000)

gg = GoogleServerSide(clienpref)

print(gg.getCriterias())