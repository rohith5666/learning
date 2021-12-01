#Find the HCF of given numbers 

num1 = int(input ("Enter a number:"))
num2 = int(input ("Enter a number:"))
num3 = int(input ("Enter a number:"))

numbers =[num1, num2, num3]
factors =[]
l1 = []
l2 =[]
l3 =[]
l4 =[]
for n in numbers: 
    if n>= 1:
        # check for factors
        for i in range(1, n):
            if (n % i) == 0:
                factors.append(i)

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

print(f"HCF of {num1}, {num2}, {num3} is ",most_frequent(factors))
