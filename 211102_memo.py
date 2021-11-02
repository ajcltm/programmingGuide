from pathlib import Path
import re
import pandas as pd
import numpy as np
from datetime import datetime



# df = pd.DataFrame(
#     np.random.randn(3, 2), columns=[" Column A ", " Column B "], index=range(3)
# )

# print(df)

# print(df.columns.str.strip())


# s = pd.Series(["ab c", "c de ", np.nan, " f g h "], dtype="string")
# print(s)


# print(s.str.replace(' ',''))


# df = pd.DataFrame({'ticker':['005930', '000829'],
#                     'name':['samsung', 'dongsan']})

# print(df)

# print(df.apply(lambda row: row.str.cat(sep='&'), axis=1))



dic = {}
for i in range(0,4) :
    dic[f'key_{i}'] = i
print(dic)


withdrawal = {}

symbols = ['AAPL', 'NVDA', 'AMZN']
for symbol in symbols:
    withdrawal[symbol] = {'unitPrice': 0, 'amounts': 0}
print(withdrawal)


a = {1: 'a', 'name':'pey', 3:[1,2,3]}

del a[1]

print(a)


a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.clear()
print(a)


a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('nokey'))

print('name' in a)
print('email' in a)


dic1 = {1:10, 2:20}

dic2 = {1:100, 3:300}

dic1.update(dic2)

print(dic1)
