#anoymous_function_2

# Find nu,ber is divisible


my_list = [22,65,54,33,76,221,43,68]
#use annoymous function
result = list(filter(lambda x : (x % 13 == 0),my_list ))
#print
print('teh number divisible by 13 is',result)