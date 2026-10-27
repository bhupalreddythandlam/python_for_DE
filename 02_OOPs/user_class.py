class user:
    def __init__(self,username,mail,mobile):
        self.username=username
        self.mail=mail
        self.mobile=mobile

    def say_hi_to_user(self,user):
        print(f"sending message to {user.username} : hello {user.username},it is {self.username}")

user1=user("bhupal","bhupal8@gmail.com","Password@2")
user2=user("bhupathi","bhupathi@gmail.com","abc123")

user2.say_hi_to_user(user1)