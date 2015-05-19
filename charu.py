def insert(x,n):
     i = 1
     while i<n:
         key = x[i]
         j = i-1
         while j>=0 and key<x[j]:
             x[j+1]= x[j]
             j -= 1
         x[j+1] = key
         i += 1
     return x

print (insert([2,1],2))   #[1, 2, 3, 5, 10, 25, 41, 48]
