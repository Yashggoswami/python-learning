# print('hello world')

# x = 5
# y = 'yash goswami'
# z = 0.6

# l = list()
# l.append(x)
# l.append(y)
# l.append(z)

# print(l)
# print(type(l))

# x = y = z = 0.1
# print(x,y,z)
# x,y,*z = list((0.1,0.2,0.3,0.4,0.5))
# print(x,y,z)

# x=5
# y = 'john '
# print(y*x)

# x = "awesome"

# def myfunc():
#   global x
#   #what it will print
#   print(x)
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)







# s = 'yash goswami'
# s = 123
# s = 0.1
# s = 12j

# l = [12,'yash',34,2312,45]
# t = (23,'yash','goswami','manish')
# x = range(10)
# print(l)
# print(t,type(t))
# for i in x:
#     print(str('*'*i).center(30-i))



# l = [i for i in range(10)]
# print(l)
# l.append(12)
# print(l)
# print(f'index of element 12 is {l.index(12)}')

# s = l.copy()
# a = l

# l.append(14)

# # it must remain unchanged 
# print(f's is a copy of l and not actual l {s}')
# # it must be changed
# print(f'a is just another name of l since we have assigned l in a {a}')

# a.remove(12)
# print(l)





# methods in list type

# l = list(('yash','manish','suryan','adarsh'))
# s = ['lakhan','ki','gaand']

# # 1. append
# l.append('annu')
# print(l)
# # 2. copy
# t = l.copy()
# print(t)
# #3. extend
# t.extend(s)
# print(t)
# # 4. index
# print(t.index('annu'))
# # 5. count
# t.append('annu')
# print(t.count('annu'))
# #6. insert
# t.insert(0,'humtum')
# t.insert(100,'yashhhhyyyyy')
# print(t)
# # 7. pop
# t.pop(1)
# print(t)
# # 8. remove
# t.remove('annu')
# print(t)
# # 9. reverse
# t.reverse()
# print(t)
# #10. sort
# t.sort()
# print(t)

# print('-'.join(t))

#tuple

# tu = tuple(('yash','yash','goswami','is','the','best'))
# t = ('yash','gosami')
# l = ['aysh']

# print(tu.count('yash'))

# print(tu.index('yash'))

#  set

# y = set(('yash','yash','goswami'))
# s = {'12','12','yash','yash','manish'}
# print(s,y)
# # print(s.difference(y))
# s.difference_update(y)
# print(s)


l = [12,434,354,545,454,545,54,5,56,56]
print(l[7:3:-1])


























