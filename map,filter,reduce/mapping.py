# def cube(n):
#     return n**3

# print(cube(7))
# l = [1,2,3,4,5]
# l1 = list(map(cube , l))
# print(l1)




# With the use of lambda
l = [1,2,3,4,5]
l1 = list(map(lambda x : x**3 , l))
print(l1)