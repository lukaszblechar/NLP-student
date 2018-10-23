#################################################################
#################################################################
#################################################################


def clean_string(my_string):
    result = ""
    for x in my_string:
      if x not in "0123456789,:;|\/\'\"!~()[]!@#?!":
          result = result + x
    return result.lower().split()

def gospel_list_text(gospel):

    file = open(gospel,'r')
    string = file.read()
    file.close()
    lst = clean_string(string)
    return lst
   

def gospel_dicti(gospel):
   
    lst = gospel_list_text(gospel)
    dicti = []
    for x in lst:
        if x not in dicti:
            dicti.append(x)
    return dicti




def gospel_words(gospel):
   
   
    wording = {}
    dictionary = gospel_dicti(gospel)
    text = gospel_list_text(gospel)
    for w1 in dictionary:
        counter = 0
        for w2 in text:
            if w1 == w2:
                counter += 1
        wording[w1] = counter
    return wording


def gospel_ngrams(gospel,n):
    gospel_list = gospel_list_text(gospel)
    return[gospel_list[i:i+n] for i in range(len(gospel_list) - n +1)]

class Gospel:
    def __init__(self,name):
        self.name = name
        self.dictionary = gospel_dicti(name+".txt")
        self.grams3 = gospel_ngrams(name+".txt",3)
        self.grams5 = gospel_ngrams(name+".txt",5)
        self.wording = gospel_words(name+".txt")
        self.text = gospel_list_text(name+".txt")

def wording_sorted(words_freq):
    wording_s = []
    for (w,n) in words_freq:
        el = (n,w)
        wording_s.append(el)
    return sorted(wording_s)
   

def word_grams(word,gospel_grams):
    gram_list = []
    for gram in  gospel_grams:
        if word in gram:
            gram_list = gram_list + [gram]
    return gram_list

def neigh(gram_list,dicti):
    neighbour = {}
    for w in dicti:
        counter = 0
        for gram in gram_list:
            if w in gram:
                counter += 1
        neighbour[w] = counter
    return neighbour
   
##    for w in dicti:
##        counter = 0
##        if w != word:
##            for gram in grammy:
##                if word in grammy:
##                    if w in grammy:
##                        counter += 1
##            neighb[w] = counter
##    return neighb
