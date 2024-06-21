import pandas as pd
import random

#file location
file_loc = "D:\\Self\\NameSorter\\text.xlsx"

#Use Pandas Framework to get all Data from Excel to a tuple
studentList = pd.read_excel('D:/Project/NameSorter/test.xlsx')

#Filter out non Facilitators
facilitatorsList = studentList[studentList['Position'] == 'Facilitators']

#Sort Experienced Facilitators by Gender
experiencedFacilitatorsMale = facilitatorsList[(facilitatorsList['Experience'] == "Yes") & (facilitatorsList["Gender"] == "M")].reset_index(drop = True)
experiencedFacilitatorsFemale = facilitatorsList[(facilitatorsList['Experience'] == "Yes") & (facilitatorsList["Gender"] == "F")].reset_index(drop = True)

#Sort Inexperienced Facilitators by Gender
inexperiencedFacilitatorsMale = facilitatorsList[(facilitatorsList['Experience'] == "No") & (facilitatorsList["Gender"] == "M")].reset_index(drop = True)
inexperiencedFacilitatorsFemale = facilitatorsList[(facilitatorsList['Experience'] == "No") & (facilitatorsList["Gender"] == "F")].reset_index(drop = True)

#Randomise Facilitators to groups based on Experience and Gender
'''totalFacilitators = len(facilitatorsList)

#Assume max 15 Facilitators per group
totalGroup = int(totalFacilitators/15)
'''

#To randomize the Facilitators into different groups
def NumRandomizer(totalGroup, facilitatorDF, total):
    numSequence = random.shuffle(list(range(total)))

'''
    for i in range(total):
        groupList(facilitatorDF.iloc[numSequence], i)
'''

def groupList(facilitatorInfo, group):
    group1 = []
    group2 = []
    group3 = []
    group4 = []
    group5 = []
    group6 = []
    group7 = []
    group8 = []
    group9 = []
    group10 = []
    
    match group:
        case 1:
            group1.append(facilitatorInfo)
        case 2:
            group2.append(facilitatorInfo)
        case 3:
            group3.append(facilitatorInfo)
        case 4:
            group4.append(facilitatorInfo)
        case 5:
            group5.append(facilitatorInfo)
        case 6:
            group6.append(facilitatorInfo)
        case 7:
            group7.append(facilitatorInfo)
        case 8:
            group8.append(facilitatorInfo)
        case 9:
            group9.append(facilitatorInfo)
        case 10:
            group10.append(facilitatorInfo)

            