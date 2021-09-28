#WRITE YOUR CODE IN THIS FILE
def close10(x,y):
    if abs(10 - x) < abs(10 - y):
        return x
    elif abs(10 - x) == abs(10 - y):
        return 0
    else:
        return y
print(close10(12,18))