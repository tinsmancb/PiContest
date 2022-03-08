from mpmath import *
mp.dps = 100000
mp.pretty = True

def rama(n):
  return 9801/(2*sqrt(2)*sum([factorial(4*k)*(1103+26390*k)/((factorial(k)**4)*(396**(4*k))) for k in range(n)]))

def main():
  pi_calc = rama(15000)
  diff = (pi_calc - pi)/pi
  print(pi_calc)
  nprint(-log10(diff), 12)

if __name__ == "__main__":
  main()