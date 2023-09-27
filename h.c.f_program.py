#h.c.f_program
def hcf(n1, n2):
    if n1 > n2:
        smaller = n2
    else:
        smaller = n1

    for i in range (1, smaller + 1):
        if(( n1 % i == 0) and ( n2 % i == 0)):
            hcf = i
    return hcf

num_1 = 54
num_2 = 24

print("The hcf is :",hcf(num_1, num_2))