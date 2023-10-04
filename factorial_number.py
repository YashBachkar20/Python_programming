#factorial_number
num = 4
factorial = 1
# if number is negative
if num < 0:
    print(" factorial does not esits. ")
elif(num == 0):
    print("The factoria of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial *=i 
    print("The factorial number",num," is ",factorial)
    