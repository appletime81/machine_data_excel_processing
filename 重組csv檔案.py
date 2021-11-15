import pandas as pd
from pprint import pprint
from datetime import datetime
import copy

RUNNING = 'RUNNING'
READY = 'READY'
ERROR = 'ERROR'
NORMALCLEANING = 'NORMALCLEANING'
IDLE_STOP = 'IDLE/STOP'
SHEETCLEANING = 'SHEETCLEANING'
STARTED = 'STARTED'
TABSHOOT = 'TABSHOOT'
TABPUSHER = 'TABPUSHER'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def rebuild_original_csv(csv_file):
    # 讀取原始資料
    df = pd.read_csv(csv_file)

    # 新建空pd.DataFrame
    column_names = list(df.columns)
    new_df_dict = dict([(column_name, list()) for column_name in column_names])
    new_df = pd.DataFrame(new_df_dict)

    # 篩選重組原始CSV檔
    running_dict = dict()
    error_dict = dict()
    ready_dict = dict()
    new_result_dict = dict()
    sorted_index_list = list()

    for i in range(len(df)):
        # RUNNING CASE
        if df.loc[i, '5'] == RUNNING:
            running_dict[i] = df.loc[i]
        elif df.loc[i, '5'] == ERROR:
            error_dict[i] = df.loc[i]
        elif df.loc[i, '5'] == READY:
            ready_dict[i] = df.loc[i]

    running_dict = clear_duplicates(running_dict)
    error_dict = clear_duplicates(error_dict)
    ready_dict = clear_duplicates(ready_dict)

    running_dict.update(error_dict)
    running_dict.update(ready_dict)
    result_dict = copy.deepcopy(running_dict)

    for k, v in result_dict.items():
        sorted_index_list.append(k)
    sorted_index_list = sorted(sorted_index_list)

    for index in sorted_index_list:
        new_result_dict[index] = result_dict.get(index)

    pprint(new_result_dict)

    for k, v in new_result_dict.items():
        new_df = new_df.append(v.to_dict(), ignore_index=True)
    pprint(new_df)
    new_df.to_csv('test.csv', index=False)


def clear_duplicates(dict_):
    new_dict = dict()
    index_list = list()
    new_index_list = list()

    for k, v in dict_.items():
        index_list.append(k)

    for i in range(len(index_list)):
        if i == 0:
            new_index_list.append(index_list[i])
        else:
            if index_list[i] != index_list[i - 1] + 1:
                new_index_list.append(index_list[i])

    for index in new_index_list:
        new_dict[index] = dict_.get(index)

    return new_dict


if __name__ == '__main__':
    cvf_file = '2F_T#24.csv'
    rebuild_original_csv(csv_file=cvf_file)
