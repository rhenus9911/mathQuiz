import random

num = input("입력: ")

n = random.randint(1, 5)

if n==num:
    print("good")
else:
    print("fail")