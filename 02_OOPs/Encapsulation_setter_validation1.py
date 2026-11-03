"""
Goal: Create a Thermostat class that takes a starting temperature in __init__.

The Rules: Create a getter and setter for temperature. The setter must ensure the temperature never drops below 50 and never goes above 90. If a number outside that range is given, cap it at 50 or 90.

"""

class Thermostat:
    def __init__(self,temp):
        self.temperature=temp

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self,new_temp):
        if new_temp>90:
            print("temperature exceeds the range , cap to max")
            self.__temperature=90
        elif new_temp<50:
            print("temperature is below the range , cap to min")
            self.__temperature=50
        else:
            self.__temperature=new_temp


t1=Thermostat(45)
print(t1.temperature)