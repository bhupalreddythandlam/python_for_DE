class SecurityDrone:
    
    active_drones=0

    @staticmethod
    def estimate_flight_time(distance, speed):
        return distance / speed

    def __init__(self,battery,altitude):
        self.battery=battery
        self.altitude=altitude
        SecurityDrone.active_drones+=1

    @property
    def altitude(self):
        return self.__altitude

    @property
    def battery(self):
        return self.__battery

    @altitude.setter
    def altitude(self,new_altitude):
        if new_altitude<0:
            self.__altitude=0
        elif new_altitude>400:
            self.__altitude=400
        else:
            self.__altitude=new_altitude

    @battery.setter
    def battery(self,new_percentage):
        if new_percentage<0:
            self.__battery=0
        elif new_percentage>100:
            self.__battery=100
        else:
            self.__battery=new_percentage


print(f"estimated flight time for flich a : {SecurityDrone.estimate_flight_time(50,30)}")

drone1=SecurityDrone(-5,450)
print(f"allitude if drone : {drone1.altitude} and battery of the drone is : {drone1.battery}")

drone2=SecurityDrone(25,300)
print(f"allitude if drone : {drone2.altitude} and battery of the drone is : {drone2.battery}")




        


