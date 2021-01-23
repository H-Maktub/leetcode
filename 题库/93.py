from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        retList = []
        temp=["0"] *4
        l = len(s)
        def nextNum(i:int,n:int):
            if i>=l:
                return
            if n==3:
                num = s[i:]
                if (num == "0") or (num[0]!="0" and int(num)<=255):
                    temp[n] = num
                    ip = ".".join(temp)
                    retList.append(ip)
                return
            for x in range(i,l):
                num = s[i:x+1]
                if (num == "0") or (num[0]!="0" and int(num)<=255):
                    if n <3:
                        temp[n] = num
                        nextNum(x+1,n+1)
                else:
                    break

        nextNum(0,0)
        return retList

if __name__ == "__main__":
    a = Solution()
    b = a.restoreIpAddresses("25525511135")
    print("======",b)#["255.255.11.135","255.255.111.35"]
    b = a.restoreIpAddresses("101023")
    print("======",b)#["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]