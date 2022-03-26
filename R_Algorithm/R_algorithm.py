import pandas as pd
file = open("SCHRAGE1.DAT", "r")
n = file.readline()
Cmax = 0
Qtime = 0  # aktualny czas zakończenia, jeśli bierzemy pod uwagę czas stygnięcia
df = pd.read_csv(file, sep=' ', names=['r', 'p', 'q'])
# print(file.name, " before")
df = df.sort_values(by=["r"])
# print(file.name, " after")
print(df)

#  zliczanie samego Cmax bez czasu stygnięcia
for index, row in df.iterrows():
    if row['r'] > Cmax:
        Cmax += row['r']-Cmax
    Cmax += row['p']
    if Cmax + row['q'] > Qtime:
        Qtime = Cmax + row['q']
print("Cmax ostygnięty max: ", Qtime)

# print(df.to_latex(index=False), file=open("latex_data.txt",'w'))

