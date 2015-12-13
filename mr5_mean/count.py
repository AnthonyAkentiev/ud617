import sys
import csv
from datetime import datetime

# We filter items (see description above)
def mapper():
     for line in sys.stdin:
          data = line.strip().split("\t")

          if len(data)!= 6:
               continue

          date, time, store, item, cost, method = data

          weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
          print weekday 


# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    mapper()

if __name__ == "__main__":
    main()

