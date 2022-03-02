import itertools

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
        self.next = [0] * len(self.possibleStringList)
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

def main():
    newObject = DfaClass()
    userInput = int(input("Enter a number n: "))
    print()
    print("n =", userInput, "    Answer:", count(newObject,userInput))
    print()
    return 0

main()