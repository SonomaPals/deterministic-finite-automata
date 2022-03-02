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