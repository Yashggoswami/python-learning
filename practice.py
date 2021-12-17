# # print('hello world')

# # x = 5
# # y = 'yash goswami'
# # z = 0.6

# # l = list()
# # l.append(x)
# # l.append(y)
# # l.append(z)

# # print(l)
# # print(type(l))

# # x = y = z = 0.1
# # print(x,y,z)
# # x,y,*z = list((0.1,0.2,0.3,0.4,0.5))
# # print(x,y,z)

# # x=5
# # y = 'john '
# # print(y*x)

# # x = "awesome"

# # def myfunc():
# #   global x
# #   #what it will print
# #   print(x)
# #   x = "fantastic"
# #   print("Python is " + x)

# # myfunc()

# # print("Python is " + x)







# # s = 'yash goswami'
# # s = 123
# # s = 0.1
# # s = 12j

# # l = [12,'yash',34,2312,45]
# # t = (23,'yash','goswami','manish')
# # x = range(10)
# # print(l)
# # print(t,type(t))
# # for i in x:
# #     print(str('*'*i).center(30-i))



# # l = [i for i in range(10)]
# # print(l)
# # l.append(12)
# # print(l)
# # print(f'index of element 12 is {l.index(12)}')

# # s = l.copy()
# # a = l

# # l.append(14)

# # # it must remain unchanged 
# # print(f's is a copy of l and not actual l {s}')
# # # it must be changed
# # print(f'a is just another name of l since we have assigned l in a {a}')

# # a.remove(12)
# # print(l)





# # methods in list type

# # l = list(('yash','manish','suryan','adarsh'))
# # s = ['lakhan','ki','gaand']

# # # 1. append
# # l.append('annu')
# # print(l)
# # # 2. copy
# # t = l.copy()
# # print(t)
# # #3. extend
# # t.extend(s)
# # print(t)
# # # 4. index
# # print(t.index('annu'))
# # # 5. count
# # t.append('annu')
# # print(t.count('annu'))
# # #6. insert
# # t.insert(0,'humtum')
# # t.insert(100,'yashhhhyyyyy')
# # print(t)
# # # 7. pop
# # t.pop(1)
# # print(t)
# # # 8. remove
# # t.remove('annu')
# # print(t)
# # # 9. reverse
# # t.reverse()
# # print(t)
# # #10. sort
# # t.sort()
# # print(t)

# # print('-'.join(t))

# #tuple

# # tu = tuple(('yash','yash','goswami','is','the','best'))
# # t = ('yash','gosami')
# # l = ['aysh']

# # print(tu.count('yash'))

# # print(tu.index('yash'))

# #  set

# y = set(('yash','yash','goswami','vinay'))
# s = {'annu','12','12','yash','yash','manish','goswami'}
# # # print(s,y)
# # # print(s.difference(y))
# # # s.difference_update(y)
# # print(s)
# # s.discard('11')
# # # print(s)
# # print(y)
# # # s.intersection_update(y)
# # # print(s.isdisjoint(y))
# # print(s.issubset(y))
# # print(s.issuperset(y))
# # # s.pop()
# # print(s)
# # # print(s.symmetric_difference(y))
# # print(s.union(y))
# # print(s.update(y))

# # print(bool(''))




# # l = [12,434,354,545,454,545,54,5,56,56]
# # print(l[7:3:-1])

# #Set methods

# #1. intersection
# #2. union
# #3. update
# #4. difference
# #5. difference_update
# #6. intersection_update
# #7. isdisjoint
# #8. issubset
# #9. issuperset
# #10. add
# #11. pop
# #12. remove
# #13. discard
# #14. copy
# #15. clear


# d = {1:'yash',2:'vinay',3:'goswami',4:'manish'}
# a ={i:chr(96+i) for i in range(1,11)}
# # print(d)
# # print(a)

# #1. ord - tells the unicode of a character
# # print(ord('a'))
# # #2. chr - gives the character as per the provided unicode
# # print(chr(97))


