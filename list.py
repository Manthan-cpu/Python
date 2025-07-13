#list is a built-in datatype that stores set of values
#list can store elements of different data types
#list is mutable, meaning we can change its elements
#list is ordered, meaning the order of elements is preserved
#list is defined using square brackets
my_list = [1, 2, 3, 4, 5]
print(my_list)           # [1, 2, 3, 4, 5]
print(type(my_list))    # <class 'list'>
#list can store elements of different data types
my_list = [1, "two", 3.0, True]
print(my_list)           # [1, 'two', 3.0, True]
#list is mutable, meaning we can change its elements
my_list[0] = 10
print(my_list)           # [10, 'two', 3.0, True]
#list is ordered, meaning the order of elements is preserved
my_list = [1, 2, 3, 4, 5]
print(my_list[0])        # 1
print(my_list[1])        # 2
print(my_list[2])        # 3
print(my_list[3])        # 4
print(my_list[4])        # 5
#list can be sliced
print(my_list[0:3])      # [1, 2, 3]
print(my_list[1:4])      # [2, 3, 4]
print(my_list[2:])       # [3, 4, 5]
print(my_list[:3])       # [1, 2, 3]
print(my_list[1:])       # [2, 3, 4, 5]
print(my_list[0:2])      # [1, 2]
print(my_list[0:len(my_list)])  # [1, 2, 3, 4, 5]
#list can be checked for membership
print(1 in my_list)      # True
print(6 in my_list)      # False
print(1 not in my_list)  # False
print(6 not in my_list)  # True
#list can be concatenated
my_list2 = [6, 7, 8]
print(my_list + my_list2)  # [1, 2, 3, 4, 5, 6, 7, 8]
#list can be repeated
print(my_list * 2)        # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#list can be iterated
for item in my_list:
    print(item, end=' ')  # 1 2 3 4 5
print()  # for newline
#list can be reversed
my_list.reverse()
print(my_list)           # [5, 4, 3, 2, 1]
#list can be sorted
my_list.sort()
print(my_list)           # [1, 2, 3, 4, 5]
#list can be cleared
my_list.clear()
print(my_list)           # []
#list can be extended
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)           # [1, 2, 3, 4, 5]
#list can be appended
my_list.append(6)
print(my_list)           # [1, 2, 3, 4, 5, 6]
#list can be inserted
my_list.insert(0, 0)
print(my_list)           # [0, 1, 2, 3, 4, 5, 6]
#list can be removed
my_list.remove(3)
print(my_list)           # [0, 1, 2, 4, 5, 6]
#list can be popped
popped_item = my_list.pop()
print(popped_item)       # 6 (last item)
print(my_list)           # [0, 1, 2, 4, 5]
popped_item = my_list.pop(0)
print(popped_item)       # 0 (first item)
print(my_list)           # [1, 2, 4, 5]
#list can be counted
print(my_list.count(2))  # 1 (count of 2 in the list)
print(my_list.count(10)) # 0 (count of 10 in the list)
#list can be copied
my_list_copy = my_list.copy()
print(my_list_copy)      # [1, 2, 4, 5]
#list can be checked for equality
print(my_list == my_list_copy)  # True
print(my_list is my_list_copy)  # False (different objects)
#list can be checked for identity
print(my_list is my_list)  # True (same object)
print(my_list_copy is my_list_copy)  # True (same object)
#list can be checked for type
print(type(my_list) is list)  # True (my_list is of type list)
print(type(my_list_copy) is list)  # True (my_list_copy is of type list)
#list can be checked for truthiness
print(bool(my_list))  # True (non-empty list is truthy)
print(bool([]))       # False (empty list is falsy)     
#list can be checked for length
print(len(my_list))  # 4 (length of the list)
#list can be checked for maximum and minimum values
print(max(my_list))  # 5 (maximum value in the list)
print(min(my_list))  # 1 (minimum value in the list)
#list can be checked for sum
print(sum(my_list))  # 12 (sum of all elements in the list)
#list can be checked for average
print(sum(my_list) / len(my_list))  # 3.0 (average of the list)
#list can be checked for median
sorted_list = sorted(my_list)
n = len(sorted_list)
if n % 2 == 0:
    median = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
else:
    median = sorted_list[n//2]
print(median)  # 2.5 (median of the list)

