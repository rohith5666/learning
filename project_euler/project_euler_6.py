# The sum of the squares of the first ten natural numbers is, 385

# The square of the sum of the first ten natural numbers is, 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is . 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n=1
s= []
c= []

for n in range(1,101):
    a = n**2
    b= n
    s.append(a)
    c.append(b)
    n=n+1
sum_of_squares = sum(s)
sum_of_n = (sum(c))**2
difference = sum_of_n-sum_of_squares
print (difference)