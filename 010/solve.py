#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def wc(filename):
    f = open(filename, 'r')
    count = 0
    for line in f:
        count = count + 1
    return count


if __name__ == '__main__':
    params = sys.argv
    print(wc(params[1]))
