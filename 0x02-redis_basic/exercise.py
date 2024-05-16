#!/usr/bin/env python3
""" Redis basic """

import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count_calls function """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ call_history function """
    inkey = method.__qualname__ + ":inputs"
    outkey = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        self._redis.rpush(inkey, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(outkey, str(res))
        return res

    return wrapper

class Cache:
    def __init__(self):
        """ init function """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store function """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: Optional[Callable] = None) -> UnionOfTypes:
        """ get function """
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val


    def get_str(self, key: str) -> str:
        """ get_str function """
        return self.get(key, fn=str)


    def get_int(self, key: str) -> int:
        """ get_int function """
        return self.get(key, fn=int)
