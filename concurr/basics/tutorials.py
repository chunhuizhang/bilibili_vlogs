
import asyncio
import time


# define a coroutine
# async def main():
#     print('hello coroutine!')
#
#
# # pause the execution of a coroutine
# async def main2():
#     await main()
#     print('continue execution')


async def display_time():
    start_time = time.time()
    while True:
        dur = int(time.time() - start_time)
        if dur % 3 == 0:
            print('{} seconds have passed.'.format(dur))
        await asyncio.sleep(1)


async def print_num():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def main():

    task1 = asyncio.ensure_future(display_time())
    task2 = asyncio.ensure_future(print_num())

    await asyncio.gather(task1, task2)

if __name__ == '__main__':

    # asyncio.run(main())
    ev_loop = asyncio.get_event_loop()

    ev_loop.run_until_complete(main())

    ev_loop.close()
