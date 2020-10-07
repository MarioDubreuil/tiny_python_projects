#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    args = parser.parse_args()
    name = args.name
    print("Hello, " + name + "!")

if __name__ == '__main__':
    main()
