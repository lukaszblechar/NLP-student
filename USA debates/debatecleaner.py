import re 

def clean(debate):
    cleaned = open('New_Version_of'+debate,'w', encoding='utf-8')
    cleaned.write('New Version of Debates \n\n')
    
    with open(debate, 'r', encoding='utf-8') as deb:
        deb = deb.readlines()
        for line in deb:
            line = re.sub('\n','',line)
            line=line.strip()
            if line:
                newLine=''
                if re.match('\A[A-Z]{3}', line):
                    newLine+='\n' + line + ' '
                else:
                    newLine+=line + ' '
                cleaned.write(newLine)
    cleaned.close()
                            
debates = ['debate1.txt', 'debate2.txt', 'debate3.txt', 'debate4.txt', 'debate5.txt']

def cleanDebates():
    debatesNew=[]
    for debate in debates:
        clean(debate)
        debatesNew.append('New_Version_of'+debate)
    return debatesNew

"""def newDebates():
    debates = ['debate1.txt', 'debate2.txt', 'debate3.txt', 'debate4.txt', 'debate5.txt']            
    cleanDebates(debates)
"""

def analysis():
    debatesNew=cleanDebates()
    candidates=['CRUZ:','KASICH:','RUBIO:', 'TRUMP:','BUSH:','CARSON:', 'CHRISTIE:']
    candidateDict={}
    for candidate in candidates:
        candidateDict[candidate]=0
    for debate in debatesNew:
        debateDict = {}
        debi = open(debate, 'r', encoding='utf-8')
        deb = debi.readlines()
        debi.close()
        for candidate in candidates:
            counter = 0
            for line in deb:
                if line.startswith(candidate):
                    result1 = len(re.findall('\[applause\]',line))
                    result2 = len(re.findall('\[laughter\]',line))
                    result3 = len(re.findall('\[applause.+?\]|\[laughter.+?\]',\
                                             line))
                    counter += result1
            debateDict[candidate]=counter
            
        debatesList = debateDict.items()
        debatesList=[(v,k) for k,v in debatesList]
        debatesList=sorted(debatesList)
        debatesList=debatesList[::-1]

        print('\n\n',debate[14:-4].upper(),'\n\n')
        for pop, cand in debatesList:
            candidateDict[cand]+=pop
            print('{:25} {:10}'.format(cand,pop))
            
    print('\n\n+RESUME+\n\n')
    resume = candidateDict.items()
    resume = [(v,k) for k,v in resume]
    resume = sorted(resume)
    resume = resume[::-1]
    for pop,cand in resume:
        print('{:25} {:10}'.format(cand,pop))

"""
def perDebate(n):
    debatesNew = cleanDebates()
    dictofDict={}
    for cand in candidates:
        canDD = candDebate(cand, debatesNew)
        dictOfDict[cand]=candDD
    count=1
    for debate in debatesNew:
        print('\n\n\tDebate {:5}{:20}'.format(count,debate))
    for cand1 in candidates:
        for cand2 in candidates:
            if cand1 != cand2:
                text1= dictofDict[cand1]
                text2 = dictofDict[cand2]
                text1 = text1[count]
                text2 = text2[count]

"""
