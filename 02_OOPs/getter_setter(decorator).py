class AlienSpacecraft:
    def __init__(self,shield_level):
        self.__shield_level=shield_level

    @property
    def shield_level(self):
        return self.__shield_level

    @shield_level.setter
    def shield_level(self,new_level):
        if new_level>100:
            self.__shield_level=new_level
            print("you reach the maximum level,congrats!")
        elif new_level<0:
            self.__shield_level=0
            print("WARNING: Hull breached!")
        else:
            self.__shield_level=new_level
            print("level is updated")

    @property
    def status(self):
        if self.__shield_level>50:
            return "Optimal"
        elif self.__shield_level<50 and self.__shield_level>1:
            return "critical"
        else:
            return "destroyed"

sc1=AlienSpacecraft(-20)
print(f"current level : {sc1.shield_level}")
print(sc1.status)
sc1.shield_level=-1
print(sc1.status)