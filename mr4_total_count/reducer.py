import sys

def reducer():
     salesTotal = 0
     oldKey = None

     for line in sys.stdin:
          data = line.strip().split("\t")
          if len(data) != 2:
               # Something has gone wrong. Skip this line.
               continue

          word, index = data

          # TODO

test_text = """Word1\t12345
Word2\t950
Word3\t125"""

def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)

	reducer()

	sys.stdin = sys.__stdin__

main()
