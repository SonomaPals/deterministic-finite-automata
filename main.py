import itertools
from queue import Queue

# Problem 1: 
class DfaClass:
    def __init__(self):
        possibleStringList = []
        dictionaryCounter = {}
        counterList = []
        counterList.append(0)
        counterForDict = 0
        possibleStringList.append("")
        for i in range(1, 6):
            for str in itertools.product("abcd", repeat=i):
                someString = ""
                someString = someString.join(str)
                possibleStringList.append(someString)
                counterForDict = counterForDict + 1
                counterList.append(counterForDict)               
        for aString in possibleStringList: 
            key = possibleStringList.index(aString)
            dictionaryCounter[key] = aString
        self.possibleStringList = possibleStringList
        next = [0] * len(self.possibleStringList)
        self.prev = [1] * len(self.possibleStringList)
        self.next = next
        self.dictionaryCounter = dictionaryCounter

    def grabStateNum(self,inputString):
        CharactersOfTheString = []
        stateNum = 0
        if (inputString == ""):
            return 0
        for char in inputString:
            CharactersOfTheString.append(char)
        for i in range(0, len(CharactersOfTheString)):
            if CharactersOfTheString[i] == 'a':
                stateNum = stateNum + 1 * pow(4, (len(CharactersOfTheString) - 1) - i)

            elif CharactersOfTheString[i] == 'b':
                stateNum = stateNum + 2 * pow(4, (len(CharactersOfTheString) - 1) - i)

            elif CharactersOfTheString[i] == 'c':
                stateNum = stateNum + 3 * pow(4, (len(CharactersOfTheString) - 1) - i)

            elif CharactersOfTheString[i] == 'd':
                stateNum = stateNum + 4 * pow(4, (len(CharactersOfTheString) - 1) - i)
            else:
                print("ERROR: NO a,b,c, or d detected")
                exit(9)
        return stateNum

    def isValid(self,string):
        if len(string) < 6:
            return True
        founda = False
        foundb = False
        foundc = False
        foundd = False
        for char in string:
            if char == 'a':
                founda = True
            if char == 'b':
                foundb = True
            if char == 'c':
                foundc = True
            if char == 'd':
                foundd = True
        if (founda and foundb and foundc and foundd):
            return True
        else:
            return False
        
    def transBigQual(self, stateNum, string):
        stateCounter = 0
        string1 = "".join((string,"a"))
        string2 = "".join((string,"b"))
        string3 = "".join((string,"c"))
        string4 = "".join((string,"d"))
        if(self.isValid(string1)):
            if(5 < len(string1)):
                string1 = string1[1:]
            stateCounter += self.prev[self.grabStateNum(string1)]
        if(self.isValid(string2)):
            if(5 < len(string2)):
                string2 = string2[1:]
            stateCounter += self.prev[self.grabStateNum(string2)]
        if(self.isValid(string3)):
            if(5 < len(string3)):
                string3 = string3[1:]
            stateCounter += self.prev[self.grabStateNum(string3)]
        if(self.isValid(string4)):
            if(5 < len(string4)):
                string4 = string4[1:]
            stateCounter += self.prev[self.grabStateNum(string4)]
        self.next[stateNum] = stateCounter

def count(self,n):
    for c in range(n):
        for j, k in self.dictionaryCounter.items(): 
            self.transBigQual(j, k)
        self.prev = self.next
        self.next = [0] * len(self.possibleStringList)
    return self.prev[0]

##############################################################################################################
# Problem 2:
def shortest_string_accepted(k, d):
    Q = Queue()
    visited = [0] * k  # initializing visited, parent and label to false
    parent = [0] * k
    label = [0] * k

    for i in d:             # updating the table with the user input
        Q.put(i)
        visited[i] = 1
        parent[i] = 0
        label[i] = i

    while not Q.empty():
        current = Q.get()   # deleting from the Queue
        for digit in d:         # all posible digits ex. [1, 3]
            delta = (10 * current + digit) % k  # Mod that number
            if visited[delta] == 0:
                visited[delta] = 1
                Q.put(delta)
                parent[delta] = current
                label[delta] = digit
    if visited[0] != 1:
        return print("No Solution")
   
    result = ""
    curr = 0
    result += str(label[curr])
    while parent[curr] > 0:
        result += str(label[parent[curr]])
        curr = parent[curr]
    print(result[::-1])           
    

def main():

    print("Problem 1")
    n = 100
    newObject = DfaClass()
    print(count(newObject, n))

    print("Problem 2")
    k = 26147
    d = [1, 3]
    print(shortest_string_accepted(k, d))

    return 0

main()