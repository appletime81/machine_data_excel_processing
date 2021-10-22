import os
import pandas as pd
from pprint import pprint

path = 'ICS_OEE/2F_T#17/20210723_005155.txt'


def _sort(filename):
    filename = filename.replace('.txt', '')
    filename = filename.replace('_', '')
    return int(filename)


txt_files = os.listdir('ICS_OEE/2F_T#17/')
txt_files = sorted(txt_files, key=_sort)
txt_files = ['ICS_OEE/2F_T#17/' + txt_file for txt_file in txt_files]
pprint(txt_files)

col1 = list()
col2 = list()
col3 = list()
col4 = list()
col5 = list()
col6 = list()
col7 = list()

with open(path, 'r') as fp:
    lines = fp.readlines()

print(lines)

line = lines[0]
line = line.split(',')
line[-1] = line[-1].replace('\n', '')
print(line)
