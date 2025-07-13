#set is a collection of unodered items, and each element in the set must be unique and immutable
#list and dictionary can not be stored in a set
collection={1,2,2,3,4,"hello","hello"}
print(collection)#{1, 2, 3, 4, 'hello'}
print(type(collection))#<class 'set'>
print(len(collection))#5

collection.add(6)
print(collection)#{1, 2, 3, 4, 6, 'hello'}

collection.remove(4)
print(collection)#{1, 2, 3, 6, 'hello'}

collection.add((1,2,3,4,5))
print(collection)#{1, 2, 3, 6, 'hello', (1, 2, 3, 4, 5)}

#collection.add([1,2,3,4,5]) unhashable type error
print(collection.pop())#1
print(collection.pop())#2

print(collection)#{3, 'hello', 6, (1, 2, 3, 4, 5)}
set2={1,4,5,6,8,8,0}

print(collection.union(set2))#{0, 1, 3, 4, 'hello', 6, 5, 8, (1, 2, 3, 4, 5)}

print(collection.intersection(set2))#{6}


collection.clear()
print(collection)#set()
