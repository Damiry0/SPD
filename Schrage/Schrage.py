from timeit import default_timer as timer


def display(input_list):
    for (a, b, c, d) in input_list:
        print("i:", d + 1, "( r:", a, "p:", b, "q:", c, ")")


file = open("Data/skoczylas.dat", "r")
n = file.readline()
lines = file.readlines()
data = [tuple(int(x) for x in line.strip().split()) for line in lines]
data1 = []
for i in range(0, len(data)):
    data1.append((data[i][0], data[i][1], data[i][2], i))

# start = timer()
display(data1)
resultList = []
Cmax = 0
Qtime = 0
firstScan = True
# to pierwsze wybranie r musi sie wykonywac tylko raz, a potem to juz nie
waitingList = sorted(data1, key=lambda x: (x[0], -x[2]))
while len(waitingList) > 0:
    waitingList = sorted(waitingList, key=lambda x: (x[0], -x[2]))
    popped = waitingList.pop(0)
    resultList.append(popped)
    # Cmax += popped[0] + popped[1]
    if popped[0] > Cmax:
        Cmax = popped[0]  # dodawanie ewentualnego czekania na zadanie
    Cmax += popped[1]  # zwiekszanie czasu Cmax o czas wykonywania
    if Cmax + popped[2] > Qtime:
        Qtime = Cmax + popped[2]  # najwiekszy aktualnie czas Cmax z czasem stygniecia

    waitingList.sort(key=lambda x: x[2], reverse=True)
    array_range = len(waitingList)
    tmp_array = waitingList.copy()

    for item in waitingList:
        if Cmax >= item[0]:
            resultList.append(item)
            Cmax += item[1]  # zwiekszanie czasu Cmax o czas wykonywania
            # print("Cmax petla=", Cmax)
            if Cmax + item[2] > Qtime:
                Qtime = Cmax + item[2]  # najwiekszy aktualnie czas Cmax z czasem stygniecia
            tmp_array.remove(item)
    waitingList = tmp_array.copy()
# end = timer()
print("Cmax (z czasem stygniecia): ", Qtime)
print("Result")
display(resultList)
# print("Time elapsed:", end - start)
file.close()
