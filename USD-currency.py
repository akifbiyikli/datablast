import pandas as pd

pd.set_option('display.max_columns', None)

pip install forex_python
from forex_python.converter import CurrencyRates

c = CurrencyRates()
c.get_rates('USD')

import datetime as dt

date_obj = dt.datetime(2021, 1, 1)

c.get_rates('USD', date_obj)

c.get_rates('USD', dt.datetime(2021, 1, 1))

dates_list = pd.date_range(dt.datetime(2021, 1, 1), dt.datetime(2021, 1, 10), freq='D')

result = []
for i in dates_list:
    result.append((c.get_rates('USD', i)))

df = pd.DataFrame(result)
df.head()
df.shape
df.index = dates_list
df
