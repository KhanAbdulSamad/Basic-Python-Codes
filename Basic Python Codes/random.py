import random
a = random.randint(1,9)
while True:
    x = input("Enter:")
    if x=="exit":
        break
    x=int(x)
    if x<a:
        print("Entered number is low")
    elif x>a:
        print("Entered number is high")
    else:
        print("Both are equal")
    
    
         
