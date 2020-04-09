import random
import math

class RSA:

  def GenerateKeys(s1,s2):
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    #remove spaces
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    #convert from 26 to 10
    p = 0
    for i in s1:
      value = alphabet.find(i)
      p *= 26
      p += value
    q = 0
    for i in s2:
      value = alphabet.find(i)
      q *= 26
      q += value
  
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

    #make the keys
    n = p*q
    r = (p -1)*(q-1)
    e = random.randint(1*pow(10,398),2*pow(10,398))
    while not relativeprime(r,e):
      e += 1
    d = findModInverse(e,r)

    #public key
    public = open("public.txt","w")
    public.write(str(n) + '\n')
    public.write(str(e) + '\n')
    public.close()

    #private key
    private = open("private.txt","w")
    private.write(str(n) + "\n")
    private.write(str(d) + "\n")
    private.close()
    return
##################################################################
  def Encrypt(infile,outfile):
    #70 base alphabet
    alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    #open file to be encrypted
    fin = open(infile,"rb")
    fileBinary = fin.read()
    text = fileBinary.decode("utf-8")
    fin.close()

    #get keys to encrypt 
    fin = open('public.txt',"rb")
    Keys = fin.readlines()
    fin.close()

    #seperate into keys
    n = int(Keys[0])
    e = int(Keys[1])

    #convert from 70 to 10
    BigBlock = []
    #200 is size of text block
    while len(text) >= 200:
      c = 0
      newBlock = text[:200]
      for i in newBlock:
        value = alphabet.find(i)
        c *= 70
        c += value
      BigBlock.append(c)
      text = text[200:]

    #last block
    c = 0
    for i in text:
      value = alphabet.find(i)
      c *= 70
      c += value
    BigBlock.append(c)

    #encrypt
    message = ""
    for i in BigBlock:
      num = pow(i,e,n)
      result = ""
      if num == 0:
        result = alphabet[0]
      while num != 0:
        result = alphabet[num % 70] + result
        num = num // 70
      if result == "":
        result = "0"
      result += "$"
      message += result

    fin = open(outfile,"wb")
    fin.write(message.encode("utf-8"))
    fin.close()
    return

##################################################################
  def Decrypt(infile,outfile):
    #set alphabet
    alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    #get text
    fin = open(infile,"rb")
    fileBinary = fin.read()
    text = fileBinary.decode("utf-8")
    fin.close()

    #get keys
    fin = open('private.txt',"rb")
    Keys = fin.readlines()
    fin.close()
    n = int(Keys[0])
    d = int(Keys[1])

    textblocks = text.split('$')
    message = ""
    
    for i in textblocks:
      num = 0
      for number in i:
        value = alphabet.find(number)
        num *= 70
        num += value

      key = pow(num,d,n)
      result = ""
      if key == 0:
        result = alphabet[0]
      while key != 0:
        result = alphabet[key % 70] + result
        key = key // 70
      if result == "":
        result = "0"
      message += result

    fin = open(outfile,"wb")
    fin.write(message.encode("utf-8"))
    fin.close()
    return
########################################################################
def main():
  RSA()
  #this will make a new key every time to avoid that make a key then all future uses of this comment out the generate keys line 
  RSA.GenerateKeys("15924533657845645326547896565478954212291232125997463265214276172791575553211458974563264573724576724377584723754646728352545764849758652432421342714576746745","1592453365784569532654789656547895421229123212599746346553211458974563234573724576724377584714567427364619758345645123774646728352545764849758612432421342714576746745")
  RSA.Encrypt("testfile.txt","encrptedtestfile.txt")
  RSA.Decrypt("encrptedtestfile.txt","decreptedtestfile.txt")

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
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
#####################################################################
def egcd(a, b):
    lastR, r = abs(a), abs(b)
    x, lastX, y, lastY = 0, 1, 1, 0
    while r:
        lastR, (quotient, r) = r, divmod(lastR, r)
        x, lastX = lastX - quotient * x, x
        y, lastY = lastY - quotient * y, y
    return lastR, lastX * (-1 if a < 0 else 1), lastY * (-1 if b < 0 else 1)
#############################################################################

main()
