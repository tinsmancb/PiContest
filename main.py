from mpmath import *
mp.dps = 100 # Increase this to compute more digits.
# Note: this will result in code that takes longer to 
# run, so make sure your algorithm works before 
# changing this.
mp.pretty = True

def compute_pi():
  # Implement your pi calculation here.
  return 3 # The first digit is free.

# DON'T MODIFY ANYTHING BELOW THIS LINE!

def main():
  pi_calc = compute_pi()
  diff = (pi_calc - pi)/pi
  print(pi_calc)
  nprint(int(-log10(abs(diff))), 12)

if __name__ == "__main__":
  main()