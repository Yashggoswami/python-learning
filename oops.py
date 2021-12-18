# Object Oriented Principles

#1. class
#2. object
#3. Inheritance
#4. Polymorphism
#5. Encapsulation
#6. Abstraction
#7. Association
#8. Aggregation




#1. Class - Blue Print of Object, Logical Entity, Provides Structure, Collection of Object


class demo:
    # class variable - single copy for every object
    y = 'yash goswami'
    # constructors
    #1. default constructor
    def __init__(self):
        # instance variable - new copy for each object
        self.x = 20
    #2. parameterized constructor
    def __init__(self,m,n):
        self.m = m
        self.n = n
    #class methods or member function
    def sum(self)->int:
        return self.m + self.n
    
    def show(self):
        print('the name is',demo.y)


#2. Object

# if __name__ == '__main__':
#     # object initialized i.e. default and parameterized constructors are called
#     obj = demo(20,10)
#     # sum function is called
#     print(obj.sum())
#     # show function is called
#     obj.show()
#     # using class variable directly
#     print('outer use of class variable',demo.y)
#     # instance variable using reference variable
#     print('m and n values are',obj.m,obj.n)
#     # deleting object
#     del obj


#3. Inheritance - when one class(child class) acquires all the properties of another class(parent class) 


# parent class
class parent:
    y = 'yash goswami'
    
    def __init__(self,n):
        self.n = n
        self.x = 20
        
    def show(self):
        print('inside parent class',self.n,self.x,parent.y)

# child class
class child(parent):
    y = 'yash'
    def __init__(self,n,m):
        self.m = m
        super().__init__(n)
    def display(self):
        print('inside child class',self.n,self.m, child.y,super().y)
        
# ob = child(10000,20000)
# ob.show()
# ob.display()


# Multiple Inheritance
class base1gp:
    def __init__(self):
        print('inside base1gp')
    
class base1p(base1gp):
    def __init__(self):
        print('inside base1p')
    
class base1(base1p):
    def __init__(self):
        print('inside base1')
    y = 'base1'
    
class base2:
    def __init__(self):
        print('inside base2')
    y = 'base2'
    b = 'grant grant parent of base1'
    
    
class drive(base1,base2):
    def show(self):
        print(super().b)

ob = drive()
ob.show()




        
        
    



