# list comprehension
ls = {i for i in range(1,21) if i%2==0}
print(ls)

# dictionary comprehension
map = {i:f"value{i}" for i in range(1,21) if i%2 == 0}
map = {value:key for key,value in map.items()}
print(map)

