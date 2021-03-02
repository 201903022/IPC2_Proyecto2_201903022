
n= 5
m = 4
for i in range(0,(n-1)) : 
  k = i * m
  l = k + m 
  for j in range (k,l):
     paz = j
     union = j+m
     #dot.edge(str(k),str(union))
     print(str(paz), " -> ",str(union))
  print("***************")