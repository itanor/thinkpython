"""
Write a function named right_justify that takes a string named s as a parameter and prints the 
string with enough space so that the last letter of the string is in column 70 of the display.

right_justify('allen')
                                                                     allen
"""

def right_justify(columns, s):
  for i in range(columns):
    print(' ', end='')
  print(s)

right_justify(70, 'allen')

