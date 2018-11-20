import pandas as pd
test1=pd.read_csv("Test1.csv", sep=",",  header=0)
test1.columns=["Test Number", "Test Description", "PSNR", "Colour"]
test2=pd.read_csv("Test2.csv", sep=",",  header=0)
test2.columns=["Test Number", "Test Description", "PSNR", "Colour"]
output = pd.merge(test1, test2, on='Test Number', how='inner')

print(output)