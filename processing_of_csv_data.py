import glob

from combine_txt_to_csv import *
import pandas as pd
from datetime import datetime

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


def init_dataframe():
    _dict = {
        'Machine_Name': [],
        'Machine_Status': [],
        'Start_Dttm': [],
        'End_Dttm': [],
        'Duration': [],
        'Error_Code': [],
        'Stop_Reason': []
    }
    return _dict


def time_delta(time1, time2):
    # time2 > time1
    time_delta = datetime.strptime(time2, DATE_FORMAT) - datetime.strptime(time1, DATE_FORMAT)
    time_delta = time_delta.total_seconds()
    return time_delta


def policy(csv_file, data_dict):
    df = pd.read_csv(csv_file)
    for i in range(len(df)):
        try:
            if i > 1:
                print(i)
                if df.loc[i, '5'] == RUNNING \
                        and df.loc[i - 1, '5'] == READY \
                        and df.loc[i - 2, '5'] == NORMALCLEANING:
                    data_dict['Machine_Status'] += ['Stop', 'Stop']
                    data_dict['Start_Dttm'] += [df.loc[i - 2, '1'], df.loc[i - 1, '1']]
                    data_dict['End_Dttm'] += [df.loc[i, '1'], df.loc[i - 1, '1']]
                    data_dict['Duration'] += [time_delta(df.loc[i - 2, '1'], df.loc[i - 1, '1']),
                                              time_delta(df.loc[i - 1, '1'], df.loc[i, '1'])]
                    data_dict['Error_Code'] += ['N.A', 'N.A']
                    data_dict['Stop_Reason'] += ['NORMALCLEANING', 'MA Waiting']
                elif df.loc[i, '5'] == RUNNING \
                        and df.loc[i - 1, '5'] == READY \
                        and df.loc[i - 2, '5'] == RUNNING:
                    data_dict['Machine_Status'].append('Stop')
                    data_dict['Start_Dttm'].append(df.loc[i - 1, '1'])
                    data_dict['End_Dttm'].append(df.loc[i, '1'])
                    data_dict['Duration'].append(time_delta(df.loc[i - 1, '1'], df.loc[i, '1']))
                    data_dict['Error_Code'].append('N.A')
                    data_dict['Stop_Reason'].append('Pending load')
                elif df.loc[i, '5'] == RUNNING \
                        and df.loc[i - 1, '5'] == ERROR \
                        and df.loc[i - 2, '5'] == RUNNING \
                        and df.loc[i - 3, '5'] == READY \
                        and df.loc[i - 1, '8'] == 2041 \
                        and df.loc[i - 1, '10'] == 'TABCLOG':
                    data_dict['Machine_Status'] += ['Run', 'Stop']
                    data_dict['Start_Dttm'] += [df.loc[i - 2, '1'], df.loc[i - 1, '1']]
                    data_dict['End_Dttm'] += [df.loc[i, '1'], df.loc[i - 1, '1']]
                    data_dict['Duration'] += [time_delta(df.loc[i - 2, '1'], df.loc[i - 1, '1']),
                                              time_delta(df.loc[i - 1, '1'], df.loc[i, '1'])]
                    data_dict['Error_Code'] += ['N.A', '2041']
                    data_dict['Stop_Reason'] += ['N.A', 'TABCLOG']
                elif df.loc[i, '5'] == RUNNING \
                        and df.loc[i - 1, '5'] == READY \
                        and df.loc[i - 2, '5'] == ERROR \
                        and df.loc[i - 3, '5'] == RUNNING \
                        and df.loc[i - 4, '5'] == READY \
                        and df.loc[i - 2, '8'] == 2041 \
                        and df.loc[i - 2, '10'] == 'TABCLOG':
                    data_dict['Machine_Status'] += ['Run', 'Stop']
                    data_dict['Start_Dttm'] += [df.loc[i - 3, '1'], df.loc[i - 2, '1']]
                    data_dict['End_Dttm'] += [df.loc[i - 2, '1'], df.loc[i, '1']]
                    data_dict['Duration'] += [time_delta(df.loc[i - 3, '1'], df.loc[i - 2, '1']),
                                              time_delta(df.loc[i - 2, '1'], df.loc[i, '1'])]
                    data_dict['Error_Code'] += ['N.A', '2041']
                    data_dict['Stop_Reason'] += ['N.A', 'TABCLOG']
                elif df.loc[i, '5'] == RUNNING \
                        and df.loc[i - 1, '5'] == NORMALCLEANING \
                        and df.loc[i - 2, '5'] == SHEETCLEANING \
                        and df.loc[i - 3, '5'] == SHEETCLEANING \
                        and df.loc[i - 4, '5'] == SHEETCLEANING \
                        and df.loc[i - 2, '8'] == 2041 \
                        and df.loc[i - 2, '10'] == 'TABCLOG':
                    data_dict['Machine_Status'].append('Stop')
                    data_dict['Start_Dttm'].append(df.loc[i - 4, '1'])
                    data_dict['End_Dttm'].append(df.loc[i, '1'])
                    data_dict['Duration'].append(time_delta(df.loc[i - 4, '1'], df.loc[i, '1']))
                    data_dict['Error_Code'].append('N.A')
                    data_dict['Stop_Reason'].append('CLEANING')
                elif df.loc[i, '5'] == RUNNING \
                        and df.loc[i - 1, '5'] == READY \
                        and df.loc[i - 2, '5'] == ERROR \
                        and df.loc[i - 3, '5'] == ERROR \
                        and df.loc[i - 4, '5'] == RUNNING \
                        and df.loc[i - 5, '5'] == READY \
                        and df.loc[i - 2, '5'] == 2024 \
                        and df.loc[i - 3, '5'] == 2023 \
                        and df.loc[i - 2, '10'] == TABSHOOT \
                        and df.loc[i - 3, '10'] == TABPUSHER:
                    data_dict['Machine_Status'] += ['Run', 'Stop']
                    data_dict['Start_Dttm'] += [df.loc[i - 4, '1'], df.loc[i - 3, '1']]
                    data_dict['End_Dttm'] += [df.loc[i - 3, '1'], df.loc[i, '1']]
                    data_dict['Duration'] += [time_delta(df.loc[i - 4, '1'], df.loc[i - 3, '1']),
                                              time_delta(df.loc[i - 3, '1'], df.loc[i, '1'])]
                    data_dict['Error_Code'] += ['N.A', '2023']
                    data_dict['Stop_Reason'] += ['N.A', TABPUSHER]
                elif df.loc[i, '5'] == READY \
                        and df.loc[i - 1, '5'] == IDLE_STOP \
                        and df.loc[i - 2, '5'] == RUNNING \
                        and df.loc[i - 3, '5'] == RUNNING \
                        and df.loc[i - 4, '5'] == RUNNING \
                        and df.loc[i - 5, '5'] == RUNNING \
                        and df.loc[i - 6, '5'] == READY:
                    data_dict['Machine_Status'] += ['Run', 'Stop']
                    data_dict['Start_Dttm'] += [df.loc[i - 5, '1'], df.loc[i - 1, '1']]
                    data_dict['End_Dttm'] += [df.loc[i - 1, '1'], df.loc[i, '1']]
                    data_dict['Duration'] += [time_delta(df.loc[i - 5, '1'], df.loc[i - 1, '1']),
                                              time_delta(df.loc[i - 1, '1'], df.loc[i, '1'])]
                    data_dict['Error_Code'] += ['N.A', 'N.A']
                    data_dict['Stop_Reason'] += ['N.A', 'MA Waiting']
                elif df.loc[i, '5'] == RUNNING \
                        and df.loc[i - 1, '5'] == READY \
                        and df.loc[i - 2, '5'] == NORMALCLEANING \
                        and df.loc[i - 3, '5'] == NORMALCLEANING \
                        and df.loc[i - 4, '5'] == SHEETCLEANING \
                        and df.loc[i - 5, '5'] == NORMALCLEANING \
                        and df.loc[i - 6, '5'] == NORMALCLEANING \
                        and df.loc[i - 7, '5'] == NORMALCLEANING:
                    data_dict['Machine_Status'] += ['Stop', 'Stop']
                    data_dict['Start_Dttm'] += [df.loc[i - 5, '1'], df.loc[i - 1, '1']]
                    data_dict['End_Dttm'] += [df.loc[i - 1, '1'], df.loc[i, '1']]
                    data_dict['Duration'] += [time_delta(df.loc[i - 7, '1'], df.loc[i - 1, '1']),
                                              time_delta(df.loc[i - 1, '1'], df.loc[i, '1'])]
                    data_dict['Error_Code'] += ['N.A', SHEETCLEANING]
                    data_dict['Stop_Reason'] += ['N.A', 'MA Waiting']
        except:
            pass
    return data_dict


def main():
    prefix_paths = glob.glob('ICS_OEE/*/')
    for prefix_path in prefix_paths:
        txt_files = get_files(prefix_path)
        combine_all_txt_files(txt_files, prefix_path)

    csv_files = glob.glob('*.csv')

    for csv_file in csv_files:
        print(csv_file)
        _dict = init_dataframe()
        data_dict = policy(csv_file, _dict)
        n = len(data_dict.get('Machine_Status'))
        data_dict['Machine_Name'] = [csv_file.split('.')[0] for _ in range(n)]

        df = pd.DataFrame(data_dict)
        df.to_csv(f"{csv_file}_after_convert.csv", index=False)

main()



