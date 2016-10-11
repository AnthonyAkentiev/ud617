import fileinput
import re

def cleanInputArr(data):
     out = []
     for s in data:
          out.append(s.strip())

     return out

def reducer():
     arr = []
     for line in fileinput.input():
          data = re.split(',',line)
          data = cleanInputArr(data)
          productId, location = data

          item = [productId, location]
          arr.append(item)

     # TODO: 
     arr = sorted(arr, key=lambda a: a[0])

     print arr

def main():
    reducer()

main()
