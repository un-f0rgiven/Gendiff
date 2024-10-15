import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish', help='set format of output'
    )
    args = parser.parse_args()
    diffs = generate_diff(
        args.first_file, args.second_file, format_name=args.format
    )

    print(diffs)


if __name__ == '__main__':
    main()
