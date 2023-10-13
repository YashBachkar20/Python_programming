#sum_natural_number
num = 5
sum = 0
if (num<0):
    print("Enter the positive number.")
else:
    while num > 0:
        sum += num
        num -= 1
        #print("Sum is",sum)
    print("Sum is beyond while loop",sum)