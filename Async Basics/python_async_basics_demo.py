import asyncio
import time

async def fetch_data(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")

async def main():
    start = time.time()

    await asyncio.gather(
        fetch_data("Task A", 2),
        fetch_data("Task B", 2)
    )

    print(f"Total time: {time.time() - start:.2f}s")

asyncio.run(main())
