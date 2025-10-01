l = (1,2,3,4,5)
print(l)

# All methods of Tuple
# Answer = ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']  

print(l[0])                 #find Element by index

b = ("a" , "b" , "c" , "d")

count = l.count(4)          # To count occurnce of a number
print(count)

i = l.index(5)              # To find the index of number
print(i)