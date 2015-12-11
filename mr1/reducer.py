import sys

def reducer():
     salesTotal = 0
     oldKey = None

     for line in sys.stdin:
         data = line.strip().split("\t")
         if len(data) != 2:
              # Something has gone wrong. Skip this line.
              continue

         thisKey, thisSale = data

         if oldKey and (oldKey != thisKey):
              print oldKey, "\t", salesTotal
              salesTotal = 0

         oldKey = thisKey
         salesTotal += float(thisSale)

     if oldKey != None:
          print oldKey, "\t", salesTotal

test_text = """Miamy\t99.95
New York\t9.50
New York\t1.25"""

def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)

	reducer()

	sys.stdin = sys.__stdin__

main()
