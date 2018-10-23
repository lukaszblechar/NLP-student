def apply_f(list_f,arg):
    result=arg
    for f in list_f:
        result=f(result)
    return result

def add_level(list_list_f, list_f):
    return [x+[f] for x in list_list_f for f in list_f]

def increment (arg):
    return arg+1
def square (arg):
    return arg*arg

def mixed_solution(initial, final, list_list_f=[[]]):
    list_list_f=add_level(list_list_f,[increment,square])
    for seq in list_list_f:
        if apply_f (seq, initial)==final:
            return seq
    return mixed_solution(initial, final, list_list_f)
