import pandas as pd
from timeit import default_timer as timer
file = open("SCHRAGE9.DAT", "r")
n = file.readline()
Cmax = 0
Qtime = 0  # aktualny czas zakonczenia, jesli bierzemy pod uwagę czas stygniecia
df = pd.read_csv(file, sep=' ', names=['r', 'p', 'q'])
# print(file.name, " before")
start = timer()



df = df.sort_values(by=["r"])
# print(file.name, " after")


#  zliczanie samego Cmax bez czasu stygnięcia
for index, row in df.iterrows():
    if row['r'] > Cmax:
        Cmax += row['r']-Cmax
    Cmax += row['p']
    if Cmax + row['q'] > Qtime:
        Qtime = Cmax + row['q']
end = timer()
workTime = end - start
# print(df)
print("Cmax (z czasem stygniecia): ", Qtime)
print("Czas w sekundach", workTime)
print("Czas w mikrosekundach", workTime*1000)
print(int(n),"    ", workTime*1000)

# print(df.to_latex(index=False), file=open("latex_data.txt",'w'))

