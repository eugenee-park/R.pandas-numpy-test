import numpy as np
import pandas as pd
import sqlalchemy as db


bream_length = pd.read_csv("bream_length.csv").to_numpy().flatten()
bream_weight = pd.read_csv("bream_weight.csv").to_numpy().flatten()
smelt_length = pd.read_csv("smelt_length.csv").to_numpy().flatten()
smelt_weight = pd.read_csv("smelt_weight.csv").to_numpy().flatten()

#print(bream_length)
#print(bream_weight)
#print(smelt_length)
print(smelt_weight)
