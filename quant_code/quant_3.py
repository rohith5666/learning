#  A number is divisible by 9 only when the sum of its digits is divisible by 9
num = input("Enter a number:")
x = [int(a) for a in str(num)]
s= sum(x)
if s%9==0:
    print(num, "is divisibly by 9")
else:
    print(num, "is not divisibly by 9")