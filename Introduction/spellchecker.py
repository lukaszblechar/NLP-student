import re

def convertWord (word):
    res = ''
    for x in word:
        if x == 'ą':
            res += 'a'
        if x == 'ę':
            res += 'e'
        if x == 'ł':
            res += 'l'
        if x == 'ź':
            res += 'z'
        if x == 'ó':
            res += 'o'
        if x == 'ś':
            res += 's'
        if x == 'ż':
            res += 'z'
        else:
            res += x
    return res

def spellchecker(name):
    with open('/etc/passwd','r') as passwd:
        password =passwd.readlines()
        
