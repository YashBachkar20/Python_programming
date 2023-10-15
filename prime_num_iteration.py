#prime_num_iteration

lower_num = 100
higher_num = 234
num = 0
for i in range(lower_num, higher_num + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:               
               break
        else:
            print(num)