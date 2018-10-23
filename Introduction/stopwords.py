def getGlue():
    openFile = open('stopwords.txt','r')
    readFile = openFile.read()
    openFile.close()
    glue=readFile.split(',')
    return glue

def cleanWord(my_string):
    result = ""
    
    for x in my_string:
      if x == '-':
          result+=' '
      if x == '\n':
          result+=' '
      if x not in '"0123456789,;|\!~()[].-!@#?!':
          result += x
    return result.strip()

def checkList(aList):
    result=[]
    for x in aList:
        
        if ' ' in x:
            newEl=x.split()
            result += newEl
        else:
            if x != '':
                result+=[x]
    return result

def getText(filename):
    openFile = open(filename,'r')
    readFile = openFile.read().lower()
    openFile.close()
    text=readFile.split(' ')
    text= list(map(cleanWord,text))
    text= checkList(text)
    return text

def stopwordsFile(filename):
    file=getText(filename)
    glue=getGlue()
    fileDict={}
    for x_glue in glue:
        freq=0
        for word in file:
            if word ==x_glue:
                freq+=1
            fileDict[x_glue]=freq/len(file)
    aList=[]
    for x_glue in glue:
        aList += [fileDict[x_glue]]
    return aList
    


        

