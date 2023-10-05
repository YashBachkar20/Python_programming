#hcf_euclidean_algo

def hcf(x, y):
    while y:
        print("While loop y :", y)
        x, y = y, x % y
        print("After x :", x)
        print("After y :", y)
    return x

result = hcf(300,400)
print("H C F is",result)