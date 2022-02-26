import os.path
import re

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
        wordStat[tempList[0]] = 1     
        for i in range(len(tempList)):
            if tempList[i] in wordStat:
                wordStat[tempList[i]] +=1
            else:
                wordStat[tempList[i]] = 1
        for key, value in wordStat.items():
           print(key, ':', str(value), sep = '')
        
    def GetSentenceList(self): 
        sentenceList = []
        i = 1
        for element in self.list:
            if "." in element or "?" in element or "!" in element :
                sentenceList.append(i)
                i = 1
            else:
                i += 1
        sentenceList.sort()
        self.sentenceList = sentenceList
    
    def CountMedian(self):
        self.GetSentenceList()
        length = len(self.sentenceList)
        median = 0
        average = 0
        for element in self.sentenceList:
            average += element
        average /= length
        print(average)
        if length % 2 == 1:
            median = self.sentenceList[int(length/2)+1] 
        else: 
            median = (self.sentenceList[length/2]+self.sentenceList[length/2+1])/2
        print(median)
    
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

man = Statsman()
man.GetText()
man.WordsCounter()
man.CountMedian()
man.NGramsCounter()


