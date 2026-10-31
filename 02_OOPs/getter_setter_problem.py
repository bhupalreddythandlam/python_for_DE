class dragon:
    def __init__(self,fire_power):
        self.__fire_power=fire_power

    @property
    def fire_power(self):
        return self.__fire_power

    @fire_power.setter
    def fire_power(self,new_f_p):
        if new_f_p>1000:
            self.__fire_power=1000
            print("maximum capacity reached!")
        elif new_f_p<0:
            self.__fire_power=0
            print("power depleted!")
        else:
            self.__fire_power=new_f_p

    @property
    def danger_level(self):
        if self.__fire_power > 800:
            return "Catastrophic"
        elif self.__fire_power>300 and self.__fire_power<=800:
            return "High"
        elif self.__fire_power<=300:
            return "manageable"
        else:
            return "error fetching danger level,try again"

d1=dragon(5000)
print(f"dragon level (initial) : {d1.fire_power}")
print(f"danger level (initial): {d1.danger_level}")

d1.fire_power=300
print(f"dragon level (after updated) : {d1.fire_power}")
print(f"danger level (after updated): {d1.danger_level}")
