def delete_consonents(mystring):
    consonents = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    mystringWithoutConsonents = ""
    for eachChar in s:
        if eachChar not in Consonents:
            mystringWithoutConsonents = mystringWithoutConsonents + eachChar
    return mystringWithoutConsonents

print(removeConsonents("compsci"))
print(removeConsonents("aAbEefIijOopUus"))
