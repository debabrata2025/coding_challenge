#string compare challenge ->
# "copy" and "cpoy" -> true else -> false
def compStr(str1, str2):
    #checking length of two str are same or not
    if len(str1) != len(str2):
        return False
    #string to list
    s1 = list(str1)
    s2 = list(str2)
    #sorting lists
    s1.sort()
    s2.sort()
    #check the sorted list are same or not
    if(s1 == s2):
        return True

str1 = "cat"
str2 = "tac"
print(compStr(str1, str2))


