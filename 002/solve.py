#!/usr/bin/env python

def test(str1, str2):
    print(''.join(i + j for i, j in zip(str1, str2)))


if __name__ == '__main__':
    test('パトカー', 'タクシー')
