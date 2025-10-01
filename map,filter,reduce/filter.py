l = [1,2,3,4,5]
def filter_fun(l):
    return l<5

newl = filter(filter_fun , l)
print(list(newl)) 