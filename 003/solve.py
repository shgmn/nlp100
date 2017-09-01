#!/usr/bin/env python

def test(message):
    print(list(map(lambda x: len(x), message.replace('.', '').replace(',', '').split(' '))))


if __name__ == '__main__':
    test('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.')
