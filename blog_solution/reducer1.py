import fileinput
import re

def cleanInputArr(data):
     out = []
     for s in data:
          out.append(s.strip())

     return out

def reducer():
     location = ''

     for line in fileinput.input():
          data = re.split(',',line)
          data = cleanInputArr(data)
          key, value = data

          # if key has 'a' at the end -> this is mapper2
          # and we've got {userId,location} tuple
          if key.endswith('a'):
               location = value

          # if key has 'b' at the end -> this is mapper1
          # and we've got {userId,productId} tuple
          if key.endswith('b'):
               print '{0},{1}'.format(value, location)


def main():
    reducer()

main()
