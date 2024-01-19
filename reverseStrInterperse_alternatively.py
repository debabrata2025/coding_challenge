#reverse string interperse

def reverseStrInterperse(str1):
    token = "DEBU"
    rev_str = str1[::-1]
    final_str = ""
    i = 0
    for i in range(min(len(rev_str), len(token))):
        final_str += rev_str[i]+token[i]

    if len(rev_str) > i+1:
        final_str += rev_str[i+1:]
    if len(token) > i+1:
        final_str += token[i+1:]
    print(rev_str)
    print(token)
    print(final_str)


str1 = "debu123"

reverseStrInterperse(str1)
