#fobanacci series
term = int(input("hoe many term :"))

n1, n2 = 0, 1
count = 0

if(term< 0):
    print("Enrter positive number.")
elif( term == 1):
    print(n1)
else:
    while(count < term):
        print(n1)
        n = n1 + n2
        # for update
        n1 = n2
        n2 = n
        count +=1