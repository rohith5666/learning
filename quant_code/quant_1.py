# A number is divisible by 2 if its unit digit is any of 0, 2, 4, 6, 8.

num = input("Enter a number:")
x = [int(a) for a in str(num)]
y = [0, 2, 4, 6, 8]
r = []
i=0
n=0
while n<len(x):
    for i in range(len(x)):
        if x[n]==y[i]:
            r.append(x[n])
        else:
            pass
        i=i+1
    n=n+1
if len(r)>=1:
    print(num, "is divisible by 2")
else:
    print(num, "is not divisible by 2")

