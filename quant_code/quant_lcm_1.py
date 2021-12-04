#Find the LCM of given numbers 


num1 = int(input ("Enter a number:"))
num2 = int(input ("Enter a number:"))
num3 = int(input ("Enter a number:"))

numbers =[num1, num2, num3]
factors =[]
l1 = []
for n in numbers: 
    if n>= 1:
        # check for factors
        for i in range(1, n+1):
            if (n % i) == 0:
                factors.append(i)

def most_frequent(List, numbers):
    counter = 0
    num = []
     
    for i in List:
        curr_frequency = List.count(i)
        print(curr_frequency)
        if(curr_frequency==len(numbers)):
            num.append(i)
    num.sort()
    return num[0]

print(f"LCM of {num1}, {num2}, {num3} is ", most_frequent(factors, numbers))
