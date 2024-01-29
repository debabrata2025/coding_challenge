# Input: s = "a good   example"
# Output: "example good a"


def reverseWord(s):
    l1 = s.split()
    l1.reverse()
    newstr = ' '.join(l1)
    print(newstr)

s1 = "I eat rice"
reverseWord(s1)