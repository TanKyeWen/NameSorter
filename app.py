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
def NameRandomizer(totalGroups, facilitatorDF, total):
    numSequence = list(range(total))
    random.shuffle(numSequence)

    