import pandas as pd
import traceback

RUNNING = 'RUNNING'
READY = 'READY'
ERROR = 'ERROR'
NORMALCLEANING = 'NORMALCLEANING'
IDLE_STOP = 'IDLE/STOP'
STARTED = 'STARTED'


def init_dataframe():
    _dict = {
        'Machine_Status': [],
        'Start_Dttm': [],
        'End_Dttm': [],
        'Duration': [],
        'Error_Code': [],
        'Stop_Reason': []
    }
    return _dict


def policy(csv_file, data_dict):
    df = pd.read_csv(csv_file)
    for i in range(len(df)):
        try:
            if i > 1:
                if df.loc[i, '5'] == RUNNING \
                        and df.loc[i - 1, '5'] == READY \
                        and df.loc[i - 2, '5'] == NORMALCLEANING \
                        and df.loc[i, '6'] == STARTED \
                        and df.loc[i - 1, '6'] == STARTED \
                        and df.loc[i - 2, '6'] == STARTED:
                    data_dict['Machine_Status'].append()
                    data_dict['Start_Dttm'].append()
                    data_dict['End_Dttm'].append()
                    data_dict['Duration'].append()
                    data_dict['Error_Code'].append()
                    data_dict['Stop_Reason'].append()
                elif df.loc[i, '5'] == RUNNING \
                        and df.loc[i - 1, '5'] == READY \
                        and df.loc[i - 2, '5'] == RUNNING \
                        and df.loc[i, '6'] == STARTED \
                        and df.loc[i - 1, '6'] == STARTED \
                        and df.loc[i - 2, '6'] == STARTED:
                    data_dict['Machine_Status'].append()
                    data_dict['Start_Dttm'].append()
                    data_dict['End_Dttm'].append()
                    data_dict['Duration'].append()
                    data_dict['Error_Code'].append()
                    data_dict['Stop_Reason'].append()

        except:
            pass

        pass


if __name__ == '__main__':
    file_name = '4F_T#02.csv'
    _dict = init_dataframe()
    df = pd.read_csv(file_name)
    policy(file_name, _dict)

