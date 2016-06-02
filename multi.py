#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Reading file with main thread """

import os
import Queue
import random
import argparse
import threading
import multiprocessing


def _dummy():
    """ Generate sample file """
    variations = ['A', 'b', ' ']
    with open('alice.txt', 'a') as dst_file:
        dst_file.write(random.choice(variations) + '\n')


lock = multiprocessing.Lock()


def worker():
    """ Worker thread to filter data """ 
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

    queue = Queue.Queue()
    for i in range(args.threads):
        print i
        
    with file(source_file_path, 'r') as source_file:
        for line in source_file:
            print line
        


if __name__ == "__main__":
    main()
