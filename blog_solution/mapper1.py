#! /bin/python
import sys
import re

################################################
# Please see problem description here: 
# http://beekeeperdata.com/posts/hadoop/2015/12/14/spark-scala-tutorial.html
#
# I did the same but in Python

def cleanInputArr(data):
     out = []
     for s in data:
          out.append(s.strip())

     return out

def mapper():
     with open('input1.txt') as f:
          for line in f:
               data = re.split(',',line)
               data = cleanInputArr(data)

               transactionId, productId, userId, ammount, item = data
               print '{0}b,{1}'.format(userId, productId)

def mapper2():
     with open('input2.txt') as f2:
          for line in f2:
               data = re.split(',',line)
               data = cleanInputArr(data)

               userId, email, lang, location = data
               # Each userId ends in 'a' to make sure
               # that reducer will get this line first
               #
               # Hadoop will automatically partition and sort (by a key)
               # data between 'mapper' -> 'reducer' so we will get this 
               # item first for each userId
               print '{0}a,{1}'.format(userId, location)

def main():
     mapper()

     mapper2()

main()

