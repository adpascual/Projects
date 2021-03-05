from Apartment import *

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i += 1
            else:
                apartmentList[k] = righthalf[j]
                j +=  1
            k += 1
        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j += 1
            k += 1

def ensureSortedAscending(apartmentList):
    check = 0
    i = 1
    for i in range(len(apartmentList)-1): 
        if(apartmentList[i] > apartmentList[i + 1]): 
            check = 1
        i += 1   
        if (check == 0): 
            return True 
        else: 
            return False

def getNthApartment(apartmentList, n):
    if n > len(apartmentList)-1:
        return '(Apartment) DNE'
    return apartmentList[n].getApartmentDetails()

def getTopThreeApartments(apartmentList):
    mergesort(apartmentList)
    aStr = ""
    i = 0

    if len(apartmentList) == 1:
       return "1st: {}" \
               .format(apartmentList[0].getApartmentDetails())

    if len(apartmentList) == 2:
        return "1st: {}\n2nd: {}" \
               .format(apartmentList[0].getApartmentDetails(),
                       apartmentList[1].getApartmentDetails())
    if len(apartmentList) > 3:
        return "1st: {}\n2nd: {}\n3rd: {}" \
               .format(apartmentList[0].getApartmentDetails(),
                       apartmentList[1].getApartmentDetails(),
                       apartmentList[2].getApartmentDetails())
