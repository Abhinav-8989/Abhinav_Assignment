
#HEre we enter the sentence
str = input("Write the Sentence: ") 
 
# Taking lower number from string
str = str.lower()

# this is the list of English vovels
list = ["a","e","i","o","u"]
# This is the length of the string
L = len(str)

# here vovles
vovel = 0
# here consonent
consonent = 0

# Now print the function
print(L)

for i in range(0,L):
    if(str[i] in list):
        vovel = vovel +1
    else:
        consonent = consonent + 1
print(f"Vovels : {vovel}")
print(f"Consonent {consonent}")