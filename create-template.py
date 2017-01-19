import json
import csv

def findProperty(inputProperty):
    
    for index, pair in enumerate(namePairs):
        #print pair
        for value in pair:
            #print namePairs[index][value]
            
            if namePairs[index][value] == inputProperty:
                #print index
                return index
    
    return ""
        
def writeTemplate(csvList):
    with open('template.csv', 'w') as outputFile:
        writer = csv.writer(outputFile, delimiter=',')
    
        for row in csvList:
            writer.writerow(row)


#add input for entering the name of the file you would like to process

with open('definitions.json') as pairsFile:
    pairsData = json.load(pairsFile)
    namePairs = pairsData['pairs']

#fileToConvert = raw_input("What file would you like to convert to a template? ")

#print fileToConvert

with open('messages_en_template.properties') as file:
    inputList = []
    
    for line in file:
        #need to check for missing spaces
        splitLine = line.split(' = ')
        
        #splitLine[1].rstrip()
        
        #print splitLine[1]
        
        inputList.append(splitLine)
        #print splitLines

outputList = []

outputList.append(["","Property","en_US"])
#outputList.append(["Widget","","en_US"])

for item in inputList:
    templateRow = findProperty(item[0])
    
    if templateRow != "":
        outputList.append([namePairs[templateRow]['location'],namePairs[templateRow]['readableName'],item[1].rstrip()])
    else:
        outputList.append(["",item[0],item[1].rstrip()])
    
    
#print outputList
    
writeTemplate(outputList)

