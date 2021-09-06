# string = "yash goswami is so so intellingent no one can be like yash and it's a fact"
# print(string.count("yash",0,12))

# print(string.capitalize())
# print(string.upper())
# st1 = "yash"
# st2 = "goswami"

# print(st1.center(121))

# pattern to make pramid using string.center() function
if __name__ == "__main__":
  num  = int(input())
  for i in range(1,num+1):
      print(("*"*i).center(num+1))
