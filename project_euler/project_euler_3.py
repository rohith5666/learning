# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
num = int(input ("Enter a number:"))
f = []
pf = []

# This function computes the factor's of input number
def factors(x,f):
    for i in range (1, x+1):
        if x % i == 0 :
            f.append(i)
    #print(f)
factors(num, f)
# This function computes the prime factor's of input number
def prime_factor(y,pf):
    for i in range (2, y):
        if y % i == 0 :
            pf.append(y)
            break
    #print(pf)

n=0
y=0
while n < len (f):
    y= f[n]
    #print(y)
    prime_factor(y,pf)
    n=n+1
# Printing the largest prime factor of input number
print ("Largest prime factor of",num, "is",pf[-1])