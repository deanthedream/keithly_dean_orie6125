import numpy as np


class binaryArray(object):


    def __init__(self):
        self.binaryArray = np.random.randint(2, size=10)*2-1#generate a random array of length 10 with 1's and -1's


    def find_longest(self):
        """A function to find the longest binarySubarray where the sum is 0.
        """
        bA = self.binaryArray
        n = bA.shape[0]#length of binary Array
        mySum = np.zeros([n])
        firstList = list()
        lastList = list()
        lastIndex = list()
        firstIndex = list()
        for i in np.arange(n):
            try:
                mySum[i] = mySum[i-1] + bA[i]
            except:
                mySum[i] = bA[i]
            if mySum[i] in firstList:#check if this sum is in the first occurance list
                if mySum[i] in lastList:#Have we seen the second occurance of this value?
                    tmpInd = [k for k in np.arange(len(lastList)) if lastList[k] == mySum[i]][0]
                    lastIndex[tmpInd] = i#Update index entry
                else:#This is the first time we have seen this number second
                    lastList.append(mySum[i])#keep track of last Value
                    lastIndex.append(i)#keep track of last index
            else:#Not in first occurance List so add it
                firstList.append(mySum[i])#keep track of first Value
                firstIndex.append(i)#keep track of first index
        # Find index of first occurance of all values that occured more than once
        maxSeq = np.zeros(len(lastList))
        for i in np.arange(len(lastList)):#iterate through all elements in last list
            tmpInd = [k for k in np.arange(len(firstList)) if firstList[k] == lastList[i]][0]
            maxSeq[i] = lastIndex[i] - firstIndex[tmpInd]#difference between last occura and first occurence
        ind = np.argmax(maxSeq)#Get the index of the maximum
        val = maxSeq[ind]#get the value of the maximum
        lastIndex[ind]#We h
        myInd = [tmpInd for tmpInd in np.arange(len(firstList)) if firstList[tmpInd]==lastList[ind]][0]#Find where this value occurs in first ind
        return firstIndex[myInd], lastIndex[ind]
