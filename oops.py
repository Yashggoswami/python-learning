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

    @classmethod
    def clsmethod(cls):
        print(cls.y)
        

#2. Object

# if __name__ == '__main__':
    
    # object initialized i.e. default and parameterized constructors are called
    # obj = demo(20,10)
    
    # # sum function is called
    # print(obj.sum())
    # # show function is called
    # obj.show()
    # # using class variable directly
    # print('outer use of class variable',demo.y)
    # # instance variable using reference variable
    
    # print('m and n values are',obj.m,obj.n)
    
    #using class method
    # demo.clsmethod()
    
    # # deleting object
    # del obj


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
    
class base1p:
    def __init__(self):
        print('inside base1p')
    
class base1(base1p,base1gp):
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

# ob = drive()
# print(drive.__mro__)
# ob.show()

'''
the object st called the second constructor whereas both have the same configuration. The first method is not accessible by the st object. Internally, the object of the class will always call the last constructor if the class has multiple constructors.
'''
class Animal:
    def __init__(self):    
        self.name = 'yash'
        self.age = 22
        print('Animal constructor is called')
    

    def show(self):
        print(self.name,self.age)

class Dog(Animal):
    def __init__(self):
        super().__init__()
        
    
    def show(self):
        super().show()

# ob = Dog()
# ob.show()


class demoConstructor:
    # def __init__(self):
    #     print('inside second constructor')
    # def __init__(self,m):
    #     print('inside fourth constructor')
    # def __init__(self,n):
    #     print('inside third constructor')
    def __init__(self,n='12',m='yash'):
        print('inside 1st constructor')
        self.n = n
        self.m = m
    
# ob = demoConstructor()
    

#5. Encapsulation   
class Encapsulation:
   
    def __init__(self,n,m,q):
        # Public member
        self.n = n
        self._m = m
        self.__q = q
    
    def show(self):
        print(self.n)
        print(self._m)
        print(self.__q)
        
    def showq(self):
        print(self.__q)
        
    def display(self):
        print('function is in parent class')

class Encapsulation1(Encapsulation):
    def __init__(self,n,m,q):
        super().__init__(n,m,q)
    
    def show(self):
        super().show()
       
    
    
# obj  = Encapsulation('public','protected','private')
# obj.show()


# ob = Encapsulation1('public','protected','private')
# ob.show()
# ob.display()

# print(ob._m)
# ob.showq()


#6. abstraction 
# https://www.godaddy.com/engineering/2018/12/20/python-metaclasses/


class demo:
    g = 'class variable'
    
    def __init__(self,n,m):
        print('inside constructor')
        self.n = n
        self.m = m
        
    # instance method
    def instancemethod(self):
        print(self.n,self.m)
        
    @classmethod
    def clsmethod(cls,name,age):
        print(cls.g)
        return cls(name,age+2)
    @staticmethod
    def stmethod(age):
        return age+5    
    
ob  = demo('yash',23)
ob.instancemethod()
ob = ob.clsmethod('manish',23)

ob.instancemethod()
print(ob.stmethod(25))




        


