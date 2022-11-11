def even(arr):
    
    res = []
    n = len(arr)
    
    if n == 1:
        if arr[0] % 2 == 0:
            return res.append(arr[0])
        return res
    
    res = even(arr[0:n-1])
    if arr[n-1] % 2 == 0:
        res.append(arr[n-1])
        return res
        
    return res



