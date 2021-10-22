import pandas as pd
import os
from pprint import pprint


def load_file(file_name):
    pass


def data_processing():
    pass


def combine_txt_files_to_csv(txt_file_list):
    pass


def _sort(file_name):
    file_name = file_name.split('/')[-1]
    file_name = file_name.replace('.txt', '')
    file_name = file_name.replace('_', '')
    return int(file_name)


if __name__ == '__main__':
    prefix = 'ICS_OEE'
    subfiles = os.listdir(f'{prefix}')
    subfiles = [f'{prefix}/{file}' for file in subfiles]
    folders = [file for file in subfiles if os.path.isdir(file)]

    for folder in folders:
        txt_files = os.listdir(f'{folder}')
        txt_files = sorted(txt_files, key=_sort)
        txt_files = [f'{folder}/{txt_file}' for txt_file in txt_files]
        print('-----------------------------')
        print(f'folder: {folder}')
        print(txt_files)
    # file = ''
    # load_file(file)
    # data_processing()
