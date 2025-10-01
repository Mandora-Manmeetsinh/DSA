l = {1,2,3,4,5}
print(l)

# All methods of Set
# Answer = ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# print(l[0])                 #Does not support search by index

l.add(6)                      #Insert direct element
print(l)

l.remove(2)                   # remove direct element at given index
print(l)

l.pop()                       # Remove the last element
print(l)

# l.sort()                    # Does not support Sorting

# l.clear()                   # To clear the set , not delete
# print(l)

b = {"a" , "b" , "c" , "d"}

l.intersection(b)                 # To add to list
print(l)