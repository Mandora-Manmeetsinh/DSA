# ============================================================ #
# ============================================================ #
# ============================================================ #
# async function 1st approch

# import time

# def func1() :
#     time.sleep(3)
#     print("Function 1")

# def func2() :
#     time.sleep(2)
#     print("Function 2")

# def func3() :
#     time.sleep(4)
#     print("Function 3")

# func1()
# func2()
# func3()

# =============================================================== #
# =============================================================== #
# =============================================================== #
# async function 2nd approch

# import time
# import asyncio

# async def func1() :
#     # time.sleep(3)
#     await asyncio.sleep(1)
#     print("Function 1")

# async def func2() :
#     # time.sleep(2)
#     await asyncio.sleep(1)
#     print("Function 2")

# async def func3() :
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("Function 3")

# async def main() :
#     task  = asyncio.create_task(func1())
#     task  = asyncio.create_task(func2())
#     task  = asyncio.create_task(func3())
    
# asyncio.run(main())

# =================================================================== #
# =================================================================== #
# =================================================================== #

import time
import asyncio

async def func1() :
    # time.sleep(3)
    await asyncio.sleep(1)
    print("Function 1")

async def func2() :
    # time.sleep(2)
    await asyncio.sleep(1)
    print("Function 2")

async def func3() :
    # time.sleep(4)
    await asyncio.sleep(4)
    print("Function 3")

async def main() :
    L = await asyncio.gather(func1(),func2(),func3())

print(L)