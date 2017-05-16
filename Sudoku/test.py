import copy
a=[[[1,1,1],[1,1,1]],[[1,1,1],[1,1,1]]]
b=list(map(list,a))
#b=copy.deepcopy(a)
print(a,b)
a[1][1][1]=5
print(a,b)
