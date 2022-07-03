import pandas as pd
import numpy as np
import copy

data_url="https://www.csie.ntu.edu.tw/~htlin/course/ml21fall/hw1/hw1_train.dat"
col_names = [i for i in range(1,12)]
data = pd.read_csv(data_url, header=None, names=col_names, delimiter='\t')

target = data[11]