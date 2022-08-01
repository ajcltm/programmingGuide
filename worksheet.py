import pickle
from pathlib import Path
from pprint import pprint

path = Path('F:').joinpath('data', 'naverLand', '220714','5. complexPrice', 'hscpNo_ptpNo_23_3.pickle')

with open(path, mode='rb') as fr:
    data = pickle.load(fr)

print(data)