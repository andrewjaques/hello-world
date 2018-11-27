import numpy as np
import pandas as pd
import os

my_numpy_array = np.random.rand(3)
my_first_series = pd.Series(np.random.rand(3))
my_first_df = pd.DataFrame(np.random.rand(3, 2))  # 3 rows, 2 columns of random data as a Pandas Data Frame

# print("\n\nNumpy Array:\n", my_numpy_array)
#
# print("\n\nPandas Series:\n", my_first_series)
#
# print("\n\nPandas DataFrame:\n", my_first_df)

array_2d = np.random.rand(3, 2)
print(array_2d[0, 1])
# So a regular array can be indexed like [0, 1] - this example gets first row, second column
# DataFrame doesn't work the same way - if you tried this on my_first_df, you get a Key Error

df = pd.DataFrame(array_2d)  # Making a Data Frame out of existing array_2d

# Data Frames - to set labels for columns
df.columns = ["First", "Second"]

print("\n", df)

csv_path = os.path.join('Test1.csv')

andrew_df = pd.read_csv(csv_path, nrows=10, index_col="Test Number", usecols=["Test Number", "PSNR"])

print("\n", andrew_df)

# Creating a new variable for just the PSNR figures in the andrew_df data frame:
psnr_figures = andrew_df['PSNR']
# Determining the number of unique PSNR figures using Panda's own unique function:
print("\n", len(pd.unique(psnr_figures)))

new_csv = os.path.join('example-dvta-results-data-latin1.csv')
new_df = pd.read_csv(new_csv, encoding="latin1", usecols=["Test Description", "Lipsync (ms)", "E-E Delay (ms)", "PSNRY Bad Frames", "PSNRY Average"])

# iloc (index-location) method:
print("\n", new_df.iloc[0, 0:])
# loc (location) method:
print("\n", new_df.loc[12, 'PSNRY Bad Frames'])

