#anoymous_function

#Dispalu power of 2
count = int(input('How many count you want :'))

#anoymous function
result = list(map(lambda x : x ** 2, range(count)))

for i in range(count ):
    #print(count)
    print("2 is raised to power", i, "is", result[i])
