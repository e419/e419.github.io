#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict


""" Python meta """


class A(object):
    phrase = 'Test'

    def test(self):
        print self.phrase


class Proxy(object):

    def __init__(self, target):
        super(Proxy, self).__setattr__('target', target)
        super(Proxy, self).__setattr__('calls', defaultdict(lambda: 0))

    def __getattr__(self, name):
        return getattr(self.target, name)

    def __setattr__(self, name, value):
        self.calls[name] += 1
        setattr(self.target, name, value)

    def __str__(self):
        return str(self.calls)
    
def main():
    proxy = Proxy(A())
    proxy.phrase = 'Hello World!'
    proxy.sdfa = 1
    proxy.test()
    print str(proxy.phrase)

if __name__ == "__main__":
    main()
    
