from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = [[]]
        temp = 0
        def change_to_str(ws,l):
            n = len(ws[-1])
            space = 0
            tempspace = 0
            if n == 1:
                space = maxWidth-l+1
                ws[-1]=ws[-1][-1]+" "*space
            else:
                space = (maxWidth-l+n)//(n-1)
                tempspace = (maxWidth-l+n)%(n-1)
                ret = ""
                for i in range(n-1):
                    ret+=ws[-1][i]+" "*space
                    if tempspace>0:
                        ret+=" "
                        tempspace-=1
                ret+=ws[-1][-1]
                ws[-1]= ret


        for word in words:
            l = len(word)
            if l+temp <= maxWidth:
                ret[-1].append(word)
                temp += l+1
            else:
                change_to_str(ret,temp)
                t = [word]
                ret.append(t)
                temp = l+1
        s=""
        for w in ret[-1]:
            s+=w+" "
        s=s+" "*(maxWidth-len(s))
        ret[-1] =s[:maxWidth]
        return ret

if __name__ == "__main__":
    b = Solution()
    a = b.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)
    print("=======",a)
    a = b.fullJustify(["What","must","be","acknowledgment","shall","be"],16)
    print("=======",a)
    a = b.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20)
    print("=======",a)