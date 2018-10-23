def clean (my_string):
    result = ""
    for x in my_string:
        if x not in "0123456789.,:;\"\'\\/[]()?!":
            result= result+x
    return result.split()

def gospel_n_grams(n,gospel):
    gospel_file=open(gospel, "r")
    gospel_test=gospel_file.read()
    gospel_file.close()
    gospel_list=clean(gospel_test)
    return [gospel_list[l:l+n] for l in range (len(gospel_list)-n+1)]
