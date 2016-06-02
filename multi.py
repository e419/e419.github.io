#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Reading file with main thread """

import os
import argparse
import threading
import Queue


def main():
    parser = argparse.ArgumentParser(description='Producers/consumers')
    parser.add_argument('--threads', help='Number of threads', default=2, type=int)
    parser.add_argument('--file', help='File to read', default='alice.txt', type=str)
    parser.add_argument('--file', help='File to read', default='alice.txt', type=str)
    args = parser.parse_args()
    if args.file and args.file is not 'alice.txt':
        source_file = args.file
        if not os.path.exists(source_file):
            print "No file to read. Please check:", source_file
            exit()
    else:
        source_file = args.file
    with file(source_file, 'r') as source:
        for line in source:
            print line
        


if __name__ == "__main__":
    main()
