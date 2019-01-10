# coding: utf-8
"""
随手库，把平时常用的一些函数直接塞到这个包里面。
"""

from . import img
from . import sta

__all__ = [
        'img',
        'sta',
        'run',
        'second',
        ]


def run():
    """
    测试 docstring.
    """
    pass


def second(a):
    """
    第二个函数，来个参数
    """

    pass


def main():
    print('installed successfully.')
    pass


if __name__ == '__main__':
    main()
