import pandas as pd
import numpy as np
from openpyxl import load_workbook
import os

print("_" * 50)
print("Welcome To Name Sorter!")
print("_" * 50)
print("* Note: THE EXCEL FILE MUST BE IN THE SAME FOLDER AS THIS PYTHON FILE!!")

fileName = input("Enter your Excel Name: \n")
outputFileName = input("Enter the output file name: \n")
roleColomnName = input("Enter the Roles Column Name: \n")
experienceColumnName = input("Enter the Experience Column name: \n")
faciIdentifier = input("Enter the Facilitator's role name : \n")

#To know if foundation and degree are seperated or not
seperationInput = input("Do you want to seperate Foundation and Degree? (Y/N)\n").capitalize()

seperation = 2 if seperationInput in ['Y', 'YES'] else 1
if seperation == 2:
    studiesColumnName = input("Enter the Degree and Foundation Column name: \n")
    degreeIdentifier = input("Enter the Degree's role name: \n")
    numOfGrpDegree = int(input("Enter the Numbers of Groups for Degree: \n"))
    foundationIdentifier = input("Enter the Foundation's role name: \n")
    numOfGrpFoundation = int(input("Enter the Numbers of Groups for Foundation: \n"))
else:
    numOfGrpDegree = int(input("Enter the Numbers of Groups for Degree: \n"))

#file location
fileLoc = os.getcwd() + "/" + (fileName if fileName.endswith(".xlsx") else fileName + ".xlsx")

#Use Pandas Framework to get all Data from Excel to a tuple
studentList = pd.read_excel(fileLoc)

destinationFilePath = os.getcwd() + '/' + outputFileName + '.xlsx'
studentList.to_excel(destinationFilePath, sheet_name='AllData', index=False)

def create_balancedGrps(df, numOfGrps):
    # Stratify by Gender and Experience
    strata = df.groupby(['Gender', experienceColumnName])
    
    # Initialize empty groups
    groups = {i: pd.DataFrame(columns=df.columns) for i in range(numOfGrps)}
    
    # Shuffle and distribute each stratum
    for _, group in strata:
        group = group.sample(frac=1).reset_index(drop=True)  # Shuffle
        for i in range(len(group)):
            groups[i % numOfGrps] = pd.concat([groups[i % numOfGrps], group.iloc[[i]]])

    groups[numOfGrps - 1] = pd.concat([groups[numOfGrps - 1], groups[0].iloc[[-1]]])
    groups[numOfGrps - 2] = pd.concat([groups[numOfGrps - 1], groups[0].iloc[[-1]]])
    
    return groups

def toExcel(combinedDataframe, balancedGroups, sheet):
    for i, group in balancedGroups.items():
        if combinedDataframe.empty:
            combinedDataframe = group.reset_index(drop=True)
        else:
            combinedDataframe = pd.concat([combinedDataframe, pd.DataFrame(np.nan, index=combinedDataframe.index, columns=[''])], axis=1)
            combinedDataframe = pd.concat([combinedDataframe, group.reset_index(drop=True)], axis=1)
    
    # Write the combined DataFrame to an Excel file
    with pd.ExcelWriter(destinationFilePath, engine='openpyxl', mode='a') as writer:
        combinedDataframe.to_excel(writer, sheet_name=sheet, index=False)

for _ in range(seperation):
    #Filter out non Facilitators
    facilitatorsList = studentList[(studentList[roleColomnName] == faciIdentifier) if seperation == 1 else
                                   ((studentList[roleColomnName] == faciIdentifier) & 
                                    (studentList[studiesColumnName] == (foundationIdentifier if _ == 0 else degreeIdentifier)))].reset_index(drop = True)

    # Create balanced groups
    balancedGrps = create_balancedGrps(facilitatorsList, (numOfGrpFoundation if _ == 0 else numOfGrpDegree))

    # Combine groups into one DataFrame with each group separated by one column
    combinedDataframe = pd.DataFrame()

    toExcel(combinedDataframe, balancedGrps, ('FoundationFaci' if _ == 0 else 'DegreeFaci'))