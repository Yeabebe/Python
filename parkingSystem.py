class ParkingSystem: 
    def __init__(self, big: int, midium: int, small: int):
        self.slots = {
            1: big,
            2: midium, 
            3: small
        }

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True 
        return False