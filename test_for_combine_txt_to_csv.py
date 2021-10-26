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
    col_list = [list() for i in range(10)]

    for txt_file in txt_files:
        with open(txt_file, 'r') as fp:
            lines = fp.readlines()
        line = lines[0]
        line = line.split(',')
        line[-1] = line[-1].replace('\n', '')
        for i in range(10):
            try:
                col_list[i].append(line[i])
            except:
                col_list[i].append('')

    _dict = dict([(i+1, _list) for i, _list in enumerate(col_list)])
    print(_dict)
    for k, v in _dict.items():
        print(len(v))
    df = pd.DataFrame(_dict)
    df.to_csv(f'{prefix_path.split("/")[1]}.csv', index=False)


if __name__ == "__main__":
    prefix_path = 'ICS_OEE/4F_T#02/'
    txt_files = get_files(prefix_path)
    combine_all_txt_files(txt_files=txt_files)

    # ------------------------------------------------
    print(f'總執行時間{time.time() - start}秒')
