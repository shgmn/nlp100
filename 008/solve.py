#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cipher(message):
    ciphered_message = ''.join(map(lambda x: chr(219 - ord(x)) if x.islower() else x, message))
    return ciphered_message


if __name__ == '__main__':
    print(cipher('asdf1234ASDF!@#$'))
