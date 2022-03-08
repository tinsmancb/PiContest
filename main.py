from mpmath import *
mp.dps = 100
mp.pretty = True

def compute_pi():
  return 3

def main():
  pi_calc = compute_pi()
  diff = (pi_calc - pi)/pi
  print(pi_calc)
  nprint(-log10(abs(diff)), 12)

if __name__ == "__main__":
  main()