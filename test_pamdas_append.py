import pandas as pd

df = pd.read_csv('2F_T#24.csv')
column_names = list(df.columns)
dict_ = dict([(column_name, list()) for column_name in column_names])
new_df = pd.DataFrame(dict_)
print(len(df))
for i in range(len(df)):
    # print(df.loc[i].to_dict())
    new_df = new_df.append(df.loc[i].to_dict(), ignore_index=True)

print(new_df)