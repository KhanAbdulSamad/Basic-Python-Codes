def list_end(t):
    return(t[0],t[-1])
    

s=int(input("Enter how many number in list:"))
q=[]
for i in range(1,s+1):
    p = int(input("Enter %d i number:"))
    q.append(p)
print(list_end(q))
