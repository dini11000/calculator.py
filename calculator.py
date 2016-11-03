#!/usr/bin/python -tt

# ./calculator.py 4*3-4+2+2 - 3/2

import sys
import re

def main():
  if len(sys.argv) == 1:
     print "Please pass the numbers to the calulator program. For e.g.: ./calculator.py 4*2-1+3"
  else:
    argueList = sys.argv[1:]
    string = ' '.join(argueList)
    calculate(string)

def calculate(string):
  list = parseString(string)
  # Return list like [ '1', '+', '2', '*', '3' ]
  if len(list) < 3:
    print "Nothing to do.. Hence exiting.."
    sys.exit(1)
  else:
    while len(list) != 1:
      for precedence in range(1,2):
        for start in range(0, len(list), 2):
          result = evaluate(list[start], list[start+1], list[start+2], precedence)
          if result:
            newList1 = list[0:start-1]   # check start-1  >= 0
            newList2 = list[start+2:]
            newList[0] = result
            list = newList[1] + newList[2]
    print "Result is: ", list[0]

def evaluate(number1, operand, number2, precedence):
  precedences = { '*':1, '/': 1, '+': '2', '-': 2 }  
  p = precedences[operand]
  result = ""
  if precedence == p:
     if operand == "+":
        result = str(int(number1) + int(number2))
     elif operand == "-":
        result = str(int(number1) - int(number2))
     elif operand == "*":
        result = str(int(number1) * int(number2))
     elif operand == "/":
        result = str(int(number1) / int(number2))
     else:
        print "undefined operand: " + operand
        sys.exit(1)
  return result

def parseString(string):
  list = []
  while (len(string) > 0):
    result = re.search( '([\d\.]+)(.)', string )
    if result:
      number = result.group(1)
      operand = result.group(2)
      list.append(number)
      list.append(operand)
      string.replace(number+operand, "")
    else:
      break 
  return list
  

if __name__ == '__main__':
  main()
