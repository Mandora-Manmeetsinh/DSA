l = [1,2,3,4,5]
print(l)

# All methods of List
print(dir(l))
# Answer = ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(l[0])                 #find Element by index

l.append(6)                 #Insert direct element
print(l)

l.insert(1 , 9)             #Insert at given index
print(l)

l.remove(2)                 # remove direct element at given index
print(l)

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

c = [1,3,5,7,2,7,3,9,3]
print(f"List {c} before sorting")
c.sort()
print(f"List {c} after sorting")

a = 123
b = 12

# a=a+b                     # 1st way to swap 
# b=a-b
# a=a-b
# print(a,b)

def swap(a,b):              # 2nd way to swap numbers using function
        d = a
        a = b
        b = d

        return a,b

print(swap(10,20))
print(swap(20,10))
print(swap(10,20))
