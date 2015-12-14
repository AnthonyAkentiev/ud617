import sys

def reducer():
     salesTotal = 0
     oldKey = None

     result = ""
     first = True

     for line in sys.stdin:
          data = line.strip().split("\t")
          if len(data) != 2:
               # Something has gone wrong. Skip this line.
               continue

          word, index = data

          result = result + index
          result = result + " "

     print result

# Already sorted values
test_text = """Word1\t12345
Word1\t950
Word1\t125"""

def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	reducer()
	sys.stdin = sys.__stdin__

main()
