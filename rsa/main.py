#https://cit.dixie.edu/cs/3310/programs/RSA_Assignment.htm
import random
import math

class RSA:

  def GenerateKeys(s1,s2):
    p = 0 #s1
    q = 0 #s2
    x = 0 #counter
    #convert from 26 to 10
    for i in str(s1):
      p += int(i)*pow(26,x)
      x += 1
    x = 0
    for i in str(s2):
      q += int(i) * pow(26,x)
      x += 1
    #mod
    fixer = pow(10,200)
    if p > fixer:
      p %= fixer
    else:
      print("p was too small")
    if q > fixer:
      q %= fixer
    else:
      print("q was too short" )
    #make odd
    if p % 2 == 0:
      p += 1
    if q % 2 == 0:
      q += 1
    #make prime
    while not prime(p,30):
      p += 2
    while not prime(q,30):
      q += 2
    n = p*q
    r = (p -1)*(q-1)
    e = random.randint(1*pow(10,398),2*pow(10,398))
    while not relativeprime(r,e):
      e += 1
    d = findModInverse(e,r)

    #public key
    public = open("public.txt","w")
    public.writelines([str(n) + "\n",str(e) + "\n"])
    public.close()

    #private key
    private = open("private.txt","w")
    private.writelines([str(n) + "\n",str(d) + "\n"])
    private.close()
    return
##################################################################
  def Encrypt(infile,outfile):
    alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    fin = open(infile,"rb")
    fileBinary = fin.read()
    text = fileBinary.decode("utf-8")
    fin.close()
    #get keys
    fin = open('public.txt',"rb")
    PlainTextBinary = fin.read()
    PlainText = PlainTextBinary.decode("utf-8")
    fin.close()
    PlainText = PlainText.splitlines()
    n = PlainText[0]
    e = PlainText[1]

    x = 0
    p = 0
    holder = 0
    #convert from 70 to 10
    for i in text:
      holder = alphabet.index(i)
      p += int(holder)*pow(70,x)
      x += 1
    #encrypt
    p = pow(int(p),int(e),int(n))

    stringMessage = ""
    res = ""
    #convert from 10 to 70
    while p > 0:
      res += alphabet[pow(int(p),1,70)]
      p = int(p)//70
    stringMessage += str(res)
    fin = open(outfile,"wb")
    fin.write(stringMessage.encode("utf-8"))
    fin.close()
    return

##################################################################
  def Decrypt(infile,outfile):
    #get text
    fin = open(infile,"rb")
    fileBinary = fin.read()
    text = fileBinary.decode("utf-8")
    fin.close()
    alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    #get keys
    fin = open('private.txt',"rb")
    PlainTextBinary = fin.read()
    PlainText = PlainTextBinary.decode("utf-8")
    fin.close()
    PlainText = PlainText.splitlines()
    n = PlainText[0]
    d = PlainText[1]

    x = 0
    p = 0
    holder = 0
    #convert from 70 to 10
    for i in text:
      holder = alphabet.index(i)
      p += int(holder)*pow(70,x)
      x += 1
    p = pow(int(p),int(d),int(n))

    stringMessage = ""
    res = ""
    #convert from 10 to 70
    while p > 0:
      res += alphabet[pow(int(p),1,70)]
      p = int(p)//70
    stringMessage += str(res)
    fin = open(outfile,"wb")
    fin.write(stringMessage.encode("utf-8"))
    fin.close()
    return
########################################################################
def main():
  RSA()
  #RSA.GenerateKeys("1592453365784564532654789656547895421229123212599746326553211458974563264573724576724377584723754646728352545764849758652432421342714576746745","1592453365784569532654789656547895421229123212599746346553211458974563234573724576724377584723774646728352545764849758612432421342714576746745")
  fin = open("testfile.txt","w")
  fin.write("this is a lot of test code you got to test in order to have test code oh wow it seems i have really done it i am a super genius of unparelled genius for being like me oh year i am great oh yea where do you break i kn")
  fin.close()
  RSA.Encrypt("testfile.txt","encrptedtestfile.txt")
  RSA.Decrypt("encrptedtestfile.txt","decreptedtestfile.txt")
  
  fin = open("testfile.txt","r")
  print(fin.read())
  fin.close()

  fin = open("decreptedtestfile.txt","r")
  print(fin.read())
  fin.close()

###################################################################
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
##################################################################
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
####################################################################
def relativeprime(a,b):#finds nearest realtivly prime number of given number
  return math.gcd(a,b) == 1
############################################################################
def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if math.gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
#####################################################################

main()