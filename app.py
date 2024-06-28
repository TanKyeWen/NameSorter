import pandas as pd
import random

# TO get user inputs
def main():
    print("aa")

# Append user to group 
def groupList(specificList, num, startRow, startCol):
    facilitator = pd.DataFrame()
    facilitator = pd.concat([facilitator, pd.DataFrame(specificList.loc[num]).T])

    specificList.drop(num, inplace = True)
    specificList.reset_index(drop = True, inplace = True)

    facilitator.to_excel('ModifiedTest.xlsx', index_label = False, startrow = startRow, startcol = startCol)

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

memberPerGroup = 1
numOfGrp = 2

for y in range(numOfGrp):
    for i in range(memberPerGroup):
        rng = random.randint(0, len(experiencedFacilitatorsFemale))
        groupList(experiencedFacilitatorsFemale, rng, 0, y)

    for i in range(memberPerGroup):
        rng = random.randint(0, len(experiencedFacilitatorsMale))
        groupList(experiencedFacilitatorsMale, rng, memberPerGroup, y)

    for i in range(memberPerGroup): 
        rng = random.randint(0, len(inexperiencedFacilitatorsFemale))
        groupList(inexperiencedFacilitatorsFemale, rng, memberPerGroup*2, y)

    for i in range(memberPerGroup):
        rng = random.randint(0, len(inexperiencedFacilitatorsMale))
        groupList(inexperiencedFacilitatorsMale, rng, memberPerGroup*3, y)
