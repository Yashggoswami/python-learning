# # num1 = float(input())
# # num1 = "first"
# # print(type(num1))

# # camel case
# myVariableName = 122434
# # pascal case
# MyVariableName = "yash goswami"
# # snake case
# my_variable_name = 2134.534


# # red,orange,green = 1,23,34
# # print(red,orange,green)

# first = second = three = 12

# # print(first,second,three)

# # If you have a collection of values in a list1, tuple etc. Python allows you extract the values into variables. This is called unpacking.


# list1 = ("first","second","three","four","five","six","seven")

# first,second,*list1 = list1

# # print(first,second,three)

# # print(first)
# # print(second)
# # print(list1)

# num  = float(122)
# string = "yash"
# # print(string+str(num))

# #global variable in python

# def fun():
#     global x
#     x = 35
#     print(x)
# # fun()
# #print(num)

# def show():
#     global num
#     num = 23
#     print(num)
    
# #show()    
# #print(num)

# r = 1+32+5+\
#     +545
# #print(r)

# num = 324.2324
# num = "yash"
# #print(type(num))

# print(list(range(10,0,-1)))

# list2 = list(range("a","z"))
# print(list2)
# print(list("abc"))


company = [["yash",24],\
           ["vinay",3],\
            ["ananya",12]]


def sort_key(company):
    return company[0]

company.sort(key=sort_key,reverse = True)

print(company)