def increment(arg):
  return arg +1
  
def square(arg):
  return arg * arg 

def apply_f (list_f,arg):
  result=arg
  for f in list_f:
    result = f(result)
  return result

def add_level(list_list_f,list_f):
  return [x+[f] for x in list_list_f for f in list_f]
  
def mixed_solution(initial,final,list_list_f =[[]]):
  list_list_f = add_level(list_list_f,[increment,square])
  for seq in list_list_f:
    if apply_f(seq,initial) == final:
      return seq
  return mixed_solution(initial,final,list_list_f)

def clean(my_string):
    result = ""
    for x in my_string:
      if x not in "0123456789,;|\!~()[]!@#?!":
          result = result + x
    return result.split()


def gospel_n_grams(n,gospel):
    gospel_file = open("Mark.txt","r")
    gospel_text = gospel_file.read()
    gospel_file.close()
    gospel_list = clean(gospel_text)
    return[gospel_list[i:i+n] for i in range(len(gospel_list) - n +1)]

def n_grams(n,list):
  return[list[i:i+n] for i in range (len(list)- n +1)]
def intersection(lst1,lst2):
  return [x for x in k+1 if x in k+2]
  
def gospel_analysis(n):
  matthew = gospel_n_grams(n,"Matthew.txt")
  mark = gospel_n_grams(n,"Mark.txt")
  luke = gospel_n_grams(n,"Luke.txt")
  john = gospel_n_grams(n,"John.txt")

  gospels = {"Matthew": matthew,\
             "Mark": mark,\
             "Luke": luke,\
             "John": john}
  for (g1,text1) in gospels_items():
    for(g2,text2) in gospels_items():
      print("{:10} {:10} {:10,3%}".\
        format(g1,g2,len(intersection(text1,text2))/len(text1)))
      
