
dict={"key1":1234,"k2":"ram"}
list1=[1234,"ram",1,2,3,4,"kshbkj","ashdiuas"]
list2=[]
for key,value in dict.items():
    for i in list1:
        if(value == i):
            list2.append(i)

print(list2)           