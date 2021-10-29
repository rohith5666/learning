#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

n=1
multiples = []
while n<1000:
    if n%3==0:
        multiples.append(n)
    elif n%5==0:
        multiples.append(n)
    else:
        pass
    n=n+1
#print(multiples)
print("Sum of multiples of 3 & 5 below 1000 is", sum(multiples))