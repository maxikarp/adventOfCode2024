inputFile = open('dayTwo\daytwo_input.txt')
#inputFile = open('dayTwo\daytwo_small.txt')
#inputFile = open('dayTwo\errorLog.txt')

fileContent = (inputFile.read()).splitlines()

safeReports = 0

def isAsc(r):
    for i in range (len(r)-1):
        if int(r[i]) < int(r[i+1]):
            continue
        else:
            return False
    return True

def isDesc(r):
    for i in range (len(r)-1):
        if int(r[i]) > int(r[i+1]):
            continue
        else:
            return False
    return True

def isSorted(r):
    if(isAsc(r) or isDesc(r)):
        return True
    return False

def checkAdj(r):
    for i in range (len(r)-1):
        if abs( (int( r[i+1] ) - int (r[i] )) ) in [1,2,3]:
            continue
        else:
            return False
    return True


for i in range (len(fileContent)):

    currReport = fileContent[i]
    reportList = currReport.split(' ')

    if (isSorted(reportList) and checkAdj(reportList)):
        safeReports += 1

print(safeReports)