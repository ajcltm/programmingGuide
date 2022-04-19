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

# df = pd.DataFrame({'col1':[1,1,2,2,3], 'col2':[1,1,2,4,7], 'col3':['a','a','b','c','d']})

# print(df.drop_duplicates(['col1'], keep='last'))


# dic1 = {'1':10, '2':20}
# dic2 = {'1':100, '3':300}

# dic3 = dict(dic1, **dic2)
# print(dic3)


# left = pd.DataFrame(
#     {
#         "key1": ["K0", "K0", "K1", "K2"],
#         "key2": ["K0", "K1", "K0", "K1"],
#         "A": ["A0", "A1", "A2", "A3"],
#         "B": ["B0", "B1", "B2", "B3"],
#     }
# )


# right = pd.DataFrame(
#     {
#         "key1": ["K0", "K1", "K1", "K2"],
#         "key2": ["K0", "K0", "K0", "K0"],
#         "C": ["C0", "C1", "C2", "C3"],
#         "D": ["D0", "D1", "D2", "D3"],
#     }
# )


# result = pd.merge(left, right, how="cross")

# print(left)
# print(right)
# print(result)

# def power(base, exponent):
#     return base ** exponent

# from functools import partial

# square = partial(power, exponent=2)
# cube = partial(power, exponent=3)

# def test_partials():
#     assert square(2) == 4
#     assert cube(2) == 8

# test_partials()

# df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],
#                    'B': ['abc', 'bar', 'xyz']})

# print(df)

# from blinker import signal

# frobnicated = signal('frobnicated')

# class Receiver(object):

#   def __init__(self):
#     def handle_frobnicated(sender, **kwargs):
#       self.on_frobnicated(sender, **kwargs)
#     self.handle_frobnicated = handle_frobnicated
#     frobnicated.connect(handle_frobnicated)

#   def on_frobnicated(self, sender, **kwargs):
#     print(sender, kwargs['message'])

# if __name__ == '__main__':
#   receiver = Receiver()
#   for i in range(10):
#       frobnicated.send('Sender %s' % i, message='hello')

import sys
parentPath='c:/Users/ajcltm/PycharmProjects' # parent 경로
sys.path.append(parentPath) # 경로 추가
import datetime
import time
from messageBot import telegramBot
from blinker import signal
from pandas_datareader import data as pdr
import yfinance as yf

# def receiver(sender, **kwargs):
#   now = kwargs['time']
#   ticker = kwargs['ticker']
#   time_str = f"{now.strftime('%Y-%m-%d %p %H:%M')}\n"

#   try:
#     yf.pdr_override()
#     data = pdr.get_data_yahoo(ticker, start='2022-4-18', end='2022-4-18')
#     data = data.to_dict(orient='records')[0]
#     o, h, l, c, p = data['Open'], data['High'], data['Low'], data['Close'], ((data['Close']/data['Open'])-1)*100
#     data_str = f"[{ticker}]\nOpen :{o:0.2f}\nHigh :{h:0.2f}\nLow  :{l:0.2f}\nClose:{c:0.2f}\nPct  :{p:0.2f}%"
#   except:
#     data_str = "It's seem to be an little error..."

#   print(time_str+data_str)
#   tb.send_message(time_str+data_str)

# sg = signal('timer')
# sg.connect(receiver)


# token = '5344052624:AAH6OUawVEknHCzBOIKixH3by3HNptGMkBA'
# tb = telegramBot.TelegramBot(token = token)

# old_minute = 100
# while True:
#   time.sleep(1)
#   now = datetime.datetime.now()
#   if now.second == 0 and now > datetime.datetime(2022,4,19,21,15) :
#     if not now.minute == old_minute:
#       old_minute = now.minute
#       print(now)
#       sg.send('KimBot', time=now, ticker='005930.KS')

# s = datetime.datetime(2022, 4, 18)
# e = datetime.datetime(2022, 4, 19)
# yf.pdr_override()
# data = pdr.get_data_yahoo('005930.KS', start=s, end=e)
# print(data)


import sys
parentPath='c:/Users/ajcltm/PycharmProjects' # parent 경로
sys.path.append(parentPath) # 경로 추가
from datetime import datetime
from blinker import signal
from signalProcessor import receiver, emitter, processor

class I:
  def __init__(self, ticker):
    self.ticker = ticker

  def strategy(self, sender, **kwargs):
    idx = kwargs['idx']
    date = kwargs['date']
    print(idx, date, self.ticker)

sp = signal('BTAlgo')

r = receiver.BTAlgoReceiver(signal=sp, strategy=I('NVDA').strategy)
start, end = datetime(2022, 4, 1), datetime(2022, 4, 19)
e = emitter.BTAlgoEmitter(signal=sp, start=start, end=end)

processor.Processor(emitter=e, receiver=r).execute()
