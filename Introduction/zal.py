def cypher(String):
    newList = String.split()
    counter = 0
    first = []
    second = []
    for word in newList:
        newWord = word [::-1]
        if counter % 2 == 0:
            first.append(newWord)
            counter += 1
        else:
            second.append(newWord)
            counter += 1
    ##print(first)
    ##print(second)
    final = first + second
    return ' '.join(final)

def cypher1(String):
    newList = String.split()
    counter = 0
    first = []
    second = []
    for word in newList:
        if counter % 2 == 0:
            first.append(word)
            counter += 1
        else:
            second.append(word)
            counter += 1
    print(first)
    print(second)
    final = first + second
    return ' '.join(final)


def decypher (String1):
    newList1 = String1.split()
    l = len(newList1)
    m = l // 2
    
    if l % 2 == 0:
        first = newList1[:m]
        second = newList1[m:]
    else:
        first = newList1[:m+1]
        second = newList1[m+1:]
    print(first)
    
    print(second)
    f = 0
    s = 0
    final = []
    for n in range(l):
        if n % 2 ==0:
            final.append(first[f])
            f += 1
        else:
            final.append(second[s])
            s += 1
##    for word1 in newList1:
##        if counter1 %2 == 0:
##            first1.append(word1)
##            counter1 += 1
##        else:
##            second1.append(word1)
##            counter2 += 1
##    print(first1)
##    print(second1)
    final = [w[::-1] for w in final]
    return ' '.join(final)
