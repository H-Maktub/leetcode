class SnapshotArray:

    def __init__(self, length: int):
        self.temp = [{}]

    def set(self, index: int, val: int) -> None:
        self.temp[-1][index] = val

    def snap(self) -> int:
        self.temp.append({})
        return len(self.temp)-2

    def get(self, index: int, snap_id: int) -> int:
        res = 0
        while snap_id >= 0:
            if index in self.temp[snap_id]:
                res = self.temp[snap_id][index]
                break
            else:
                snap_id-=1
        return res



a = SnapshotArray(3)
b = a.set(0,5)
print(b)
b =a.snap()
print(b)
b =a.set(0,6)
print(b)
b =a.get(0,0)
print(b)