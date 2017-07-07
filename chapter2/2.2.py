def show_value_and_type(value, type_of):
  print('type of ' + value + ' is: ' + type_of)

width = 17
height = 12.0
delimiter = '.'

w1 = width / 2
show_value_and_type(str(w1), str(type(w1)))

w2 = width / 2.0
show_value_and_type(str(w2), str(type(w2)))

h1 = height / 3
show_value_and_type(str(h1), str(type(h1)))

# PEMDAS: Parentheses, Exponentiation, Multiplication and Division, Addition and Subtraction
precedence = 1 + 2 * 5
show_value_and_type(str(precedence), str(type(precedence)))

points = delimiter * 5
show_value_and_type(points, str(type(points)))

