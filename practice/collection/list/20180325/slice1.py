#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


if __name__ == '__main__':
    a = ['a', 'b', 'c', 'd', 'e']

    # 切片起止索引越界不会出问题
    first_20_items = a[: 20]
    print(first_20_items)   # ['a', 'b', 'c', 'd', 'e']
    last_20_items = a[-20:]
    print(last_20_items)    # ['a', 'b', 'c', 'd', 'e']

    # 访问单个元素时，下标不能越界
    try:
        print(a[20])
    except Exception as e:
        print(e.__class__, e)
        # < type 'exceptions.IndexError' >
        # IndexError('list index out of range', )

    # 对切片内容赋值，会自动扩张或收缩原列表
    a[2:4] = [1, 2, 3, 4]
    print(a)   # ['a', 'b', 1, 2, 3, 4, 'e']

    # 对原列表进行拷贝
    b = a[:]
    print(b == a)  # True
    print(b is a)   # False

    # 增加新的引用
    a = ['a', 'b', 'c', 'd', 'e']
    b = a
    a[2: 4] = [1, 2, 3, 4]
    print(b)    # ['a', 'b', 1, 2, 3, 4, 'e']
    print(b is a)   # True
