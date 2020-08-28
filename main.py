import argparse
import sys

from csv_parser import parse


parser = argparse.ArgumentParser(description="Parse a csv to Python.")
parser.add_argument('input')
parser.add_argument('--file', action="count")
parser.add_argument('--output')

args = parser.parse_args()

if args.file: 
    with open(args.input, 'r', encoding='utf-8') as f:
        csv_data = f.read()
else:
    csv_data = args.input

python_list = parse(csv_data)

if args.output:
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(str(python_list))

print(python_list)
