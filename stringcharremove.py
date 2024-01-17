# token -> abxrho, str -> hello output -> ell -> remove the matched char

def compStr(str1):
    token = "abxrhodu"
    s1 = list(str1)
    i = 0
    newstr = ''
    while(i<len(token)):
        j = 0
        while(j<len(s1)):
            if(token[i] == s1[j]):
                s1.pop(j)
            else:
                j = j+1
        i = i+1
    newstr = ''.join(s1)
    print(newstr)

compStr("debu")