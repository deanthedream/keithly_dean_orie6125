import numpy as np
import random
import math

def bisect(key,uO,lbi,ubi):
    #print(uO[np.arange(ubi-lbi)+lbi])
    bInd = (ubi-lbi)/2+lbi
    # bIndu= int(math.ceil(bInd))
    # bIndl = int(math.floor(bInd))#bisecting Index
    bInd = int(bInd)

    #Here we check if key is at bInd
    if(key == uO[bInd]):
        return bInd

    assert lbi != ubi,'lbi and ubi are the same'

    lb = uO[lbi]
    ub = uO[ubi]
    bi = uO[bInd]
    k = key

    if(lb < bi):#case 1.1, 1.2, 1.3, 1.4, 3.1, 3.2, 3.3, 3.4
        if(ub < bi):#case 1.1, 1.2, 1.3, 1.4, 3.3, 3.4
            if(lb < k):#case 1.1, 1.2, 3.3, 3.4
                if(ub < k):#case 1.1, 1.2, 3.3, 3.4
                    if(bi > k):#case 1.1, 3.3
                        print('Case 1.1 or Case 3.3')
                        return bisect(k,uO,lbi,bInd)
                    else:#(bi < k) case 1.2, 3.4
                        print('Case 1.2 or Case 3.4')
                        return bisect(k,uO,bInd,ubi)
                else:#(ub > k)
                    print('ERROR 3 no cases for this')
                    print(key)
                    print(uO)
                    print([lb,bi,ub])
                    assert(False)
            else:#(lb > k) case 1.3, 1.4
                #NO POINT TO THIS CHECK
                if(ub < k):#case 1.4
                    print('case 1.4')
                    return bisect(k,uO,bInd,ubi)
                else:#(ub > k) case 1.3
                    print('case 1.3')
                    return bisect(k,uO,bInd,ubi)
        else:#(ub > bi) case 3.1, 3.2 
            if(lb < k):#case 3.1, 3.2
                if(ub < k):#case 
                    print('ERROR 4 no cases for this')
                    print(key)
                    print(uO)
                    print([lb,bi,ub])
                    assert(False)
                else:#(ub > k) case 3.1, 3.2
                    if(bi > k):#case 3.1
                        print('case 3.1')
                        return bisect(k,uO,lbi,bInd)
                    else:#(bi < k) case 3.2
                        print('case 3.2')
                        return bisect(k,uO,bInd,ubi)
            else:#(lb > k) case
                print('ERROR 2 no cases for this')
                print(key)
                print(uO)
                print([lb,bi,ub])
                assert(False)
    else:#(lb > bi) case 2.1, 2.2, 2.3, 2.4, 3.5, 3.6
        if(ub < bi):#case SPECIAL 1 where
            if(lb < k):
                return bisect(k,uO,lbi,bInd)# IDK if this is right but its something
            else:#(lb > k)#does this even make sense?
                return bisect(k,uO,bInd,ubi)# IDK of this is right but its something
            print('ERROR 1 no cases for this')
            # print(key)
            # print(uO)
            # print([lb,bi,ub])
            # assert(False)
        else:#(ub > bi) case 2.1, 2.2, 2.3, 2.4, 3.5, 3.6 
            if(lb < k):#case 2.3
                print('case 2.3')
                return bisect(k,uO,lbi,bInd)
            else:#(lb > k) case 2.1, 2.2, 2.4, 3.5, 3.6
                if(ub < k):#case 2.4
                    print('case 2.4')
                    return bisect(k,uO,lbi,bInd) 
                else:#(ub > k) case 2.1, 2.2, 3.5, 3.6
                    if(bi > k):#case 2.2, 3.5
                        print('case 2.2 or case 3.5')
                        return bisect(k,uO,lbi,bInd)
                    else:#(bi < k) case 2.1, 3.6
                        print('case 2.1 or case 3.6')
                        return bisect(k,uO,bInd,ubi)

    # if(uO[lbi] < uO[bInd] and uO[bInd] < uO[ubi]):#Case 3 (all 3 on same sorted array)
    #     if(uO[bInd] < key):
    #         print('case 3.1')
    #         return bisect(key,uO,bInd,ubi)#same sorted array right of bisector
    #     else:
    #         print('case 3.2')
    #         return bisect(key,uO,lbi,bInd)#same sorted array left of bisector
    # elif(uO[bInd] > uO[ubi]):#Case 1 (bInd is greater than ubi) lbi and bInd are on same sorted array
    #     if(uO[lbi] < key):#True for cases 1.1,1.2
    #         if(uO[bInd] > key):#case 1.1
    #             print('case 1.1')
    #             return bisect(key,uO,lbi,bInd)
    #         else:#case 1.2
    #             print('case 1.2')
    #             return bisect(key,uO,bInd,ubi)
    #     else:#(uO[lbi] > key)#True for cases 1.3,1.4
    #         if(uO[ubi] > key):#case 1.3
    #             print('case 1.3')
    #             return bisect(key,uO,bInd,ubi)
    #         else:#case 1.4
    #             print('case 1.4')
    #             return bisect(key,uO,bInd,ubi)
    # elif(uO[bInd] < uO[ubi]):#Case 2 (bInd is less than ubi) ubi and lbi are on the same slab
    #     if(uO[lbi] < key):#True for cases 2.3
    #         print('case 2.3')
    #         return bisect(key,uO,lbi,bInd)
    #     else:#(uO[lbi] > key)#True for cases 2.1,2.2,2.4
    #         if(uO[ubi] < key):#True for case 2.4
    #             print('case 2.4')
    #             return bisect(key,uO,lbi,bInd)
    #         else:#Case 2.1,2.2
    #             if(uO[bInd] < key):#True for case 2.1
    #                 print('case 2.1')
    #                 return bisect(key,uO,bInd,ubi)
    #             else:#case 2.2
    #                 print('case 2.2')
    #                 return bisect(key,uO,lbi,bInd)
    # else:#IDK there is some unhandled case
    #     print('Error')


    # if(uO[lbi] < key):
    #     if(uO[bInd] > key):
    #         if(uO[ubi] < key):
    #             print('case 1.1')
    #             return bisect(key,uO,lbi,bInd)
    #         else:#(uO[ubi] > key)
    #             print('case DNE 1')
    #             return
    #     else:#(uO[bInd] < key) #key should be between bInd and ubi
    #         if(uO[ubi] < key):
    #             print('case 1.2')
    #             return bisect(key,uO,bInd,ubi)
    #         else:#(uO[ubi] > key)




    # #mostly works but there is some error in here
    # if(key >= uO[lbi] and key < uO[bInd]):#case 1.1
    #     print('case 1.1')
    #     return bisect(key,uO,lbi,bInd)
    # elif(key >= uO[lbi] and key > uO[bInd]):#case 1.2
    #     print('case 1.2')
    #     return bisect(key,uO,bInd,ubi)
    # elif(key < uO[lbi] and key < uO[bInd]):#case 1.3
    #     print('case 1.3')
    #     return bisect(key,uO,lbi,bInd)
    # elif(key <= uO[ubi] and key < uO[bInd]):#case 2.1
    #     print('case 2.1')
    #     return bisect(key,uO,lbi,bInd)
    # elif(key <= uO[ubi] and key > uO[bInd]):#case 2.2
    #     print('case 2.2')
    #     return bisect(key,uO,bInd,ubi)
    # elif(key > uO[ubi] and key > uO[bInd]):#case 2.3
    #     print('case 2.3')
    #     return bisect(key,uO,bInd,ubi)
    # else:
    #     print('Passing')
    #     pass

class findElement(object):
    
    def __init__(self):
        self.ordered = np.sort(np.unique(np.random.randint(0,high=100, size=10)))#Generate random array
        self.n = self.ordered.shape[0]##number of integers in array

        #pick random index from 0 to n-1
        i = np.random.randint(0,self.n-1)
        self.unordered = np.concatenate([self.ordered[np.arange(i+1,self.n)],np.reshape(np.asarray(self.ordered[i]),(1,)),self.ordered[np.arange(0,i)]],axis=0)#includes start, excludes stop

    def find_element(self,key):
        #print('Finding Element %d'%key)
        uO = self.unordered
        self.key = key
        #Search upper array
        lbi = 0 #lower bound ind
        lb1 = uO[lbi]#lower bound of 1
        ubi = uO.shape[0]-1#upper bound ind
        ub1 = uO[ubi]#upper bound of 2

        #check if either endpoint
        if(key == uO[lbi]):
            return lbi
        elif(key == uO[ubi]):
            return ubi

        sInd = bisect(key,uO,lbi,ubi)
        return sInd
