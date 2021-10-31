#  A number is divisible by 3 only when the sum of its digits is divisible by 3
num = input("Enter a number:")
x = [int(a) for a in str(num)]
s= sum(x)
if s%3==0:
    print(num, "is divisibly by 3")
else:
    print(num, "is not divisibly by 3")