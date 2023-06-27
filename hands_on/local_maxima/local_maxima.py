def local_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    localmax = []
    for e in x:
        if e.index == 0:
            if e > e.index+1:
                localmax.append(e)
            else:
                continue

        elif e.index == len(x):
            if e > e.index-1:
                localmax.append(e)
            else:
                continue
            
        elif e > x.index(e)+1 and e > x.index(e)-1:
            localmax.append(e)
        
        else:
            continue            
    return localmax


t1 = [1, 3 ,-2, 0, 2, 1]
t2 = [-1,-1,0,-1]
t3 = [4,2,1,3,1,5]
t4 = [1,2,2,1]
t5 = [1,2,2,3,1]
test = [t1, t2, t3, t4, t5]
for e in test:
    a,b = local_maxima(e)
    print(f"Result {e}")
    print(a,b)
