import ast

l1 = input()
l1 = ast.literal_eval(l1)
print(type(l1))