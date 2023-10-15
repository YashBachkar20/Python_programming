#prime_number

def prime_number(num):
    #crete flag variable
    flag = False
    if(num == 1):
        print(num," its not the prime number.")
    elif(num > 1):
        for i in range(2, num):
            if(num % i == 0):
                #factor found
                flag = True
                break
        # check if flag is True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
    return num

num = 31
print("The prime number is ",prime_number(num))

