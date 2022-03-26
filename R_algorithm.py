import pandas as pd
file = open("SCHRAGE1.DAT", "r")
n = file.readline()
df = pd.read_csv(file, sep=' ', names=['r', 'p', 'q'])
print(df)
df = df.sort_values(by=["r","p"])
print(df)
