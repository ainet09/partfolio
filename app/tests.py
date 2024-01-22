from django.test import TestCase

# n = 13
# if n % 2 == 0 and n % 7 == 0 and n % 11 != 0 and n % 13 != 0:
#     print("ishladi")
# else:
#     print("ishlamadi")
# import random

asadb = []

for i in range(1, 100):
    
    if i % 2 == 0 and i % 7 == 0 and i % 11 != 0 and i % 13:
        asadb.append(i)
        print("ishladi")
    
    else:
        print("ishlamadi")

