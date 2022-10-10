from mpmath import *
mp.dps = 10000 # Increase this to compute more digits.
# Note: this will result in code that takes longer to 
# run, so make sure your algorithm works before 
# changing this.
mp.pretty = True

def compute_pi():
  n=1000
  return 9801/(2*sqrt(2)*sum([factorial(4*k)*(1103+26390*k)/((factorial(k)**4)*(396**(4*k))) for k in range(n)]))
    

# SERIOUSLY: DON'T MODIFY ANYTHING BELOW THIS LINE!

def main():
  pi_calc = compute_pi()
  diff = (pi_calc - pi)/pi
  print(pi_calc)
  nprint(int(-log10(abs(diff))), 12)

if __name__ == "__main__":
  main()