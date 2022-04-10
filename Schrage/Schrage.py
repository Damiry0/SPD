from timeit import default_timer as timer

file = open("Data/SCHRAGE2.DAT", "r")
n = file.readline()
lines = file.readlines()
data = [tuple(int(x) for x in line.strip().split()) for line in lines]
data1 = []
for i in range(0, len(data)):
    data1.append((data[i][0], data[i][1], data[i][2], i))

start = timer()
for (a, b, c, d) in data1:
    print("i:", d + 1, "( r:", a, "p:", b, "q:", c, ")")

count = 0
tmp_count = 0
resultList = []

# while len(data1) > 0:
#     data1.sort(key=lambda x: x[0], reverse=True)
#     popped = data1.pop()
#     tmp_array = [popped]
#     for item in data1:
#         if popped[0] == item[0]:
#             tmp_array.append(item)
#             data1.remove(item)
#     tmp_array.sort(key=lambda x: x[2])
#     count += tmp_array[0][1] + tmp_array[0][0]
#     sortedArray.append(tmp_array.pop())
#     if len(tmp_array) != 0:
#         data1.extend(tmp_array)
#     tmp_array=[]
#     data1.sort(key=lambda x: x[2],reverse=True)
#     for item2 in data1:
#         if count >= item2[0]:
#             tmp_array.append(item2)
#     tmp_array.sort(key=lambda x: x[2])
#     while tmp_array:
#         popped=tmp_array.pop()
#         tmp_count += popped[1]  # dodatkowe warunki
#         sortedArray.append(popped)
#         data1.remove(popped)
#     count += tmp_count
Cmax = 0
Qtime = 0
firstScan = True
# to perwsze wybranie r musi sie wykontywac tylko raz a potem to juz nie
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
            print("Cmax petla=", Cmax)
            if Cmax + item[2] > Qtime:
                Qtime = Cmax + item[2]  # najwiekszy aktualnie czas Cmax z czasem stygniecia
            tmp_array.remove(item)
    waitingList = tmp_array.copy()
# end = timer()
print("Qtime=", Qtime)
print("Result")
for (a, b, c, d) in resultList:
    print("i:", d + 1, "( r:", a, "p:", b, "q:", c, ")")
# print("Time elapsed:", end - start)
file.close()
