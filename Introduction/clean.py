def clean (my_string):
    result = ""
    for x in my_string:
        if x not in "0123456789.,:;\"\'\\/[]()?!":
            result= result+x
    return result.split()

    
