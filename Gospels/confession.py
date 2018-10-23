import re

def lust (con):
    analysis = re.findall ('slept (.+?\.)',con)
    count = 0
    for x in analysis:
        if 'girl' in x: count += 1
        if 'boy' in x: count += 1
        if 'friend' in x: count += 1
        if 'colleague' in x: count += 1

    porn = re.findall('porn|peep|peek',con)

    return count+len(porn)

def laziness(con):
    analysis = re.findall ('slept .+?\.',con)
    count = 0
    for x in analysis:
        if lust(x) == 0: count += 1

    rest = re.findall('lazy|rest',con)
    return count+len(rest)
def gluttony (con):

    analysis1 = re.findall('eat|ate', con)
    analysis2 = re.findall('eat|ate', con)

    return len(analysis1+analysis2)

def confession():
    
    print ('Examine your conscience')
    print ("NOW PLEASE TELL ME WHAT HAVE YOU DONE MY CHILD")
    confess = input('>>> ')
    con = confess.lower()
    count = 0
    sins = []
    if lust (con) > 0: sins.append('LUST')
    if laziness (con) > 0: sins.append('LAZINESS')
    if gluttony (con) > 0: sins.append('GLUTTONY')
    count = lust(con) +\
            laziness(con) +\
            gluttony(con)
    if count !=0:
        print ("Your sins are:")
        for x in sins:
            print (x, ' ', end='')
        
 
    
        print ('Father forgive them they do not know what they are doing')
        print ('Though your sins be like scarlet they shall become white as snow Though they be red like crimson they shall become white as wool')
        print ("PLEASE SAY THE LORD'S PRAYER {} TIMES".format (count))
        print ('your sins are forgiven go home and trespass no more')
    else:
        print('\nYour sin is pride....\n')

    
