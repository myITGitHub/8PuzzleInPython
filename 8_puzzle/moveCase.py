import copy
def case(par):
    direction = []
    list1 = []
    k=par.index(0)
    y=k%3
    x=k//3
    if (x <= 1):
        direction.append('up')
    if (x >= 1):
        direction.append('down')
    if (y <= 1):
        direction.append('left')
    if (y >= 1):
        direction.append('right')
    for i in direction:
        par1 = copy.deepcopy(par)
        if i=='up':
            par1[k+3],par1[k]=par1[k],par1[k+3]
        elif i=='down':
            par1[k-3],par1[k]=par1[k],par1[k-3]
        elif i=='left':
            par1[k],par1[k+1]=par1[k+1],par1[k]
        elif i=='right':
            par1[k-1],par1[k]=par1[k],par1[k-1]
        list1.append(par1)
    return list1