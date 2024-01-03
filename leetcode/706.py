class MyHashMap:

    def __init__(self):
        self.temp = [[] for _ in range(10000)]

    def hash(self,key):
        return key % 10000
    def pos(self, key):
        return key // 10001


    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        
        if not self.temp[hashkey]:
            self.temp[hashkey] = [-1] * 10001
        self.temp[hashkey][self.pos(key)] = value


    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        # print(hashkey)
        if self.temp[hashkey] == []:
            return -1
        return self.temp[hashkey][self.pos(key)]


    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if self.temp[hashkey]:
            self.temp[hashkey][self.pos(key)] = -1

if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1) # myHashMap 现在为 [[1,1]]
    myHashMap.put(2, 2) # myHashMap 现在为 [[1,1], [2,2]]
    print(myHashMap.get(1))    # 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
    print(myHashMap.get(3))    # 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
    myHashMap.put(2, 1) # myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
    print(myHashMap.get(2))    # 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
    myHashMap.remove(2) # 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
    print(myHashMap.get(2))    # 返回 -1（未找到），myHashMap 现在为 [[1,1]]

#