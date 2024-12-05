
inputFile = open('dayone_input.txt')
listOne = []
listTwo = []
sumList = []


fileContent = (inputFile.read()).splitlines()

for i in range(len(fileContent)):
    currLine = fileContent[i].split('   ')
    listOne.append(currLine[0])
    listTwo.append(currLine[1])

for i in range(len(listOne)):
    counter = 0
    for j in range(len(listTwo)):
        if listOne[i] == listTwo[j]:
            counter+= 1

    sumList.append(int(listOne[i])*counter)

print(sum(sumList))