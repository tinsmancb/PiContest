from mpmath import *
mp.dps = 100 # Increase this to compute more digits.
# Note: this will result in code that takes longer to 
# run, so make sure your algorithm works before 
# changing this.
mp.pretty = True

def compute_pi():
  acc = 0
  for n in range(int(1e7)):
    acc += ((-1)**n)/(2*n+1)

  return 4*acc
    

# DON'T MODIFY ANYTHING BELOW THIS LINE!

def main():
  pi_calc = compute_pi()
  diff = (pi_calc - pi)/pi
  print(pi_calc)
  nprint(int(-log10(abs(diff))), 12)

if __name__ == "__main__":
  main()