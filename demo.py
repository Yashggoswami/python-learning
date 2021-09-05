class demo:
    def __init__(self):
        self.first = 0
    def takefun(self):
        self.first = int(input())
    def show(self):
        print(self.first,"is a number") if isinstance(self.first,int) else print(self.first,"it is not a number")

def start():
    p1 = demo()
    p1.takefun()
    p1.show()

start()