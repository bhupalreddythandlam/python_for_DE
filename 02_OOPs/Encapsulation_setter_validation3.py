class CargoShip:
    def __init__(self,weight,speed):
        self.cargo_weight=weight
        self.cargo_speed=speed

    @property
    def cargo_weight(self):
        return self.__cargo_weight

    @property
    def cargo_speed(self):
        return self.__cargo_speed

    @cargo_weight.setter
    def cargo_weight(self,new_weight):
        if new_weight<0:
            print("cargo weight can't be negitive , set to 0")
            self.__cargo_weight=0
        else:
            self.__cargo_weight=new_weight

    @cargo_speed.setter
    def cargo_speed(self,new_speed):
        if new_speed>100:
            print("speed is reached maximum,set to 100")
            self.__cargo_speed=100
        else:
            self.__cargo_speed=new_speed


cs1=CargoShip(90,89)
print(cs1.cargo_weight)
print(cs1.cargo_speed)

cs2=CargoShip(-90,102)
print(cs2.cargo_weight)
print(cs2.cargo_speed)
