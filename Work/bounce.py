# bounce.py
#
# Exercise 1.5

height = 100
bounce = 1

while bounce <= 10:
    print(bounce, round(height * 0.6, 4))
    bounce = bounce + 1
    height = height * 0.6
