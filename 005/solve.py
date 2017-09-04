#!/usr/bin/env python

def ngram(stream, n):
    lst = []
    for i in range(len(stream) - (n - 1)):
        lst.append(stream[i:i+n:])

    print(lst)


def ngram_by_mode(stream, n, mode):
    if mode == 'char':
        ngram(stream.replace(',', '').replace('.', '').replace(' ', ''), n)
    elif mode == 'word':
        ngram(stream.replace(',', '').replace('.', '').split(' '), n)


if __name__ == '__main__':
    ngram_by_mode('I am an NLPer', 2, 'char')
    ngram_by_mode('I am an NLPer', 2, 'word')
