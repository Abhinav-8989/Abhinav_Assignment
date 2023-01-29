# convert a number into binary 

# n=int (input ("Enter a number: "))
# a= []
# while(n>0):
#     digit=n%2
#     a.append(digit)
#     n=n//2
    
# a.reverse()
# print("Binary value is: ")
# for i in a:
#     print(i)


# covert binary into number.

b=int(input("enter a binary value: "))

value, i, a = 0, 0, 0

while(b!= 0): 
        a = b % 10
        value = value + a * pow(2, i) 
        b = b//10
        i += 1
        
print(value)
 