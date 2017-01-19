import csv
import json

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

inputFile = []
outputList = []

def findPair(name):
    backendName = name
    
    for pair in namePairs:
        if name == pair['readableName']:
            backendName = pair['backendName']
    return backendName

def writeProperties(propertyList):
    language = propertyList[0][1].split('_')
    language = language[0]
    
    with open('messages_'+ language +'.properites', 'w') as outputFile:
        for row in propertyList:
            if row[0] and row[1] != "":
                outputString = row[0] + " = " + row[1] + "\n"
                outputFile.write(outputString)

fileSelected = raw_input("What file would you like to export to properties files? ")

with open(fileSelected, 'r') as languagesFile:
        reader = csv.reader(languagesFile)
        
        for row in reader:
            #print row
            inputFile.append(row)
            
with open('definitions.json') as pairsFile:
    pairsData = json.load(pairsFile)
    namePairs = pairsData['pairs']
    
#print len(inputFile[0])

count = 2

while count < len(inputFile[0]):
    for row in inputFile:
        #print row
        
        outputList.append([findPair(row[1]),row[count]])
        
        writeProperties(outputList)
        
    count = count + 1