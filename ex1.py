
n=int(input())

def jaegwi(n):
    if n==1:
        return 1
    return n+jaegwi(n-1)


print(jaegwi(n))

print