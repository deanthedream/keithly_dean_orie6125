import numpy as np
import time

def quicksort2(A,p,r,K):
    if A.shape[0] < K:
        if p < r:#there is a problem here because the next quicksort calls require matrices of at least 5.
            print A
            q = partition(A,p,r)
            A = quicksort2(A,p,q-1,K)
            A = quicksort2(A,q+1,r,K)
            return A
    else:
        return insertion_sort(A)

def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r-1):
        if A[j] <= x:
            i += 1 # increment i
            tmp = A[i] # Next 3 lines swap A[i] and A[j]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i + 1] # Next 3 lines swap A[i + 1] with A[r]
    A[r] = A[i + 1]
    A[i + 1] = A[r]
    return i+1

def insertion_sort(array):
    #This is a homebrew insertion sort algorithm
    iterarray = range(0, len(array), 1)
    for i in iterarray:
        j=i
        while(j > 0 and array[j-1] > array[j]):
            #swap(j-1,j)
            tmp = array[j-1]
            array[j-1] = array[j]
            array[j] = tmp
            j -= 1
    return array

class hybridSort(object):

    def __init__(self):

        pass

    def quick_sort(self,array):#this is the default numpy quicksort implmentation. It currently uses the optimal K parameter
        start = time.time()
        tmpArr = np.sort(array,kind='quicksort')
        return tmpArr, time.time()-start

    def myQS2(self,A,p,r,K):
        start = time.time()
        if A.shape[0] < K:
            if p < r:#there is a problem here because the next quicksort calls require matrices of at least 5.
                print A
                q = partition(A,p,r)
                A = quicksort2(A,p,q-1,K)
                A = quicksort2(A,q+1,r,K)
                return A, time.time()-start
        else:
            return insertion_sort(A), time.time()-start








