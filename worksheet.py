from pathlib import Path
import os
import pickle
import os
from tqdm import tqdm
from threading import Thread
from multiprocessing import Process, Pool

def get_working_list(path):
    with open(path, mode='rb') as fr :
        data = pickle.load(fr)
    return data

path = Path('F:').joinpath('data', 'naverLand', '220714', '4. articleInfo')
lst = os.listdir(path)

def threadingwork(lst_):
    working_list = []
    for file in tqdm(lst_) :
        file_path = path.joinpath(file)
        data = get_working_list(file_path)
        i = dict(hscpNo=data['articleDetail']['hscpNo'], ptpNo=data['articleDetail']['ptpNo'])
        working_list.append(i)
    return working_list

class Thr(Process):
    def __init__(self, target, args):
        Process.__init__(self)
        self.target = target
        self.args = args
        self.value = None
    
    def run(self):
        self.value = self.target(self.args[0])


def chunk_lst(lst, n):
    c, d = divmod(len(lst), n)
    return [lst[i:i+c] for i in range(0, len(lst), c)]

# data = threadingwork(lst) 
# print(data[:1])

clst = chunk_lst(lst, 3)

with Pool(3) as pool:
    pool.starmap(threadingwork, [(clst[0],), (clst[1],), (clst[2],)])

# thread0 = Thr(target=threadingwork, args=(clst[0],))
# thread1 = Thr(target=threadingwork, args=(clst[1],))
# thread2 = Thr(target=threadingwork, args=(clst[2],))
# thread3 = Thr(target=threadingwork, args=(clst[3],))
# thread4 = Thr(target=threadingwork, args=(clst[4],))
# thread5 = Thr(target=threadingwork, args=(clst[5],))
# thread6 = Thr(target=threadingwork, args=(clst[6],))
# thread7 = Thr(target=threadingwork, args=(clst[7],))
# thread8 = Thr(target=threadingwork, args=(clst[8],))
# thread9 = Thr(target=threadingwork, args=(clst[9],))

# thread0.start()
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()
# thread9.start()

# thread0.join()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# thread6.join()
# thread7.join()
# thread8.join()
# thread9.join()

# print(thread0.value[:2])
# print(thread1.value[:2])
# print(thread2.value[:2])
# print(thread3.value[:2])
# print(thread4.value[:2])
# print(thread5.value[:2])
# print(thread6.value[:2])
# print(thread7.value[:2])
# print(thread8.value[:2])
# print(thread9.value[:2])