from asyncio import Future

my_future = Future()

print(f"Is my future done ? {my_future.done()}")

my_future.set_result(42)

print(f"Is my future done ? {my_future.done()}")

print(f"What is the result of my future ? {my_future.result()}")