# # dictionary methods
# #1. clear - clears all the key and value pairs from the dictionary
# # d.clear()
# # #2. copy
# # q = d.copy()
# # # print(q)
# # #3. from key - generates dictionary with corrosponding keys by keeping a default value
# # # temp =  dict.fromkeys(range(10),0)
# # # print(temp)
# # #4. get method
# # # print(d.get(2))
# # # print(d.items())

# # # for i,j in d.items():
# # #     print(f'{i} = {j}')
    

# # # keys
# # # l = list(d.keys())
# # # print(l)

# # # pop
# # # .pop(0)
# # # print(d)d
# # # d[5] = 'annu'
# # # print(d)

# # # d.popitem()
# # # print(d)







# # print(d)
# # print(d.setdefault(6,'chinu'))
# # print(d)

# # d[7] = 'superman'
# # print(d)
# # d.update({8:'batman'})
# # print(d)


# #if else if and else statement
# # or      
# # conditional statement

# # a = 4
# # if a==0:
# #     print('a is zero')
# # elif a>0:
# #     print('a is greater than zero')
# # else:
# #     print('a is hero')


# # list comprehension
# # l =  [i for i in range(10) if i%2==0 or i>5]

# # print(l)



# # # i = 0
# # # while i<=10:
# # #     print(str(i).center(2).rjust(i+1,'-'),end='')
# # #     print(''.ljust(i*2,'-'))
# # #     i+=1
    
    
    
    
# # # string methods

# # s = 'abcdefghijklmnopqrstuvwxyz'

# # print(s.capitalize())
# # print(s.upper())
# # print(s.lower())
# # print(s.isupper())
# # print(s.islower())
# # print(s.count('a'))
# # print(''.join(sorted(s)))


# # z = 'yash'
# # print(z.center(25,'-'))
# # print(z.ljust(25,'-'))
# # print(z.rjust(25,'-'))
# # print(s.endswith('xyz'))
# # print(z.startswith('y'))

# # t  = '.'.join(list(map(chr,range(65,65+26))))
# # print(t)


# # t = '-'.join([chr(i) for i in range(65,65+26)])
# # print(t)
# # t+='A'
# # print(t)
# # print(t.find('A'))
# # print(t.rfind('A'))
# # # print(list(t.split('-')))
# # print(t.replace('-','*'))
# # w=5
# # print(f'{t} is a {w} string')
# # print('{1} {0}'.format(w,t))









# def my_fun(*myname):
#     print(f'{myname[0]} this is the first function ever')
#     print(myname[1])
    

# name = 'yash'
# my_fun(name,'manish')
# print(name)


# def  demo_fun(a,b,c):
    # print(a,b,c)

#keyword arguments  
# demo_fun(b='yash',c='goswami',a='manish')

# arbitary arguments
# def demo(**arg):
#     print(arg['b'])
#     print(arg['a'])
# def de(*ar):
#     print(ar[0])
#     print(ar[1])
# de('yash','goswami')
# demo(b='goswami',a='yash')



# int return type
# fun name of function
#  s - argument
# string  - type of argument

# int fun(String st){
#     #return statement
#     return Integer.parseInt(st);
# }

#str - return type
#l - argument
#list - type of argument

# def d(l:list)->str:
#     return '.'.join(l)

# l = list(map(str,range(10)))
# print(d(l))



# def fab(a:int)->int:
#     if a<=0:
#         return 0
#     if a==1 or a==2:
#         return 1
#     return fab(a-1)+fab(a-2)

# #  0 1 1 2 3 5 8
    
# print(fab(6))


# s = {1,2,3,34,34,4}
# print(s)

# def demoset(s):
#     s.add(12)
#     print('inside',s)
    
# demoset(s.copy())
# print('outside',s)

# a = 20

# def sum():
#     global a
#     a = 10
#     print(a)

# sum()
# print(a)


# 1. call by value - immutable object uses different memory location
# any change in variable will create object in new memory location soo that if outer variable is used the changes will not be reflected

#2. call by reference - mutable object uses same memory location

# any changes in variable will not create any other object in memory and will make changes in same memory location therefore if outer variable is used it will show the reflected changes











