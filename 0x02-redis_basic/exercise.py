#!/usr/bin/env python3
""" Redis basic """

import uuid
import redis


class Cache:
    def __init__(self):
        """ init function """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: bytes | str | int | float) -> str:
        """ store function """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
