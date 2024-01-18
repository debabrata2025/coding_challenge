#reverse string and token interparse challenge
# debu -> ubed -> token = "axbc3tc" -> interparse
#  interparse -> uabxebdc

def reverse_str(str1):
    s2 = str1[::-1]
    token = "ax"
    finalstr = ""
    i = 0

    if len(s2) < len(token): #reverse str is smaller than token
            while(i<len(s2)):
                finalstr += s2[i]+token[i]
                i += 1
                j = len(s2)  #dutor interparse result
            while(j<len(token)): #dutor interparse result + #remaining of token
                finalstr += token[j]
                j += 1
    elif len(s2) > len(token): #reverse str is greater than token
        k = 0
        while(k<len(token)):
            finalstr += s2[k]+token[k]
            k += 1
        l = len(token)
        while(l<len(s2)):
            finalstr += s2[l];
            l += 1
    else:                     #reverse str is equal size of token
        m = 0
        while (m < len(s2)):
            finalstr += s2[m] + token[m]
            m += 1

    print(s2)
    print(token)
    print(finalstr)


reverse_str("de")