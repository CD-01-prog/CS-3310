def main():
  a = 4
  usernum = int(input("what is your number between 1-9:"))
  lex = list(range(1,a + 1))
  count = 0
  print(lex)
  while usernum > count:
    lexPgen(a,lex)
    count += 1
  print("and thats all folks")

def lexPgen(length,lex):
  n = length
  j = n - 2
  while lex[j] > lex[j + 1]:
    j = j - 1

  k = n - 1
  while lex[j] > lex[k]:
    k = k - 1
  lex[j],lex[k] = lex[k],lex[j]
  r = n -1
  s = j + 1
  while r > s:
    lex[r], lex[s] = lex[s], lex[r]
    s = s + 1
    r -= 1
  print(lex)
  return;

main()
