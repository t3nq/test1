import random

def wer(a, b):
    j = random.randint(a,b)
    return j

a = int(input("введите число"))
b = int(input("введите число")) 
res = wer(a,b)
print("Ваше число:", res)
