import numpy as np
import time

# def quicksort2(A,p,r):
#     try:
#         if p < r:#there is a problem here because the next quicksort calls require matrices of at least 5.
#             print A
#             q = partition(A,p,r)
#             A = quicksort2(A,p,q-1)
#             A = quicksort2(A,q+1,r)
#             return A
#     except:
#         assert not type(A) == type(None)
#         return A

# def partition(A,p,r):
#     x = A[r]
#     i = p - 1
#     for j in range(p,r-1):
#         if A[j] <= x:
#             i += 1#increment i
#             tmp = A[i]#Next 3 lines swap A[i] and A[j]
#             A[i] = A[j]
#             A[j] = tmp
#     tmp = A[i + 1]#Next 3 lines swap A[i + 1] with A[r]
#     A[r] = A[i + 1]
#     A[i + 1] = A[r]
#     return i+1

class hybridSort(object):

    def __init__(self):

        pass

    def quick_sort(self,array):
        start = time.time()
        tmpArr = np.sort(array,kind='quicksort')
        return tmpArr, time.time()-start

    def insertion_sort(self,array):
        #This is a homebrew insertion sort algorithm
        start = time.time()
        iterarray = range(0, len(array), 1)
        for i in iterarray:
            j=i
            while(j > 0 and array[j-1] > array[j]):
                #swap(j-1,j)
                tmp = array[j-1]
                array[j-1] = array[j]
                array[j] = tmp
                j -= 1
        return array, time.time()-start

    # def myQS2(self,A,p,r):
    #     start = time.time()#for measuring calculation time
    #     try:
    #         if p < r:#if p less than r
    #             q = partition(A,p,r)#create new partititons about a pivot point q
    #             A = quicksort2(A,p,q-1)#quicksort from p to q-1 of partititon
    #             A = quicksort2(A,q+1,r)#quicksort from q+1 to r
    #             assert not type(A) == type(None), 'ASSERT 1'
    #             print(1)
    #             print(A)
    #             return A, time.time()-start
    #         else:
    #             assert not type(A) == type(None), 'ASSERT2'
    #             print(2)
    #             print(A)
    #             return A, time.time()-start
    #     except:
    #         assert not type(A) == type(None)
    #         print(3)
    #         print(A)
    #         return A, time.time()-start







