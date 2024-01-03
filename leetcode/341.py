class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.temp = []
        def dfs(t):
            for i in t:
                if i.isInteger() == True:
                    self.temp.append(i.getInteger())
                else:
                    dfs(i.getList())
        dfs(nestedList)
        self.len = len(self.temp)
        self.number = 0
    def next(self) -> int:
       
        t= self.temp[self.number]
        self.number  +=1
        return t
    
    def hasNext(self) -> bool:
        return not self.len==self.number