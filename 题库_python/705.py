class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp = [[] for _ in range(1000)]
    def hash(self,key):
        return key % 1000
    def pos(self, key):
        return key // 1001

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        
        if not self.temp[hashkey]:
            self.temp[hashkey] = [0] * 1001
        print(hashkey,self.pos(key))
        self.temp[hashkey][self.pos(key)] = True
        # print(self.temp,hashkey)

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if self.temp[hashkey]:
            self.temp[hashkey][self.pos(key)] = False

    def contains(self, key: int) -> bool:
        hashkey = self.hash(key)
        # print(hashkey)
        return self.temp[hashkey] != [] and self.temp[hashkey][self.pos(key)]



# Your MyHashSet object will be instantiated and called as such:
if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1000000)     
    myHashSet.add(2);     
    # myHashSet.contains(1)
    print(myHashSet.contains(1000000))
    # myHashSet.contains(3)
    # print(myHashSet.contains(3))
    # myHashSet.add(2)
    # myHashSet.contains(2)
    # print(myHashSet.contains(2))
    # myHashSet.remove(2)
    # myHashSet.contains(2)
    # print(myHashSet.contains(2))
