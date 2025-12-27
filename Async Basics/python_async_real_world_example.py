"""
python_async_real_world_example.py
=================================

Real-world async example:
-------------------------
Simulate a backend service that:
- Calls multiple external APIs
- Each API call is slow (network delay)
- Async allows all calls to run concurrently

This pattern is used in:
- FastAPI
- Microservices
- Data ingestion systems
- ML feature fetching

Author: Anupam Bhattacharyya
"""

import asyncio
import time


# ============================================================
# PART 1 — SYNCHRONOUS (BLOCKING) VERSION
# ============================================================

def fetch_user_sync(user_id):
    """Simulate slow API call"""
    print(f"[SYNC] Fetching user {user_id}")
    time.sleep(2)  # blocking
    return {"id": user_id, "name": f"User{user_id}"}


def sync_main():
    start = time.time()

    users = []
    users.append(fetch_user_sync(1))
    users.append(fetch_user_sync(2))
    users.append(fetch_user_sync(3))

    print("[SYNC] Result:", users)
    print(f"[SYNC] Total time: {time.time() - start:.2f}s")


# ============================================================
# PART 2 — ASYNC (NON-BLOCKING) VERSION
# ============================================================

async def fetch_user_async(user_id):
    """Simulate async API call"""
    print(f"[ASYNC] Fetching user {user_id}")
    await asyncio.sleep(2)  # non-blocking
    return {"id": user_id, "name": f"User{user_id}"}


async def async_main():
    start = time.time()

    users = await asyncio.gather(
        fetch_user_async(1),
        fetch_user_async(2),
        fetch_user_async(3)
    )

    print("[ASYNC] Result:", users)
    print(f"[ASYNC] Total time: {time.time() - start:.2f}s")


# ============================================================
# PART 3 — REAL BACKEND-STYLE SERVICE
# ============================================================

async def get_user_profile(user_id):
    """
    Simulates a real service endpoint:
    - Fetch user
    - Fetch orders
    - Fetch recommendations
    """

    async def fetch_orders():
        await asyncio.sleep(1.5)
        return ["order1", "order2"]

    async def fetch_recommendations():
        await asyncio.sleep(1)
        return ["itemA", "itemB"]

    user_task = fetch_user_async(user_id)
    orders_task = fetch_orders()
    recommendations_task = fetch_recommendations()

    user, orders, recommendations = await asyncio.gather(
        user_task,
        orders_task,
        recommendations_task
    )

    return {
        "user": user,
        "orders": orders,
        "recommendations": recommendations
    }


async def service_main():
    start = time.time()
    profile = await get_user_profile(10)
    print("[SERVICE] User profile:", profile)
    print(f"[SERVICE] Total time: {time.time() - start:.2f}s")


# ============================================================
# RUN SECTION
# ============================================================

if __name__ == "__main__":

    print("\n================ SYNC VERSION ================\n")
    sync_main()

    print("\n================ ASYNC VERSION ================\n")
    asyncio.run(async_main())

    print("\n=========== REAL SERVICE EXAMPLE ==============\n")
    asyncio.run(service_main())
