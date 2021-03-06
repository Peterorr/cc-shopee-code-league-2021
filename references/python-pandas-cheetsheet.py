import pandas as pd
import numpy as np

pandas.to_datetime()

time_zero = pd.to_datetime('1970-01-01')
df["unix_time"] = pd.to_datetime(df["event_time"]).apply(lambda x: int((x - time_zero).total_seconds()))
df = df.sort_values('unix_time')

for index, row in df.iterrows():
    print(row['c1'], row['c2'])

dtype = {
    'orderid': np.int64,
    'pick': np.int64,
    '1st_deliver_attempt': np.int64,
    '2nd_deliver_attempt': np.float64,
    'buyeraddress': np.object,
    'selleraddress': np.object,
}
df = pd.read_csv(filepath, dtype=dtype)


df.groupby('A').sum()
data.dropna()

df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})


