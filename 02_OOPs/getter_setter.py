class Secreateagent:
    def __init__(self,name,code,status):
        self.__real_name=name
        self._Agent_code=code
        self.status=status

    def get_real_name(self):
        return self.__real_name

    def get_Agent_code(self):
        return self._Agent_code

    def set_real_name(self,new_name):
        self.__real_name=new_name

    def set_agent_code(self,newcode):
        self._Agent_code=newcode

a1=Secreateagent("james","A007","Active")

"""
so we are unable to access the private attributes from the outside class and we do not access the protected attributes also from out side the class.
so here we create the methods to view and update protected and private attributes.
this concept is called getter's and setter's
"""
# calling the values of the protected and private attributes.
print(f"hello {a1.get_real_name()} your code is {a1.get_Agent_code()} and your status is {a1.status}")

# updating the values of protected and private attributes.
a1.set_real_name("james bond")

print(f"hello {a1.get_real_name()} your code is {a1.get_Agent_code()} and your status is {a1.status}")