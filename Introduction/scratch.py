#a= 2 + 2
#print (a)
#X=1

#def f(x):
#    return x+5 

#a=[1,2,3]
#b=a
#id (b)
#id (a)

#imperative approach

def frac(a,b):
    return [a,b]

def num (a):
    return a[0]

def denum (a):
    return a[1]

def timesz(a,b):
    n=num(a)*num(b)
    d=denum(a)*denum(b)
    return frac(n,d)

def plusz (a,b):
    n=(num(a)*denum(b))+(denum(a)*num(b))
    d=(denum(a)*denum(b))
    return frac(n,d)
                
#print(plusz(frac(1,2),frac(1,3)))

def negsz (a):
    return frac(-num(a), denum(a))

def minusz (a,b):
    return plusz(a, negsz(b))

print(minusz(frac(1,2),frac(1,3)))

import turtle
t=turtle.Pen()
for x in range(100):
    t.forward(x)
    t.right(91)

#object-oriented approach
class Fraction:
    def __init__(self,a,b):
        self.num=a
        self.denum=b
    def display (self):
        print (self.num,"/",self.denum)

def pluszOb(a,b):
    n=(a.num*b.denum)+(a.denum*b.num)
    d=(a.denum*b.denum)
    return Fraction(n,d)

ex=pluszOb(Fraction(2,3),Fraction(3,2))
print(ex)
ex.display()


#08/03/2017
def heron_R(n, guess=1):
    if abs((guess*guess)-n)<0.000001:
        return guess
    else:
        guess=((guess*(n/guess))/2)
        return heron_R(n,guess)
