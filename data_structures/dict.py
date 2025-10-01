l = {"One" : 1 , "Two" : 2 , "Three" : 3}
print(l)

# All methods of Dictionary
# Answer = ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print(l["One"])                 #find Element by index

a = l.get("one")                 #Insert direct element
print(a)

l.pop()                     # Remove the last element
print(l)

l.sort()                    # Sort in ascending order , for desending l.sort(reverse = True)
print(l)

# l.clear()                 # To clear the list , not delete
# print(l)

b = [ "a" , "b" , "c" , "d"]

l.extend(b)                 # To add to list
print(l)

count = l.count(4)          # To count occurnce of a number
print(count)

l.reverse()                 # To reverse the list
print(l)

i = l.index(5)              # To find the index of number
print(i)