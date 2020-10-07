#!/usr/bin/env python3
"""
Author : mario <mario@localhost>
Date   : 2020-10-06
Purpose: Crow's nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow''s nest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('name',
                        metavar='str',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main"""

    args = get_args()
    name = args.name
    article = 'an' if name[0].lower() in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {article} {name} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
