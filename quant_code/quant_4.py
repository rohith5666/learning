#  A number is divisible by 4 if the number formed by its last two digits is divisible by 4.
num = input("Enter a number:")
x = [int(a) for a in str(num)]

if (x[-2]+x[-1])%4 == 0:
    print(num, "is divisible by 4")
else:
    print(num, "is not divisible by 4")

