class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def bark(self):
        print("bow , bow")

dog1 = Dog("goldy","labrador")
print(dog1.breed)

# basic structure of creating class and objects

class owner:
    def __init__(self,name,address,mobile):
        self.name=name
        self.address=address
        self.phone_number=mobile

class property:
    def __init__(self,name,size,country,owner):
        self.property_name=name
        self.property_size=size
        self.country=country
        self.owner=owner

owner1=owner("bhupal","tirupathi",0000000000)

propert1=property("danial","5000 sqft","india",owner1)
print(f"owner of the property {propert1.owner.name}")