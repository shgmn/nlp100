#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ngram(stream, n):
    lst = []
    for i in range(len(stream) - (n - 1)):
        lst.append(stream[i:i+n:])

    return set(lst)


def ngram_by_mode(stream, n, mode):
    if mode == 'char':
        return ngram(stream.replace(',', '').replace('.', '').replace(' ', ''), n)
    elif mode == 'word':
        return ngram(stream.replace(',', '').replace('.', '').split(' '), n)


if __name__ == '__main__':
    x = ngram_by_mode('paraparaparadise', 2, 'char')
    y = ngram_by_mode('paragraph', 2, 'char')
    print(x)
    print(y)

    print(x.union(y)) # 和集合 x|y
    print(x.intersection(y)) # 積集合 x&y
    print(x.difference(y)) # 差集合 x-y

    x_message = "含まれる" if 'se' in x else "含まれない"
    print("'se'はxに" + x_message)

    y_message = "含まれる" if 'se' in y else "含まれない"
    print("'se'はyに" + y_message)
