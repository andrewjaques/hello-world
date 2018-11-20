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

print(df)

csv_path = os.path.join('Test1.csv')

andrew_df = pd.read_csv(csv_path, nrows=10, index_col="Test Number", usecols=["Test Number", "PSNR"])

print(andrew_df)