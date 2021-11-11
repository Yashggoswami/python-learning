class mycls:
    @staticmethod
    def myfun():
        print('this is static method')

obj = mycls()
mycls.myfun()
obj.myfun()