#a built-in data type that lets us create immutable sequence of values
tuple=(1,2,3,4,5)
print(type(tuple)) # <class 'tuple'>
print(tuple)# (1, 2, 3, 4, 5)
print(tuple[0])  # 1
# tuple[1]=2 gives error
tuple.index(2) #1, gives first index of 2
tuple.count(2)#1, gives the frequency of occurence
