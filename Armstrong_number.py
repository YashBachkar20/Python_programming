num = int(input("Enter a number: "))

sum = 0

# find the sum of the cube of each digit
temp = num
print(temp)
while temp > 0:
   print(temp)
   digit = temp % 10
   print(digit)
   sum += digit ** 3
   print("Difit =",digit)
   print("Sum =",sum)
   temp //= 10


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")