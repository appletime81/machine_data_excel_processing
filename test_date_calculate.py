import pandas as pd
from datetime import datetime


def time_delta(time1, time2):
    # time2 > time1
    time_delta = datetime.strptime(time2, DATE_FORMAT) - datetime.strptime(time1, DATE_FORMAT)
    time_delta = time_delta.total_seconds()
    return time_delta


if __name__ == '__main__':
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    df = pd.read_csv('4F_T#02.csv')
    time_delta = time_delta(df.loc[0, '1'], df.loc[1, '1'])
    print(time_delta)
    print(df.loc[0, '8'] == 2042)
