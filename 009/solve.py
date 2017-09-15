#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def typoglycemia(message):
    shuffle = lambda x: ''.join(random.sample(x ,len(x)))
    result = ' '.join(map(lambda x: x[0] + shuffle(x[1:len(x)-1]) + x[-1] if len(x) > 4 else x, message.split(' ')))
    return result


if __name__ == '__main__':
    print(typoglycemia('I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'))
