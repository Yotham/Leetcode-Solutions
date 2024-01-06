class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.storage = {"big":big,"medium":medium,"small":small}
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.storage["big"] > 0:
                self.storage["big"]-=1
                return True
            else:
                return False
        elif carType == 2:
            if self.storage["medium"] > 0:
                self.storage["medium"]-=1
                return True
            else:
                return False
        elif carType == 3:
            if self.storage["small"] > 0:
                self.storage["small"]-=1
                return True
            else:
                return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)