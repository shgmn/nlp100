#!/usr/bin/env python

def test(message, indices):
    msglst = message.replace(',', '').replace('.', '').split(' ')
    inlst = list(map(lambda x: x-1, indices))
    dic = {}
    for i, message in enumerate(msglst):
        dic[i+1] = i in inlst and message[:1:] or message[:2:]

    print(dic.items())


if __name__ == '__main__':
    target_indices = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    test("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.", target_indices)
