def bubble(x,n):
    """
    冒泡排序，x是列表，n是列表长度
    """
    for i in range(n):
        for j in range(n-1):
            if x[j]>x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x
                
print (bubble([1,10,2,5,41,25,3,48], 8))  #[1, 2, 3, 5, 10, 25, 41, 48]);
