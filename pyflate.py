"""
Test simple raw data inflate

Thanks to http://stackoverflow.com/questions/1089662/python-inflate-and-deflate-implementations
"""

import getopt
import zlib
import sys


def inflate(data):
    return zlib.decompress(data)


def open_file(filename):
    with open(filename, 'rb') as f:
        b = f.read()
        return b


def parseargs():
    try:
        opts, args = getopt.getopt(sys.argv[1:], '')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)

    return args


def find_relevant_part(b):
    p = b.find(b'2933')
    if p != -1:
        return p + 42
    else:
        return p


def main():
    # args = parseargs()
    # if not args:
    #     print('Input PDF file was not specified')
    #     sys.exit(1)
    #
    # contents = open_file(args[0])

    contents = open_file('collier.pdf')

    print('File has {} bytes'.format(len(contents)))
    position = find_relevant_part(contents)
    print('Position in file: {} bytes from the start'.format(position))
    compressed = contents[position:position+2933]
    decompressed = inflate(compressed)
    print(decompressed)


if __name__ == '__main__':
    main()
