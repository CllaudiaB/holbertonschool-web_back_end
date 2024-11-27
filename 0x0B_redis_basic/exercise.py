#!/usr/bin/env python3
"""Redis exercices"""
import redis
from typing import Callable, Optional, Union
import uuid
import functools


def count_calls(method: Callable) -> Callable:
    """Count how many times a method has been called"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Storing lists"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper"""
        name = method.__qualname__
        self._redis.rpush(name + ":inputs", str(args))
        outputs = method(self, *args, **kwargs)
        self._redis.rpush(name + ':outputs', outputs)
        return outputs
    return wrapper


def replay(method: Callable) -> Callable:
    """Display the history of calls of a particular function"""
    cls = method.__self__
    number_call = cls.get(method.__qualname__)

    print(f"{method.__qualname__} was called {int(number_call)} times:")

    inputs = cls._redis.lrange(
        "{}:inputs".format(cls.store.__qualname__), 0, -1
    )
    outputs = cls._redis.lrange(
        "{}:outputs".format(cls.store.__qualname__), 0, -1
    )

    for _input, output in zip(inputs, outputs):
        print(
            f"{method.__qualname__}(*{_input.decode('utf-8')}) -> "
            f"{output.decode('utf-8')}"
        )


class Cache:
    """Cache"""
    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """Get value"""
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Convert str"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Convert int"""
        return self.get(key, lambda x: int(x.decode('utf-8')))
