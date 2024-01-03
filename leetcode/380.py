import random
class RandomizedSet:
    
    def __init__(self):
        self.temp = set()
    def insert(self, val: int) -> bool:
        if val in self.temp:
            return False
        self.temp.add(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.temp:
            return False
        self.temp.remove(val)
        return True

    def getRandom(self) -> int:
        n = random.randint(0, len(self.temp)-1)
        return list(self.temp)[n]

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
# param_2 = obj.remove(val)
param_3 = obj.getRandom()