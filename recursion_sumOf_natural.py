# recursion_sumOf_natural
num = 16

#function
def rec_SumOfnatural(n):
    if n<=1:
        return n
    else:
        return n + rec_SumOfnatural(n-1)

#condition
if num < 0:
    print("Enter the positive number,")
else:
    print('sum of number is',rec_SumOfnatural(num))
