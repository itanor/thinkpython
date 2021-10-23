"""
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Hint: to print more than one value on a line, you can print a comma-separated sequence:

print '+','-'

If the sequence ends with a comma, Python leaves the line unfinished, so the value printed
next appears on the same line.

print '+',
print '-'

The output of these statements is '+ -'.
A print statement all by itself ends the current line and goes to the next line.

2. Write a function that draws a similar grid with four rows and four columns.
"""

def horizontal(size):
  print('+', end='')
  for i in range(size):
    print(' - - - - ', end='')
    print('+', end='')
  print('')

def vertical(size):
  for i in range(size):
    print('|         ', end='')
  print('|')

def print_block(times):
  for i in range(times):
    for i in range(4):
      vertical(times)
    horizontal(times)

def grid_with_size(size):
  horizontal(size)
  print_block(size)

### 1
grid_with_size(2)

print('')

### 2
grid_with_size(4)

grid_with_size(8)
