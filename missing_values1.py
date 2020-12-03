# importing required values
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# read the train data
train_data = pd.read_csv('dataset/train_kOBLwZA.csv')

# check for the null values
train_data.isna().sum()
