import numpy as np
import random
import hmwk2PATHS
from homework2.hybridSort import hybridSort
hmwk2PATHS
# import matplotlib.pyplot as plt

hS = hybridSort()#create Instance

timeQS = list()
#timeIS = list()
timeQS2 = list()
ArrayLength = 100
for i in np.arange(ArrayLength-1)+1:#The length of each array to sort
    unsorted = np.asarray(random.sample(range(1,(ArrayLength-1)*10),ArrayLength))#np.unique(np.random.randint(0,high=1000, size=i))
    sortedArrayQS, timeQStmp = hS.quick_sort(unsorted.copy())
    #sortedArrayIS, timeIStmp = hS.insertion_sort(unsorted.copy())
    sortedArrayQS2, timeQS2tmp = hS.myQS2(unsorted.copy(),0,unsorted.copy().shape[0]-1,i)
    timeQS.append(timeQStmp)
    #timeIS.append(timeIStmp)
    timeQS2.append(timeQS2tmp)
    #assert sortedArrayQS.tolist() == sortedArrayIS.tolist(),'Arrays are not identical'
    #assert sortedArrayQS.tolist() == sortedArrayQS2.tolist(), 'Arrays are not identical'

    if i%100 == 0:
        print(i)

# plt.plot(np.arange(ArrayLength-1)+1,timeQS,color='r',marker='x')
# #plt.plot(np.arange(ArrayLength-1)+1,timeIS,color='b',marker='o')
# plt.plot(np.arange(ArrayLength-1)+1,timeQS2,color='k',marker='d')
# plt.xlabel('Array Length')
# plt.ylabel('Execution Time (seconds)')
# plt.legend(['Quicksort','Insertion Sort'])
# plt.show(block=False)



#key = random.choice(fE.unordered)
#sInd = fE.find_element(key)