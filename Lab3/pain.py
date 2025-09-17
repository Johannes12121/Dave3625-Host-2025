import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re



df = pd.read_csv('data/Titanic.csv')

df.head(10)
df.tail(10)




print('Mean of "Age" is %.2f' %(df["Age"].mean(skipna=True)))

