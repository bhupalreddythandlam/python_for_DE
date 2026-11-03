class UserAccount:

    default_pass="12345678"

    def __init__(self,password):
        self.password=password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,new_password):
        if len(new_password)<8:
            print("password is too short!,you password set to default")
            self.__password=UserAccount.default_pass
        else:
            print("password updated sucessful!")
            self.__password=new_password

user1=UserAccount("Pass")
print(user1.password)

user2=UserAccount("Password@2")
print(user2.password)