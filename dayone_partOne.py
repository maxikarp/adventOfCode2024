
inputFile = open('dayone_input.txt')
listOne = []
listTwo = []
sumList = []


fileContent = (inputFile.read()).splitlines()

for i in range(len(fileContent)):
    currLine = fileContent[i].split('   ')
    listOne.append(currLine[0])
    listTwo.append(currLine[1])

listOne.sort()
listTwo.sort()

for i in range(len(listOne)):
    sumList.append(abs(int(listOne[i]) - int(listTwo[i])))

print('answer: ' + str(sum(sumList)))