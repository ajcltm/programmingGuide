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



# dic = {}
# for i in range(0,4) :
#     dic[f'key_{i}'] = i
# print(dic)


# withdrawal = {}

# symbols = ['AAPL', 'NVDA', 'AMZN']
# for symbol in symbols:
#     withdrawal[symbol] = {'unitPrice': 0, 'amounts': 0}
# print(withdrawal)


# a = {1: 'a', 'name':'pey', 3:[1,2,3]}

# del a[1]

# print(a)


# a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
# a.clear()
# print(a)


# a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
# print(a.get('name'))
# print(a.get('nokey'))

# print('name' in a)
# print('email' in a)


# dic1 = {1:10, 2:20}

# dic2 = {1:100, 3:300}

# dic1.update(dic2)

# print(dic1)


# import random 
# lst = [1, 2, 3]
# choiceLst = random.choice(lst)
# print(choiceLst)

# lst = [1, 2, 3]
# sampleLst = random.sample(lst, 2)
# print(sampleLst)


# li = [1, 2, 3]
# choiceLst = [random.choice(li) for i in range(5)]
# print(choiceLst)

# df8 = pd.DataFrame({'col_1': ['1', '2', '3'], 
#                    'col_2': ['4', 'bbb', '6']})
# df8 = df8.apply(pd.to_numeric, errors = 'coerce')
# print(df8)

# from dataclasses import dataclass, field

# @dataclass
# class Car:
#     name: str 
#     brand: str
#     price: int

# @dataclass
# class CarDealer:
#     date : str
#     name : str
#     car: dict = field(default_factory=dict)

#     def __post_init__(self):
#         self.car['car'] = Car(self.name, 'tesla', '120000')

# car = CarDealer(date='20100101', name='tesla')
# print(car)

df = pd.DataFrame({'col1':[1,5,7,6,3], 'col2':[1,2,3,6,9]})
print(df)


print(df.to_dict(orient="records"))