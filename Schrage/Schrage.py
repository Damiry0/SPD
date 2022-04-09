import pandas as pd
from timeit import default_timer as timer
file = open("SCHRAGE1.DAT", "r")
n = file.readline()
Cmax = 0
Qtime = 0  # aktualny czas zakonczenia, jesli bierzemy pod uwagę czas stygniecia
df = pd.read_csv(file, sep=' ', names=['r', 'p', 'q'])
# r - czas oczekiwania
# p - czas wykonywania zadania
# q - czas stygnięcia/dostarczenia

# print(file.name, " before")
# print(df)
start = timer()
df = df.sort_values(by=["r", "q"], ascending=[True, False])
# print(file.name, " after")
# print(df)
for index, row in df.iterrows():
    if row['r'] > Cmax:
        Cmax += row['r']-Cmax  # dodawanie ewentualnego czekania na zadanie
    Cmax += row['p']  # zwiekszanie czasu Cmax o czas wykonywania
    if Cmax + row['q'] > Qtime:
        Qtime = Cmax + row['q']  # najwiekszy aktualnie czas Cmax z czasem stygniecia
end = timer()
workTime = end - start  # czas pracy algorytmu w sekundach



print(df)
print("Cmax (z czasem stygniecia): ", Qtime)
# print("Czas w sekundach", workTime)
print("Czas w mikrosekundach", workTime*1000)
# print(int(n), "    ", workTime*1000)

# print(df.to_latex(index=False), file=open("latex_data.txt",'w'))
