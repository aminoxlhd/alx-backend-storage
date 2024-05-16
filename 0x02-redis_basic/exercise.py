#!/usr/bin/env python3
""" Redis basic """

import uuid
import redis
from typing import Union, Callable, Optional


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
