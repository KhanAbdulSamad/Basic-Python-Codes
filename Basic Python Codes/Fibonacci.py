def febi():
     s=[]
     i=1
     if q ==1:
        s=[1]
     elif q==2:
          s=[1,1]
     elif q>2:
          s=[1,1]
          while i<q-1:
               s.append(s[i]+s[i-1])
               i+=1
     return s
q = int(input("Enetr a:"))
print(febi())
