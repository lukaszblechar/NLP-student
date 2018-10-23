#08/03/2017
#with recurssive function
def heron_R(n, guess=1):
    if abs((guess*guess)-n)<0.000001:
        return guess
    else:
        guess=((guess+(n/guess))/2)
        return heron_R(n,guess)

#iterative style
def heron_I(n):
    guess=1
    while abs((guess*guess)-n)>0.000001:
        guess =(guess+(n/guess))/2
    return guess
          
#OVERWHELMING COMPUTING POWERRRRR
def sqDroot(n,minV=0,maxV=n,guess=1):
    if abs((guess*guess)-n)<0.000001:
        return guess
    else guess=(m




def sqDroot(n):
    minV=0
    maxV=n
    guess=1
    while abs((guess*guess)-n)>0.000001:
        if (guess*guess)>n:
                maxV=guess
                guess=(minV+maxV)/2
        else:
                minV=guess
                guess=(minV+maxV)/2
            
        return guess
