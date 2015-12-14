import sys
import re
import csv

def processWord(w,l,ids):
     count = 0
     data = re.split("[/. ,;!?:\"()<>#$=-]+",w)
     for s in data:
          if s.lower()=="fantastically":
               count = count + 1
               print "Found ", ";id: ",l[0]
               ids.append(l[0])

     return count

def processLine(l,ids):
     count = 0
     for w in l:
          count = count + processWord(w,l,ids)

     return count

def main():
     if len(sys.argv)!=2:
          print "Please pass filename"
          sys.exit(-1)
          return

     inputFile = sys.argv[1]
     f = open(inputFile)
     reader = csv.reader(f, delimiter='\t')

     ids = []

     totalCount = 0
     for line in reader:
          totalCount = totalCount + processLine(line,ids)

     print "Total count: ", totalCount
     print "Ids count: ", len(ids)

     top_n = sorted(ids, key=lambda a: int(a))[0:9]
     print "Top: ", top_n


if __name__ == "__main__":
     main()
