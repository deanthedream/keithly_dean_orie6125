# import os 
# import sys

# spark_home = os.environ.get('SPARK_HOME', None)
# sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.10.6-src.zip'))
# sys.path.insert(0, os.path.join(spark_home, 'python'))
# sc = execfile(os.path.join(os.environ["SPARK_HOME"], 'python/pyspark/shell.py'))

# #Notes must be run from new terminal with "source .bashrc" having never been called. This extends the $SPARK_HOME path length each time it is called.

#From here https://stackoverflow.com/questions/23256536/importing-pyspark-in-python-shell
import findspark
findspark.init()
#import the necessary modules

import sys
from pyspark import SparkContext
from pyspark import SparkConf

#goal recommend 10 friend recommendations for each person
conf = SparkConf()
sc = SparkContext(conf=conf)
#sc = SparkContext('local[*]')

# def myFunc(s):
#     person = s.splitlines()#("\n")#should be split into the number of lines that there are people
#     #line = person.split("\t")
#     #line[0] # each person1
#     #friends = line[1].split(",") # each friend of person1
#     peopleDict = {}
#     for person1 in person:#Iterate through each line (person1)
#         line1 = person1.split("\t")#Split each line by the tab. line[0] is the current person. line[1] is the string of person's friends
#         person1Dict = {}#create empty dictionary for person1
#         p1friends = line1[1].split(",")# a list containing all the friends of person1
#         for person2 in person:#Iterate through each person2 (person2 = friend of person1)
#             line2 = person2.split("\t")#Split each line by the tab. line[0] is the current person. line[1] is the string of person's friends
#             if line2 in p1friends:#if the current person (line2) is a friend of person1
#                 #Iterate through all friends of line2, add 1 for each friend
#                 person1Dict[line2] = 1
#         peopleDict[line1] = person1Dict
#     return peopleDict


# #TRY 1########################################################################################################################
# # SAMPLE DATA
# tmpdat = sc.textFile('/home/dean/Documents/keithly_dean_orie6125/homework3/socialNetworkFriendAlgorithm/out.txt')

# #tmpdat.map(str)# operation strips lines of unicode information  https://stackoverflow.com/questions/34479444/how-to-remove-unicode-when-reading-data
# lines = tmpdat.map(lambda line: str(line).split("\n"))#should split file into subcomponents by line
# tmp1 = lines.collect() # produces a list containing each line of the file
# people = lines.map(lambda people: (people[0].split("\t")[0], people[0].split("\t")[1].split(",")))
# tmp25 = people.collect()
# #tmp25 has form
# #people[0] = first line of form tuple (person1, friends1)
# #people[0][0] = person1 = '0'
# #people[0][1] = friends1
# #friends1 = list of friends ['1','5','6',...]
# ###################################################
# def myFunc2(people):
#     pFFlist = list()
#     peopleIndex = [item[0] for item in people]#list of all first terms in people
#     print('peopleIndex: ' + str(peopleIndex))
#     print('people: ' + str(people))
#     for person1 in people:#iterate over each person tuple
#     person1 = people
#         print('person1: ' + str(person1))
#         person1Num = person1[0]#person1 number ex. '0'
#         print('person1[0]: ' + str(person1[0]))
#         person1Friends = person1[1] #friends of person1 ex. '1' #LINE8
#         print('person[1]: ' + str(person1[1]))
#         for friend1 in person1Friends:#iterate over each friend of person#LINE 8
#             #add all friends of friend1 to pFFlist[person]
#             if friend1 in peopleIndex:# Would look like this if array -> people[:][0]:
#                 friend1Index = peopleIndex.index(friend1)#get index of friend in people
#                 for person2 in people[friend1Index]:#iterate through all friend2 of friend1
#                     person2Num = person2[0] # friends of person2 (should also be friend1)
#                     person2friends = person2[1] # friends of person2
#                     pFFlistIndex = [item[0] for item in pFFlist]#list of all first terms in pFFlist
#                     for friend2 in person2friends:
#                         if not friend2 == friend1:#So long as friend2 is not a friend of person1
#                             pFFlist[pFFlistIndex.index(friend2)].append(person1Num) #append person1Num to remaining friends of (friends of person1)
#             else:
#                 pFFlist.append(friend2)
#                 pFFlist[-1].append(person1Num)
#     return pFFlist
# #########################################################
# #pFFlist = list()
# #people does not work with myFunc2 since people must be a fully intact list...
# #I could just expand the tuples a few times. that might work....
# peopleFofF = people.map(lambda people: myFunc2(people)) # Watch out, people may only be first index (this means we might not need first for loop)
# tmp3 = peopleFofF.collect()

