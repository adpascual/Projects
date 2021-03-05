from lab06 import *

class Apartment:

    def __init__(self, rent=0, metersFromUCSB=0, condition="N/A"):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent
    
    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format (self.rent, self.metersFromUCSB, self.condition)

    def __lt__(self, other):
        if self.rent != other.rent:
            if self.rent < other.rent:
                return True
            else:
                return False
        else:
            if self.metersFromUCSB != other.metersFromUCSB:
                if self.metersFromUCSB < other.metersFromUCSB:
                    return True
                else:
                    return False
            else:
                if self.condition != other.condition:
                    if len(self.condition) < len(other.condition):
                        return False
                    else:
                        return True
                else:
                    return True
        return False

    def __gt__(self, other):
        if self.rent != other.rent:
            if self.rent > other.rent:
                return True
            else:
                return False
        else:
            if self.metersFromUCSB != other.metersFromUCSB:
                if self.metersFromUCSB > other.metersFromUCSB:
                    return True
                else:
                    return False
            else:
                if self.condition != other.condition:
                    if len(self.condition) > len(other.condition):
                        return False
                    else:
                        return True
                else:
                    return True
        return False
    
    def __eq__(self, other):
        quality = {
        "bad": 0,
        "average": 1,
        "excellent": 2}
        if self.rent == other.rent and \
           self.metersFromUCSB == other.metersFromUCSB and \
           self.condition == other.condition:
            return True
        return False
