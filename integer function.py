def prime():
    x= int(input("Enter a number:"))
    s=[]
    for i in range (1,x+1):
        if x%i == 0:
            s.append(i)
    if s==[1,x]:
        print("number is prime")
       # print(s)
    else:
        print("number is not prime")
        #print(s)
while 1==1:
    prime()
        
    
