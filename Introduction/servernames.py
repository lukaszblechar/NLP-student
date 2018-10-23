myS='Both your emails do not work. I mean maarten.wolski@gmail.com.!.!?!?#., which gives an error 0127 and marcin.wolski@umcs.lublin.pl.'
import re

def dropEnd(String):
    result = String
    for x in '.,!@#?:':
        while String.endswith(x):
            result=String[:-1]
            String = result
    return result

def findServer(String):
    result=[]
    while '@' in String:
        begin = String.find('@')
        middle = String [begin+1: ]
        end = middle.find(' ')
        if end >0:
            result.append(middle[:end])
            String=middle
        else:
            result.append(middle)
            String=middle
    return [dropEnd(x) for x in result]


def reSerwer (string):
    return [re.sub('(\W+)$','', x) for x in re.findall('\S+?@(\S+)',string)]

                   
