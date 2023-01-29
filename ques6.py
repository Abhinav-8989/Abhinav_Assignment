lst = ["happy","1",2,3,4,5,"pbx","cr"]
lst1 = ["apache","i","himachal",99,88,77,"car","NATIONAL"]
def fun(lst,x):
    lst2 = []
    for i in range(len(lst)):
        if(i%2!=0):
            lst2.append(lst[i])
    for j in range(len(x)):
        if(j%2==0):
            lst2.append(x[j])
    return lst2



print(fun(lst,lst1))