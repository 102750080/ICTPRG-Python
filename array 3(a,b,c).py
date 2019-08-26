b = input("enter a sentence")
word = (b.split())
print(word)
print(word[0])
print(len(word))


if len(word) > 3:
    print(word[2])
    
else: 
    print("nothing") 

count = 0 
while count < (len(word)) :
    count = count + 4
    print(word[1:3]) 
    

 
