def test(n,x):
    if n==1:
        return False
    while x<=n**(1/2):
        if n%x==0:
            return False
        else:
            x+=1
            test(n,x)
    return True

n=int(input("Enter a number: "))
if test(n,2):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")