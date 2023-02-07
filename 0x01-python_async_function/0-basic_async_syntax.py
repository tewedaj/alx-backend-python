#!/usr/bin/env python3
""" 0th task """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """await data for random amount of time and
        also make stuff happen
    """

    random_val = random.uniform(0, max_delay)
    await asyncio.sleep(random_val)
    return random_val
