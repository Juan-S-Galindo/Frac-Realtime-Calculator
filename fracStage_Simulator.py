
import csv
import random
import time
import pandas as pd

#opens the file to simulate.
originalData_csv = pd.read_csv('SampleCSV.csv') #Specify the location of the CSV file to simulate <-------------
originalData_csv.iloc[[0]] = 0 #The first row of this specific CSV are units. Text is converted to 0 to be compatible with the to_numeric conversion.

#Creates lists to a store the information we need from the csv as numeric data.
time_list = pd.to_numeric(originalData_csv['Time']).to_list()
rate_list = pd.to_numeric(originalData_csv['Combined Slurry Rate']).to_list()
pressure_list = pd.to_numeric(originalData_csv['Well Side PSI']).to_list()
slurryTotal_list = pd.to_numeric(originalData_csv['Combined Slurry Total']).to_list()
totalProppant_list = pd.to_numeric(originalData_csv['Screw Prop Total']).to_list()
proppantConc_list = pd.to_numeric(originalData_csv['Wellhead Screw PPA']).to_list()
frConc_list = (pd.to_numeric(originalData_csv['Chem 8 Conc - C8']) + pd.to_numeric(originalData_csv['Chem 10 Conc - C10'])).to_list()

#Names of the headers for the CSV.
headerNames = ["Job Time (min)", "Dirty Rate (bpm)", "Pressure (psi)", 'Slurry Total (bbls)','Proppant Conc (ppg)','Total Proppant (lbs)', 'Friction Reducer (gpt)']

#Defines variables to use during the data simulation loop and assigns the starting values as first index of each list.
rowCount = 0 #Iteration counter to change index position in the loop.
timeGenerator = time_list[0]
rateGenerator = rate_list[0]
pressureGenerator = pressure_list[0]
slurryGenerator = slurryTotal_list[0]
totalPropGenerator = totalProppant_list[0]
propConcGenerator = proppantConc_list[0]
chemicalConceGenerator = frConc_list[0]

#Creates a csv
with open('simulationOutput.csv', 'w') as csv_file:

    #Writes the headers of the csvs
    csv_writer = csv.DictWriter(csv_file, fieldnames = headerNames)
    csv_writer.writeheader()

#Condtion for the while loop. 
loopCondition = True

#While the loop condition is true, perform the loop.
while loopCondition == True:

    #Opens the file in append mode. 
    with open('simulationOutput.csv', 'a') as csv_file:

        csv_writer = csv.DictWriter(csv_file, fieldnames = headerNames)

        #Maps where to append the information. 
        info = {
            'Job Time (min)': timeGenerator,
            'Dirty Rate (bpm)': rateGenerator,
            'Pressure (psi)': pressureGenerator,
            'Slurry Total (bbls)' : slurryGenerator,
            'Proppant Conc (ppg)' : propConcGenerator,
            'Total Proppant (lbs)' : totalPropGenerator,
            'Friction Reducer (gpt)' : chemicalConceGenerator
        }

        #Writes the information in the row.
        csv_writer.writerow(info)

        #Can print the log in the console.
        print(timeGenerator, rateGenerator, pressureGenerator, slurryGenerator, propConcGenerator, totalPropGenerator, chemicalConceGenerator)

        #After appending the row, add 1 to the  counter
        rowCount += 1 #Make sure to return to 1 <--------------------------------

        #Stores the information fo the next iteration. 
        timeGenerator = time_list[rowCount]
        rateGenerator = rate_list[rowCount]
        pressureGenerator = pressure_list[rowCount]
        slurryGenerator = slurryTotal_list[rowCount]
        propConcGenerator = proppantConc_list[rowCount]
        totalPropGenerator = totalProppant_list[rowCount]
        chemicalConceGenerator = frConc_list[rowCount]

        #Assigns the time delay.
        time.sleep(1)

    if rowCount == len(originalData_csv) - 1:  #use len(originalData) to run the whole csv.
        loopCondition = False
