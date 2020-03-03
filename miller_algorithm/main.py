#https://cit.dixie.edu/cs/3310/programs/monte_carlo_primality.h
import random

def miller(num,base):
  t = num - 1
  s = 0
  # find n -1 = 2^s * t
  while t % 2 == 0:
    t = t//2
    s += 1
  
  #(base ^ t ) % num
  v = pow(base,t,num)
  if v != 1:
    i = 0
    while v != (num - 1):
      if i == s - 1:
        return False
      else:
        i = i + 1
        v = pow(v,2) % num
  return True

def prime(num,k):
    #if 0 or negative not prime
    if num <= 1:
      return False
    #if exactly 2 is prime special case
    if num == 2:
      return True
    #if dividable by 2 is even and thefore not prime
    if num % 2 == 0:
      return False
    b = random.randint(2,num-1)
    while k >= 0:
      if miller(num,b):
        b = random.randint(2,num-1)
        k -= 1
      else:
        return False
    return True

def main():
  x = 0
  while x < 1000:
    print(str(prime(x,30)) + " " +str(x)) 
    x += 1
  return


main()
