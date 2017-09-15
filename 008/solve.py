#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def cipher(message):
    lowerReg = re.compile(r'^[a-z]+$')
    ciphered_message = ''.join(map(lambda x: chr(219 - ord(x)) if lowerReg.match(x) else x, message))
    return ciphered_message


if __name__ == '__main__':
    print(cipher('asdf1234ASDF!@#$'))
