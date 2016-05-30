#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Python meta """


class A(object):
    phrase = 'Test'

    def test(self):
        print self.phrase


class Proxy(object):

    def __init__(self, target):
        self.target = target

def main():
    proxy = Proxy(A())
    proxy.phrase = 'Hello World!'
    proxy.test()

if __name__ == "__main__":
    main()
    
