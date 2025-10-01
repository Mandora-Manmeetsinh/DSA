import time

def usingWhile() :
    i = 0
    while i<10 :
        i = i + 1
        print(i)

def usingFor() :
    for i in range(10) :
        print(i)

init = time.time()
usingWhile()
print(time.time() - init)
usingFor()
print(init) 