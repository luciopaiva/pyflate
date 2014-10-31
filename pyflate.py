"""
Test simple raw data inflate

Thanks to http://stackoverflow.com/questions/1089662/python-inflate-and-deflate-implementations
"""

import getopt
import zlib
import sys


def inflate(data):
    result = zlib.decompress(data, -zlib.MAX_WBITS)
    print(result)


def open_file(filename):
    with open(filename, 'rb') as f:
        b = f.read()
        print('File has {} bytes'.format(len(b)))
        inflate(b)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], '')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)

    if not args:
        print('Input file was not specified')
        sys.exit(1)

    open_file(args[0])


if __name__ == '__main__':
    main()
