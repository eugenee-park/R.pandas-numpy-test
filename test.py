import numpy as np
import pandas as pd
import sqlalchemy as db
import matplotlib.pyplot as plt

bream_length = pd.read_csv("bream_length.csv").to_numpy().flatten()
bream_weight = pd.read_csv("bream_weight.csv").to_numpy().flatten()
smelt_length = pd.read_csv("smelt_length.csv").to_numpy().flatten()
smelt_weight = pd.read_csv("smelt_weight.csv").to_numpy().flatten()

#print(bream_length)
#print(bream_weight)
#print(smelt_length)
#print(smelt_weight)

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
#plt.show()

fish_length = np.concatenate((bream_length, smelt_length))
fish_weight = np.concatenate((bream_weight, smelt_weight))

fish_data = np.column_stack((fish_length, fish_weight))
print(fish_data)