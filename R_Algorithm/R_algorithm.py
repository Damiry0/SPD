import pandas as pd
file = open("SCHRAGE1.DAT", "r")
n = file.readline()
Cmax = 0
df = pd.read_csv(file, sep=' ', names=['r', 'p', 'q'])
# print(file.name, " before")
df = df.sort_values(by=["r"])
# print(file.name, " after")
print(df)
for index, row in df.iterrows():
    if row['r'] > Cmax:
        Cmax += row['r']-Cmax
    Cmax += row['p']

print("Cmax: ", Cmax)
# print(df.to_latex(index=False), file=open("latex_data.txt",'w'))

