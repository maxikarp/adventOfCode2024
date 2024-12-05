import re

inputFile = open('dayThree/daythree_input.txt')
#inputFile = open('dayThree/daythree_small.txt', 'r')
#inputFile = open('dayTwo\errorLog.txt')

inString = inputFile.read()

patt = "^mul.([0-9].)"

allMul = re.search(patt, inString)