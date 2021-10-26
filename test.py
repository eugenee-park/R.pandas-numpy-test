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
#print(fish_data)

#print(bream_length.shape)
#print(smelt_length.shape)

fish_target = np.concatenate((np.ones(35), np.zeros(14)))
#print(fish_target)

indexes = np.arange(49)
np.random.shuffle(indexes)
#print(indexes)

fish_data = fish_data[indexes]
fish_target = fish_target[indexes]
#print(fish_data)
#print(fish_target)

train_data = fish_data[:39]
train_target = fish_target[:39]
test_data = fish_data[39:]
test_target = fish_target[39:]

plt.scatter(train_data[:,0], train_data[:,1])
#plt.show()

## (1) train
#print(train_target.shape)
train_target = train_target.reshape(39, 1)
#print(train_target.shape)
#print(train_data.shape)
train = np.hstack((train_data, train_target))
#print(train)
train_dataFrame = pd.DataFrame(train, columns=["train_length", "train_weight", "train_target"])
#print(train_dataFrame)
#print(train_data)
#print(train_target)

## (2) test
test_target = test_target.reshape(10, 1)
test = np.hstack((test_data, test_target))
test_dataFrame = pd.DataFrame(test, columns=["test_length", "test_weight", "test_target"])
#print(test_dataFrame)

engine = db.create_engine("mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")
train_dataFrame.to_sql("train",engine, index=False,if_exists="replace")
test_dataFrame.to_sql("test",engine, index=False,if_exists="replace")
