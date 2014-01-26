#!/usr/bin/python
import sys
import os
import nltk
from collections import Counter
import csv


# Function to return the file contents as List
def returnList(fileName):
    wordsList = []
    if os.path.exists(fileName):
        try:
            f = open(fileName)
            lines = f.read()
            linesLower = lines.lower()
            wordsList = linesLower.split()
        except :
            print "Error in Handing File:", fileName
            sys.exit()
    return wordsList


#Counter Initialization

# Using Python Natural Language ToolKit to generate the Sentimental Analysis

#To Count the words in each sentiment 
def getCount(freqDist,sentList):
    count = 0
    for word in sentList:
        if freqDist.has_key(word):
            count += freqDist[word]
    return count

def getArticleCount(split_paper):
    # TO Open up the file handling 
    countList = []
    lowerArticle = split_paper.lower()
    wordsArticle = lowerArticle.split()
    freqDist = nltk.FreqDist(wordsArticle)
    
    positiveCount = 0
    negativeCount = 0
    modalWeakCount = 0
    modalStrongCount = 0
    litigiousCount = 0
    uncertaintyCount = 0
    
    positiveList = returnList('positive.txt')
    negativeList = returnList('negative.txt')
    modalWeakList = returnList('modal_weak.txt')
    modalStringList = returnList('modal_strong.txt')
    litigiousList = returnList('litigious.txt')
    uncertaintyList =  returnList('uncertainty')

    positiveCount = getCount(freqDist,positiveList)
    negativeCount = getCount(freqDist,negativeList)
    modalWeakCount = getCount(freqDist,modalWeakList)
    modalStrongCount = getCount(freqDist,modalStringList)
    litigiousCount = getCount(freqDist, litigiousList)
    uncertaintyCount = getCount(freqDist, uncertaintyList)
    
    #Getting the values for each sentiment
    #Printing the values
    print 'Positive Count:', positiveCount
    print 'Negative Count:', negativeCount
    print 'Modal Weak Count:', modalWeakCount
    print 'Modal Strong Count:', modalStrongCount
    print 'Litigious Count:', litigiousCount
    print 'Uncertainty Count:', uncertaintyCount


    countList.append(positiveCount)
    countList.append(negativeCount)
    countList.append(modalWeakCount)
    countList.append(modalStrongCount)
    countList.append(litigiousCount)
    countList.append(uncertaintyCount)
    
    return countList
