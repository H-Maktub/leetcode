class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.temp = [big,medium,small]
    def addCar(self, carType: int) -> bool:
        if self.temp[carType-1]>0:
            self.temp[carType-1] -=1
            return True
        return False

if __name__ == "__main__":
    a = ParkingSystem(1,1,0)
    b = a.addCar(1)
    print(b)