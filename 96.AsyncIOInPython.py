# In this class we shall learn about AsyncIO in Python.


import asyncio



# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching Data...")
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print("Data fetched")
    return {"data": "https://www.google.com"} # Return some data


# Define another coroutine that calls the first coroutine
async def main() :
    print("Start of the main coroutine")
    task = fetch_data(2)
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await task
    print(f"Recieved result: {result}")
    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())

# Similarly, in this example we have created two tasks to run asyncronously that have the task of fetching some data from the web.

async def data(delay,id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay)
    print("Data fetched, id:", id)
    return {"data":"https://www.youtube.com"}

async def man():
    print("Starting the main coroutine.")
    task1 = data(2,1)
    task2 = data(2,2)
    result1 = await task1
    print(f"Recieved data:{result1}")
    result2 = await task2
    print(f"Recieved data:{result2}")

asyncio.run(man())

# create_task function : Makes it much easier, it help us run a another easy task whenever a task is delayed or haulted.
async def  fetching_data(id,sleep_time) :
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id":id, "data":f"Sample data from coroutine {id}"}

async def main_function():
    # Create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetching_data(1,2))
    task2 = asyncio.create_task(fetching_data(2,3))
    task3 = asyncio.create_task(fetching_data(3, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1,result2,result3)

asyncio.run(main_function())


# gather function : Gather function is a quick way to concurrently run multiple coroutines.

async def fetches_data(id , sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) # Simulate a network request or IO operation
    # Return some data as a result
    return {"id":id,"data":f"Sample data from coroutine {id}"}

async def mas_main():
    # Run coroutines concurrently and gather their return values
    results = await asyncio.gather(fetches_data(1,2),fetches_data(2,1),fetches_data(3,3))

    # Process the results
    for result in results :
        print(f"Recieved result: {result}")
# Run the main coroutine
asyncio.run(mas_main())


# TaskGroup function : More prefered function to create multiple tasks and organise them together as it also provides Built-in Error Handling.

async def fetcha_data(id,sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) # Simulate a network request or IO operation
    return {"id":id , "data":f"Sample data from coroutine {id}"}

async def main_main():
    tasks = []
    async with asyncio.TaskGroup() as tg :
        for id_index , sleep_time in enumerate([2, 1, 3], start = 1) :
            task = tg.create_task(fetcha_data(id_index, sleep_time))
            tasks.append(task)
# After the Task Group block all tasks have completed
    results = [task.result() for task in tasks]
    for result in results :
        print(f"Recieved result: {result}")

asyncio.run(main_main())


# Concept of Future :
async def set_future_result(future, value):
    await asyncio.sleep(2)
    # Set the result of the future
    future.set_result(value)
    print(f"Set the future's result to: {value}")

async def maon():
    # Create a future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # Schedule setting the future's result
    asyncio.create_task(set_future_result(future,"Future result is ready"))

    # Wait for the future's result
    result = await future
    print(f"Recieved the future's result:{result}")
asyncio.run(maon())

# Syncronization :

# A shared variable
shared_resource = 0
# An asyncio lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock :
        # Critical section starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource = shared_resource + 1 # Modify the shared_resource
        await asyncio.sleep(1) # Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        # Critical section ends

async def maan():
    await asyncio.gather(*(modify_shared_resource() for i in range(5)))

asyncio.run(maan())


# Semaphore Synchronization :
async def access_resource(semaphore, resource_id):
    async with semaphore :
        # Simulate accessing a limited resource
        print(f"Accessing resource {resource_id}")
        await asyncio.sleep(1) # Simulate work with the resource
        print(f"Releasing resource {resource_id}")

async def maam():
    semaphore = asyncio.Semaphore(2) # Allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore,i) for i in range(5)))

asyncio.run(maam())

# Event Synchronization : Allows us to do simpler synchronization.

async def waiter(event):
    print("Waiting for the next event to be set.")
    await event.wait()
    print("Event has been set, continuing execution")
async def setter(event):
    await asyncio.sleep(2) # Simulate doing some work
    event.set()
    print("Event has been set!")
async def maain():
    event = asyncio.Event()
    await asyncio.gather(waiter(event),setter(event))

asyncio.run(maain())

# These are all about asyncio in python. You will learn it more deep and proper while you code some actual
# problems and projects.


