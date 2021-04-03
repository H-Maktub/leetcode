class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        i = 0
        while  i<len(s1) and i<len(s2) and s1[i]==s2[i]:
            i+=1
        j=-1
        while -j<=len(s1) and -j<=len(s2) and s1[j] == s2[j]:
            j-=1
        print(i,j,s2[i-1],s2[j+1])
        if i==0 and j==-1:
            return False
        if i-j-1!=len(s1) and i-j-1!=len(s2):
            return False
        return True

a = Solution()
b = a.areSentencesSimilar("My name is Haley","My Haley")
print(b)
b = a.areSentencesSimilar("of","A lot of words")
print(b)
b = a.areSentencesSimilar("Eating right now","Eating")
print(b)
b = a.areSentencesSimilar("Luky","Lucccky")
print(b)
b = a.areSentencesSimilar("c h p Ny","c BDQ r h p Ny")
print(b)
b = a.areSentencesSimilar("qbaVXO Msgr aEWD v ekcb","Msgr aEWD ekcb")
print(b)
b = a.areSentencesSimilar("eTUny i b R UFKQJ EZx JBJ Q xXz","eTUny i R EZx JBJ xXz")
print(b)