# #LOGIC ######################################
# pFFlist = list()
# peopleIndex = [item[0] for item in people]#list of all first terms in people
# for person1 in people[:]:#iterate over each person tuple
#     person1Num = person1[0]#person1 number ex. '0'
#     person1Friends = person1[1] #friends of person1 ex. '1'
#     for friend1 in person1Friends:#iterate over each friend of person
#         #add all friends of friend1 to pFFlist[person]
#         if friend1 in peopleIndex:# Would look like this if array -> people[:][0]:
#             friend1Index = peopleIndex.index(friend1)#get index of friend in people
#             for person2 in people[friend1Index]:#iterate through all friend2 of friend1
#                 person2Num = person2[0] # friends of person2 (should also be friend1)
#                 person2friends = person2[1] # friends of person2
#                 pFFlistIndex = [item[0] for item in pFFlist]#list of all first terms in pFFlist
#                 for friend2 in person2friends:
#                     if not friend2 == friend1:#So long as friend2 is not a friend of person1
#                         pFFlist[pFFlistIndex.index(friend2)].append(person1Num) #append person1Num to remaining friends of (friends of person1)
# #######################################################
# ############################################################################################################################33





# #Notes must be run from new terminal with "source .bashrc" having never been called. This extends the $SPARK_HOME path length each time it is called.

#From here https://stackoverflow.com/questions/23256536/importing-pyspark-in-python-shell
import findspark
findspark.init()
#import the necessary modules

import sys
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sqp.functions import collect_list

#goal recommend 10 friend recommendations for each person
conf = SparkConf()
sc = SparkContext(conf=conf)
#TRY 2########################################################################################################################
# SAMPLE DATA
import numpy as np
#file = sc.textFile('/home/dean/Documents/keithly_dean_orie6125/homework3/socialNetworkFriendAlgorithm/out.txt')#Used for testing
file = sc.textFile('/home/dean/Documents/keithly_dean_orie6125/homework3/socialNetworkFriendAlgorithm/soc-data.txt')
#file.map(str)# operation strips lines of unicode information  https://stackoverflow.com/questions/34479444/how-to-remove-unicode-when-reading-data
lines = file.map(lambda file: str(file).split("\n"))#split file into subcomponents by line
lines = lines.filter(lambda lines: not lines[0].split("\t")[1] == '')#Filter out lines where friends = ''
people = lines.map(lambda lines: (int(lines[0].split("\t")[0]), map(int,lines[0].split("\t")[1].split(","))))#split each line into (person, friends)
people1 = lines.map(lambda lines: int(lines[0].split("\t")[0]))# each person
bVar1 = sc.broadcast(people1.collect())#list of people to broadcast, person
people2 = lines.map(lambda lines: map(int, lines[0].split("\t")[1].split(",")))# returns list of ints of friends
bVar2 = sc.broadcast(people2.collect())#list of friends to broadcast, friends
peopleExp = people.flatMap(lambda people: [(people[0], item) for item in people[1]])#creates a list of tuples ordered (person, friend)

#Now we do replacement of freind in -> peopleExp (person,friend)
peopleToCount = peopleExp.map(lambda ppl: (ppl[0], bVar2.value[bVar1.value.index(ppl[1])]))# A list of tuples ordered (person, [friendS of friend])
# Now need to flatMap peopleToCount so of form (person, friend of friend)
peopleToCountFM = peopleToCount.flatMap(lambda ppl1: [(ppl1[0], item) for item in ppl1[1]])#creates a list of tuples ordered (person, friend of friend)
# Filter: Remove all (friend of friend) who is also friend
peopleToCountFM = peopleToCountFM.filter(lambda pFOF: not pFOF[1] in bVar2.value[bVar1.value[pFOF[0]]])
goupCountedPPL = peopleToCountFM.countByValue(lambda pFOF: (pFOF[0],pFOF[1])).items()


#tmp4 = peopleToCount.collect()


# Need to add some 

################################################################################################################################
#TO RUN
# Use spark-submit to run your application # https://spark.apache.org/docs/1.0.2/quick-start.html
#$ YOUR_SPARK_HOME/bin/spark-submit --master local[4] SimpleApp.py
