def select(x,n):
    for i in range(n-1):
        key = i
        for j in range(i+1,n):
            if x[j] < x[key]:
                 key = j
        if key!=i:
            t = x[i]
            x[i] = x[key]
            x[key] = t
    return x

print select([1,10,2,5,41,25,3,48],8)   #[1, 2, 3, 5, 10, 25, 41, 48]