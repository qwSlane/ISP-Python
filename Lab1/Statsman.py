import os.path
import re
import Variables

class Statsman():

    def GetText(self):        #text input
        print("Set file path")
        path = input()
        while not os.path.isfile(path):
            print("File doesn't exist")
            path = input()
        with open(path) as file:
            self.text = file.read()
        self.list = self.text.split()
        while '-' in self.list:
            self.list.remove('-')

    def WordsCounter(self):
        tempList = []
        for element in self.list:
            tempList.append(re.sub(r'[,.?!:;"]','', element).lower())
        wordStat = {}  
        for i in range(len(tempList)):
            if tempList[i] in wordStat:
                wordStat[tempList[i]] +=1
            else:
                wordStat[tempList[i]] = 1
        for key, value in wordStat.items():
           print(key, ':', str(value), sep = '')
    
    def GetSentList(self):  #word counter in sentences
        self.sentenceList = []
        i = 1
        print(self.list)
        for k in range(len(self.list)):
            if '.' in self.list[k] or '?' in self.list[k] or '!' in self.list[k]:
                print(self.list[k])
                if self.list[k] in Variables.specials:
                    i+=1
                    continue
                else:
                    try:
                        if self.list[k+1].isupper():
                            self.sentenceList.append(i)
                            i = 1
                        else:
                            i +=1
                    except:
                        self.sentenceList.append(i)
                        break
            else:
                i += 1

    def CountMedian(self):
        self.GetSentList()
        length = len(self.sentenceList)
        median = 0
        average = 0
        print(self.sentenceList)
        if length > 1:
            for element in self.sentenceList:
                average += element
            average /= length
            print(average)
            if length % 2 == 1:
                median = self.sentenceList[int(length/2)+1] 
            else: 
                median = (self.sentenceList[length/2]+self.sentenceList[length/2+1])/2
            print(median)
        else:
            median = average = self.sentenceList[0]
            print("Average in sentence:",average)
            print("Median in sentence:", median)
    
    def NGramsCounter(self):
        NGramsList = {}
        tempList = []
        print("write k")
        K = input()
        print("write N")
        N = input()
        try:
           n = int(N)
           k = int(K)
        except:
            n = 4
            k = 10
        for element in self.list:
            tempList.append(re.sub(r'[,.?!:;"]','', element))
        for element in tempList:
            if len(element) < n:
                continue
            else:
                for i in range(len(element)):
                    if i+n <= len(element):
                        word = ''
                        for j in range(i,i+n):
                            word +=element[j]
                        if word in NGramsList:
                            NGramsList[word] +=1
                        else:
                            NGramsList[word] = 1
                    else:
                        break
        sortedDict = dict(sorted(NGramsList.items(), 
            key = lambda item: item[1], reverse=True))
        iter = 1 
        for key, value in sortedDict.items():
           print(key, ':', str(value), sep = '')
           if iter ==  k:
               break
           else:
               iter +=1


