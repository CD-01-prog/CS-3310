import math

def main():
    answer_nums = input("Enter number of elements... " )
    answer_perms = int(answer_nums)
    n = int(answer_nums)
    r = n
    lex = []
    for i in range(n):
      lex.append(i+1)

    total_perm = math.factorial(n)/(math.factorial(n-r))
    t = int(answer_perms) - 1

    print("")
    print(lex)
    print("")
    print( "Total number of permutations:", total_perm)
    lex.sort()
    print()
    print( lex, "   # 1")
    for i in range(int(t)):
        lex = lexPgen(n,total_perm,lex)
        print( lex, "   #", i + 2)

    print("")

def lexPgen(n, r, lex):
    j = n - 1
    i = n - 2

    #swap sett[j] and sett[j-1] if sett[j] is bigger
    if lex[i] < lex[j]:
        lex[i], lex[j] = lex[j], lex[i]
        return lex

    while lex[i] > lex[j]:
        #move down to next index and compare
        j -= 1
        i -= 1

        #if it reaches end of list, return
        if i < 0:
            return lex

    # this is the pivot
    k = lex[i]

    new_sett = lex[i+1:]

    #sort the 2nd list
    new_sett.sort()

    #initilize to false
    result = False

    #find the next biggest and set to true if one is found
    for item in new_sett:
        if item > k:
            result = True
            break

    if result == True:
        p = 0
        for m in lex[i:]:
            if m == item:
                break
            p += 1

        #swap the pivot with the item
        lex[i], lex[i+p] = lex[i+p], lex[i]

        #set the set to the rest of the list and then add the item to the end
        s = lex[i+1:]
        s.sort()

        lex = lex[:i+1]
        for c in s:
            lex.append(c)
        return lex

    # else return the set
    return lex

main()
