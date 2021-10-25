import os
import time
import pandas as pd
from pprint import pprint
start = time.time()

path = 'ICS_OEE/2F_T#17/20210723_005155.txt'


def _sort(filename):
    filename = filename.replace('.txt', '')
    filename = filename.replace('_', '')
    return int(filename)


def get_files(prefix_path):
    txt_files = os.listdir(f'{prefix_path}')
    txt_files = sorted(txt_files, key=_sort)
    txt_files = [f'{prefix_path}' + txt_file for txt_file in txt_files]
    return txt_files


def combine_all_txt_files(txt_files):
    col1 = list()
    col2 = list()
    col3 = list()
    col4 = list()
    col5 = list()
    col6 = list()
    col7 = list()

    for txt_file in txt_files:
        with open(txt_file, 'r') as fp:
            lines = fp.readlines()
        line = lines[0]
        line = line.split(',')
        line[-1] = line[-1].replace('\n', '')
        col1.append(line[0])
        col2.append(line[1])
        col3.append(line[2])
        col4.append(line[3])
        col5.append(line[4])
        col6.append(line[5])
        col7.append(line[6])

    _dict = {
        '1': col1,
        '2': col2,
        '3': col3,
        '4': col4,
        '5': col5,
        '6': col6,
        '7': col7,
    }
    df = pd.DataFrame(_dict)
    df.to_csv(f'{prefix_path.split("/")[1]}.csv', index=False)


if __name__ == "__main__":
    prefix_path = 'ICS_OEE/2F_T#17/'
    txt_files = get_files(prefix_path)
    combine_all_txt_files(txt_files=txt_files)

    # ------------------------------------------------
    print(f'總執行時間{time.time() - start}秒')
