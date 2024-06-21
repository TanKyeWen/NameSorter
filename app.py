import pandas as pd
import numpy as np

#file location
file_loc = "D:\\Self\\NameSorter\\text.xlsx"

#Use Pandas Framework to get all Data from Excel to a tuple
studentList = pd.read_excel('D:/Project/NameSorter/test.xlsx')

#Filter out non Facilitators
facilitatorsList = studentList[studentList['Position'] == 'Facilitators']

#Sort Experienced Facilitators by Gender
experiencedFacilitatorsMale = facilitatorsList[(facilitatorsList['Experience'] == "Yes") & (facilitatorsList["Gender"] == "M")].reset_index(drop = True)
experiencedFacilitatorsFemale = facilitatorsList[(facilitatorsList['Experience'] == "Yes") & (facilitatorsList["Gender"] == "F")]

#Sort Inexperienced Facilitators by Gender
inexperiencedFacilitatorsMale = facilitatorsList[(facilitatorsList['Experience'] == "No") & (facilitatorsList["Gender"] == "M")]
inexperiencedFacilitatorsFemale = facilitatorsList[(facilitatorsList['Experience'] == "No") & (facilitatorsList["Gender"] == "F")]

#Randomise Facilitators to groups based on Experience and Gender
