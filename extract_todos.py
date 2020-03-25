#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# TODO: Use pathlib instead of os.path and os.listdir()
import os
import re

import pandas as pd
from tabulate import tabulate


OUTPUT_FILE = 'todos.csv'
SEARCH_FOR  = '# TODO'


def _validate_filepath(parser, arg):
    if not os.path.exists(arg):
        parser.error('The file path {} does not exist!'.format(arg))
    else:
        return arg


def extract_info(filepath, line_num, line):
    line = line.strip()
    _, tag, task = line.split(': ')
    tag = tag.strip()
    task = task.strip()
    filename = os.path.basename(filepath)
    return filename, line_num, tag, task


def create_table(data):
    df = pd.DataFrame(data=data, columns=['file', 'line', 'tag', 'task'])
    df = df.sort_values(by=['file', 'tag', 'line'], ascending=[True, False, True])
    table = tabulate(df, headers='keys', showindex=False)
    return table


def export_table(table, filepath):
    with open(filepath, 'w') as outfile:
        outfile.write(table)


def crawl_files(filepaths):
    results = []
    for fp in filepaths:
        print(f'  --> {fp}')
        with open(fp) as f:
            for num, line in enumerate(f):
                if SEARCH_FOR in line:
                    info = extract_info(fp, num, line)
                    results.append(info)
    return results


if __name__ == "__main__":
    import argparse
    import subprocess

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="input_dir", required=True,
                        help="path of the directory to crawl", metavar="DIRECTORY",
                        type=lambda x: _validate_filepath(parser, x))
    parser.add_argument("-o", dest="output_filepath", required=True,
                        help="path of output file", metavar="FILE")
    parser.add_argument("-cmd", dest="open_command", required=False,
                        help="command to open file from terminal", metavar="COMMAND")

    args = parser.parse_args()
    input_dir = os.path.abspath(args.input_dir)
    output_filepath = os.path.abspath(args.output_filepath)
    open_with = args.open_command

    print(f'{input_dir} --> {output_filepath}')

    py_files = [os.path.abspath(f) for f in os.listdir(input_dir) if f.endswith('.py') and f != os.path.basename(__file__)]
    results = crawl_files(py_files)
    table = create_table(results)
    export_table(table, output_filepath)

    if open_with:
        print(f'Opening output file (`{open_with} {output_filepath}`) ...')
        subprocess.check_call([open_with, output_filepath])

    print('Done.')
