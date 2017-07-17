import math

def double_print(param):
  print(param)
  print(param)

def print_n_times(times, param):
  for i in range(times):
    print(param)

double_print('abracadabra')
double_print(19)
double_print('Spam ' * 4)
double_print(math.cos(math.pi))

print_n_times(3, 'xpto')
print_n_times(4, 'Spam ' * 4)

