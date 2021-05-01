import os
import sys
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Outputs the contents of a file.')

    parser.add_argument('file', type=str,
                        help='the file to be printed in console')
    parser.add_argument('-e', '--encoding', type=str,
                        default='ascii', nargs='?',
                        help='the encoding in which to read the file')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.file is None:
        print('There is no path to file in arguments!')
        sys.exit(1)
    if not os.path.exists(args.file):
        print(f'There is no such file: {os.path.abspath(args.file)}!')
        sys.exit(2)
    if not os.path.isfile(args.file):
        print(f'There is not a file: {os.path.abspath(args.file)}!')
        sys.exit(3)

    try:
        chr(30).encode(encoding=args.encoding)
    except LookupError:
        print(f'Incorrect encoding: {args.encoding}!')
        sys.exit(4)

    if os.path.getsize(args.file) == 0:
        print(f'File is emtpy!')
        sys.exit(0)

    try:
        open(args.file, mode='r')
    except PermissionError:
        print(f'Permission denied: {args.file}!\n'
              f'Restart the program as a root.')
        sys.exit(5)

    with open(args.file, encoding=args.encoding) as file:
        try:
            for line in file.readlines():
                print(line, end='')
            print()
        except UnicodeDecodeError:
            print(f'Can not decode bytes in file: {args.file}!')
            sys.exit(6)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
