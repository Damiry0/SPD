import pandas as pd
file = open("SCHRAGE5.DAT", "r")
n = file.readline()
df = pd.read_csv(file, sep=' ', names=['r', 'p', 'q'])
print(file.name, " before")
print(df)
df = df.sort_values(by=["r"])
print(file.name, " after")
print(df)
print(df.to_latex(index=False), file=open("latex_data.txt",'w'))

