from datetime import date

class demomethod:
    name = ""
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = date.today().year-age
    
    # instant method which has one implicit parameter i.e. self
    #used to work on current object
    
    def normalmethod(self):
        print(f"normal function -> {self.name} is {self.age} year old.")
        
    #class method used to work on global variables of the class and implicitly takes cls parameter
    
    @classmethod
    def addname(cls,name,birthyear) -> None:
        cls.name = name
        cls.age = date.today().year-birthyear
    
    @classmethod
    def showclassname(cls) -> None:
        print(f"class function -> {cls.name} is {cls.age} year old")
        
    #static method it does'nt take any parameter and is simply used to perform any utility functions
    
    @staticmethod
    def isvalid(age) -> bool:
        return age > 24
    
    
if __name__ == "__main__":
    demomethod.addname("umesh",1967)
    child1 = demomethod("yash",1999)
    child2 = demomethod("vinay",2001)
    
    child1.showclassname()
    child1.normalmethod()
    child2.normalmethod()
    
    print(f"global variables {demomethod.name} and {demomethod.age}")
    print(f"child1 instance variables {child1.name} and {child1.age}")
    print(f"child2 instance variables {child2.name} and {child2.age}")
    
    print(f"{demomethod.name} is above 24 -> {demomethod.isvalid(demomethod.age)}")
    print(f"{child1.name} is above 24 -> {child1.isvalid(child1.age)}")
    print(f"{child2.name} is above 24 -> {child2.isvalid(child2.age)}")