def check_fermat(a, b, c, n):
  a_at_n = pow(a, n)
  b_at_n = pow(b, n)
  c_at_n = pow(c, n)

  if n > 2 and (a_at_n + b_at_n == c_at_n):
    print("Holy smokes, Fermat was wrong!")
  else:
    print("No, that doesn't work.")

a = int(input("input for a:\n"))
b = int(input("input for b:\n"))
c = int(input("input for c:\n"))
n = int(input("input for n:\n"))

check_fermat(a, b, c, n)
