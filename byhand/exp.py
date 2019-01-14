# coding: utf-8

"""
測試特性
"""


def test(a, b, *params, **kwargs):
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'params: {params}')
    print(f'kwargs: {kwargs}')


def dev(level='stable'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


if __name__ == "__main__":
    test(1, 2, 3, c=4, d=5)