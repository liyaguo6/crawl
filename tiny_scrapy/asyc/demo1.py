import asyncio

################创建协程函数#################
# async def test1():
#     print("1")
#     print("2")
#
#
# async def test2():
#     print("3")
#     print("4")
#
#
# print(test1())
# print(test2())


################执行协程函数###################

#
# async def test1():
#     print("1")
#     print("2")
#
#
# async def test2():
#     print("3")
#     print("4")
#
#
# a = test1()
# b = test2()
# try:
#     a.send(None)
# except StopIteration as e:
#     print(e)
#
# try:
#     b.send(None)
# except StopIteration as e:
#     print(e)


###################交叉执行协程函数（await）#################

# async def test1():
#     print("1")
#     await asyncio.sleep(1) # asyncio.sleep(1)返回的也是一个协程对象
#     print("2")
#
# async def test2():
#     print("3")
#     print("4")
#
# a = test1()
# b = test2()
#
# try:
#     a.send(None) # 可以通过调用 send 方法，执行协程函数
# except StopIteration:
#     pass  # 协程函数执行结束时会抛出一个StopIteration 异常，标志着协程函数执行结束
#
#
# try:
#     b.send(None) # 可以通过调用 send 方法，执行协程函数
# except StopIteration:
#     pass


######################自动循环执行协程函数######################

# async def test1():
#     print("1")
#     await test2()
#     print("2")
#
# async def test2():
#     print("3")
#     print("4")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test1())


###############调用task的result方法获取返回值。############3


# async def test1():
#     print("1")
#     await test2()
#     print("2")
#     await test2()
#     return "stop"
#
# async def test2():
#     print("3")
#     print("4")
#
#
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(test1())
# loop.run_until_complete(task)
# print(task.result())

###############返回值获取第二种方法：回调函数############3

# async def test1():
#     print("1")
#     await test2()
#     print("2")
#     await test2()
#     return "stop"
#
# async def test2():
#     print("3")
#     print("4")
#
# def callback(future):
#     print('Callback:',future.result())
#
#
#
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(test1())
# task.add_done_callback(callback)
# loop.run_until_complete(task)


import asyncio

import functools


async def test1():
    print("1")
    await test2()
    print("2")
    return "stop"


async def test2():
    print("3")
    print("4")


def callback(param1, param2, future):
    print(param1, param2)
    print('Callback:', future.result())


loop = asyncio.get_event_loop()

task = asyncio.ensure_future(test1())

task.add_done_callback(functools.partial(callback, "param1", "param2"))

loop.run_until_complete(task)
