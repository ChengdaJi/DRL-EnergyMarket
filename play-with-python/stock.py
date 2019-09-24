import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../data/stock.csv')
df.head()
#
#
# #setting figure size
# from matplotlib.pylab import rcParams
# rcParams['figure.figsize'] = 20,10
#
# #for normalizing data
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler(feature_range=(0, 1))
#
# #read the file
# df = pd.read_csv('..data/stock.csv')
#
# #print the head
# df.head()