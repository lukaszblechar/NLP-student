import re

def intersection(lst1,lst2):
    return [x for x in lst1 if x in lst2]

def cleanStr(s,cand):
    text=s.replace(cand,"")
    text=re.sub("\[.*?\]","",text)
    text=text.lower()
    text=re.findall("\w+",text)
    return text

def nGrams(listN,n):
    l=len(listN)
    resultlist=[]
    for x in range(l-n+1):
        resultlist.append(listN[x:x+n])
    return resultlist

def clean(debate):
    cleaned = open("new_version_of_"+debate,'w',encoding="utf-8")
    cleaned.write("New Version of Debate\n\n")

    deb = open(debate,'r',encoding="utf-8")
    debLines = deb.readlines()
    for line in debLines:
        line = re.sub('\n'," ",line)
        line = line.strip()
        if line:
            newLine = ""
            if re.match("\A[A-Z]{3}",line):
                newLine += '\n'+line+" " 
            else:
                newLine+= line+" "
            cleaned.write(newLine)
    deb.close()
    cleaned.close()

def cleanDebates(debates):
    newDebates = []
    for debate in debates:
        clean(debate)
        newDebates.append("new_version_of_"+debate)
    return newDebates

def makeNewDebates():
    debates = ["debate1.txt","debate2.txt","debate3.txt","debate4.txt","debate5.txt"]
    result=cleanDebates(debates)
    return result

def candDebate(cand,debates):
    counter=1
    candDD={}
    for debate in debates:
        res=""
        with open(debate,encoding="utf-8") as deb:
            deb=deb.readlines()
            for line in deb:
                if line.startswith(cand):
                    res+=line+" "
        res=cleanStr(res,cand)
        candDD[counter]=res
        counter+=1
    return candDD

def analPerDebate(n):
    newDebates=makeNewDebates()
    candidates=["CRUZ","KASICH","RUBIO","TRUMP","BUSH","CARSON","CHRISTIE"]
    dictOfDicts={}
    for cand in candidates:
        candDD=candDebate(cand,newDebates)
        dictOfDicts[cand]=candDD
    counter=1
    for debate in newDebates:
        print("\n\n\tDEBATE {} {:25}".format(counter,debate))
        for cand1 in candidates:
            for cand2 in candidates:
                if cand1 != cand2:
                    text1=dictOfDicts[cand1]
                    text2=dictOfDicts[cand2]
                    text1=text1[counter]
                    text2=text2[counter]
                    result1=nGrams(text1,n)
                    result2=nGrams(text2,n)
                    share=intersection(result1,result2)
                    if len(result1)>0:
                        print("{:10}{:10} similarity: {:6.3%}".format(cand1,cand2,len(share)/len(result1)))
        counter+=1
