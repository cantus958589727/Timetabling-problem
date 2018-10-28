import datetime

sArray = ['BIOINFO', 'Mr. Anish']
sArray2 = ['COMPRO2' , 'S. Alain']
sArray3 = ['COMPRO', 'Ms. Tessie']
sArray4 = ['MACLERN', 'Ms.Courtney']
sArray5 = ['ADVDISC', 'S. Duke']

SubMatrix = [sArray, sArray2, sArray3, sArray4, sArray5]
SubMatrix2 = SubMatrix

##SubMatrix[0][0] = sArray
##SubMatrix[0][1] = sArray2
##SubMatrix[0][2] = sArray3


##print(SubMatrix[0][1])
##print(SubMatrix[2][0])

MainMatrix = []
MainMatrix.append(SubMatrix)

sArray = ['WEBAPDE', 'S. Stephen']
sArray2 = ['MOBAPDE' , 'S. Miguel']
sArray3 = ['TREDONE', 'Ms. Pia']

SubMatrix = [sArray, sArray2, sArray3]

MainMatrix.append(SubMatrix)
MainMatrix.append(SubMatrix2)
MainMatrix.append(SubMatrix)

print(MainMatrix[0])
print(MainMatrix[1])
print(MainMatrix[2])
print(MainMatrix[3])

MainMatrix.pop(2)
print(MainMatrix[2])
print(len(MainMatrix))
##6 means there are 6 classes with 15 mins break in between every day
##7:30 - 5:45

##mArray = []
##tArray = []
##wArray = []
##thArray = []
##fArray = []
##
##sampleArray = ['samplecourse', 'sampleprof']
##mArray.append(sampleArray)
##
##print(mArray)
#### sampleArray[0] = 'samplecourse2' do not do this because it will edit the array
#### defined earlier
##
##
##print(mArray)
##print(sampleArray)
