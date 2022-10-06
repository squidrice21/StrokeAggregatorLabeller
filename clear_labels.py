#!/usr/bin/env python

import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('input', help='Input data yml list')
    parser.add_argument('-o', '--output', help='output path')
    parser.add_argument('--debug', action='store_true',
                        help='place a breakpoint before execution')
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    scap_lines = ''
    with open(args.input, 'rt') as scap_f:
        scap_lines = scap_f.read()

    scap_lines = scap_lines.split('\n')
    seen_group = False
    for j in range(len(scap_lines)):
        if '{' in scap_lines[j]:
            seen_group = True
        if seen_group and '#' in scap_lines[j]:
            numbers = [s for s in scap_lines[j].split('\t') if len(s) > 0]
            assert len(numbers) == 2
            for i in range(len(numbers)):
                if '#' not in numbers[i]:
                    numbers[i] = '-1'
            scap_lines[j] = '\t{}\t{}'.format(numbers[0], numbers[1])

    with open(args.output, 'wt') as outf:
        outf.write('\n'.join(scap_lines))

if __name__ == '__main__':
    main()
