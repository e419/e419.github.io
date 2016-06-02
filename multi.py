#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Reading file with main thread """

import os
import Queue
import argparse
import threading
import multiprocessing


lock = multiprocessing.Lock()


def worker():
    with lock:
        for _ in range(10):
            sys.stderr.write(i)
            time.sleep(1)


def main():
    parser = argparse.ArgumentParser(description='Producers/consumers')
    parser.add_argument('--threads', help='Number of threads', default=2, type=int)
    parser.add_argument('--source', help='File to read', default='alice.txt', type=str)
    parser.add_argument('--target', help='File to read', default='output.txt', type=str)
    args = parser.parse_args()
    if args.source and args.source is not 'alice.txt':
        source_file_path = args.source
        if not os.path.exists(source_file_path):
            print "No file to read. Please check:", source_file_path
            exit()
    else:
        source_file_path = args.source
    with file(source_file_path, 'r') as source_file:
        for line in source_file:
            print line
        


if __name__ == "__main__":
    main()
