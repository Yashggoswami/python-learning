# num1 = float(input())
# num1 = "first"
# print(type(num1))

# camel case
myVariableName = 122434
# pascal case
MyVariableName = "yash goswami"
# snake case
my_variable_name = 2134.534


# red,orange,green = 1,23,34
# print(red,orange,green)

first = second = three = 12

# print(first,second,three)

# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.


list = ("first","second","three","four","five","six","seven")

first,second,*list = list

# print(first,second,three)

# print(first)
# print(second)
# print(list)

num  = 122
string = "yash"
# print(string+str(num))

#global variable in python

def fun():
    global x
    x = 35
    print(x)
# fun()
print(num)

def show():
    global num
    num = 23
    print(num)
show()    
print(num)

