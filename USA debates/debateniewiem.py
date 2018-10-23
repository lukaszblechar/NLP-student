import re

candidates = ['CRUZ:', 'KASICH:','RUBIO:', 'TRUMP:','BUSH:','CARSON:', 'CHRISTIE:']
debates = ['debate1.txt', 'debate2.txt', 'debate3.txt', 'debate4.txt', 'debate5.txt']
    
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


def candDebate(cand, debatesNew):
    counter = 1
    candDD={}
    for debate in debatesNew:
        res = ''
        with open(debate,'r',encoding='utf-8') as deb:
            deb = deb.readlines()
            for line in deb:
                if line.startswith(cand):
                    res += line + ''
        candDD[counter] = res
        counter += 1
    return candDD

"def n_grams(n,list):"
" return[list[i:i+n] for i in range (len(list)- n +1)]"
def intersection(lst1,lst2):
  return [x for x in lst1 if x in lst2]

def n_grams(n, text):
    return [text[i:i+n] for i in range(len(text)-n+1)]

def cleanCandText (string, cand):
    text = string.replace(cand,'')
    text = re.sub('\[.*?\]', '', text)
    text = text.lower()
    text = re.findall('\w+', text)
    return text
    

def perDebate(n):
    debatesNew = cleanDebates()
    dictOfDict={}
    for cand in candidates:
        candDD = candDebate(cand, debatesNew)
        dictOfDict[cand]=candDD
    count=1
    for debate in debatesNew:
        print('\n\n\tDebate {:5}{:20}'.format(count,debate))
        for cand1 in candidates:
            for cand2 in candidates:
                if cand1 != cand2:
                    text1= dictOfDict[cand1]
                    text2 = dictOfDict[cand2]
                    text1 = text1[count]
                    text2 = text2[count]
                    list1= cleanCandText(text1,cand1)
                    list2= cleanCandText(text2,cand2)
                    result1=n_grams(n,list1)
                    result2=n_grams(n,list2)
                    share=intersection(result1,result2)
                    print('{:10} {:10} {:12} {:6.3%}'.format(cand1,cand2,'similarity',len(share)/len(result1)))
                          
        count +=1
