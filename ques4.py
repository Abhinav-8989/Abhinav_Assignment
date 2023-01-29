# Reversing the list by using negative index 


# This is the inbuilt function
l = [10,20,30,40,50]
print(l[::-1])
# THIS IS  non inbuilt function
def fun(a):
    
    x = len(a)
    lst = []
    for i in range(x-1,-1,-1):
        lst.append(a[i])
    return lst

n = [500,400,300,200,100]
print(fun(n))