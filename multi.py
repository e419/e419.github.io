#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Reading file with main thread """

import os
import sys
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

def main():
    parser = argparse.ArgumentParser(description='Producers/consumers')
    parser.add_argument('--threads', help='Number of threads', default=4, type=int)
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

    lock = multiprocessing.Lock()

    def worker():
        """ Worker thread to filter data """
        while True:
            item = queue.get()
            with lock:
                if item.isupper():
                    with open(args.target, 'a') as dst_file:
                        dst_file.write(item)
            queue.task_done()

    for idx in range(args.threads):
        thread = threading.Thread(target=worker)
        thread.daemon = True
        thread.start()
    with file(source_file_path, 'r') as source_file:
        for line in source_file:
            queue.put(line)
    queue.join()

if __name__ == "__main__":
    main()
