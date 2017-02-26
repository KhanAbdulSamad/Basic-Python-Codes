a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
z=[n for n in a if n in b]
p=[]
for i in z:
    if i not in p:
        p.append(i)
print(p)
