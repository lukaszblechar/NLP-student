def fib_2R(n):
    if n<2:
        return n
    else:
        return fib_2R(n-1)+fib_2R(n-2)

def fib_1R(n, first=0,second=1,counter=1):
    if counter > n:
        return first
    else:
        return fib_1R(n,second,first+second,counter+1)

def fib_itR(n):
    first = 0
    second = 1
    for x in range (n):
        first_help = second
        second= first + second
        first= first_help
    return first

def split_Number (n):
    return n//10, n%10

def sum_Digits(n):
    but_last, last = split_Number(n)
    if n<10:
        return n
    else:
        return sum_Digits(but_last)+last

def valid_card(n):
    but_last, last = split_Number(n)
    if n<10:
        return n
    else:
        return help_card(but_last)+last

def help_card(n):
    but_last, last= split_Number(n)
    digit_Luhn=sum_Digits(2*last)
    if n<10:
        return digit_Luhn
    else:
        return valid_card(but_last)+digit_Luhn

def sum_Digits_I(n):
    n_list= list((str(n)))
    l=len(n_list)
    result=0
    for x in n_list:
        result=result+int(x)
    return result

def valid_Card_I(n):
    n_list=list(str(n))
    l=len(n_list)
    result=0
    if l%2==0:
        for x in range (0,l,2):
            result=result+sum_Digits_I (int (n_list[x])*2)
        for x in range (1,l,2):
            result=result+int(n_list[x])
        return result
    else:
        for x in range (1,l,2):
            result=result+sum_Digits_I (int (n_list[x])*2)
        for x in range (0,l,2):
            result=result+int(n_list[x])
        return result
