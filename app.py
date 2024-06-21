import pandas as pd
import numpy as np

file_loc = "D:\\Self\\NameSorter\\text.xlsx"

studentList = pd.read_excel('D:/Self/NameSorter/test.xlsx')

facilitatorsList = studentList[studentList['Position'] == 'Facilitators']


#Sort Experienced Facilitators by Gender
experiencedFacilitatorsMale = facilitatorsList[(facilitatorsList['Experience'] == "Yes") & (facilitatorsList["Gender"] == "M")]
experiencedFacilitatorsFemale = facilitatorsList[(facilitatorsList['Experience'] == "Yes") & (facilitatorsList["Gender"] == "F")]

#Sort Inexperienced Facilitators by Gender
inexperiencedFacilitatorsMale = facilitatorsList[(facilitatorsList['Experience'] == "No") & (facilitatorsList["Gender"] == "M")]
inexperiencedFacilitatorsFemale = facilitatorsList[(facilitatorsList['Experience'] == "No") & (facilitatorsList["Gender"] == "F")]

print(facilitatorsList)
print(experiencedFacilitatorsMale)
