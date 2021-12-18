# list comprehension
# ls = {i for i in range(1,21) if i%2==0}
# print(ls)

# dictionary comprehension
# map = {i:f"value{i}" for i in range(1,21) if i%2 == 0}
# map = {value:key for key,value in map.items()}
# print(map)



# All variables which are assigned a value in the class declaration are class variables. And variables that are assigned values inside methods are instance variables.
class experiment:
    def __init__(self):
        pass
    def add(self,n):
        global num
        num = n
    def show(self):
        print(num)

if __name__ == "__main__":
    p1 = experiment()
    p1.add(int(input()))
    print(experiment.num)
    p1.show()