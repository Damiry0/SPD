from timeit import default_timer as timer

file = open("Data/skoczylas.dat", "r")
n = file.readline()
lines = file.readlines()
data = [tuple(int(x) for x in line.strip().split()) for line in lines]
data1 = []
for i in range(0, len(data)):
    data1.append((data[i][0], data[i][1], data[i][2], i))

start = timer()
data1.sort(key=lambda x: x[0])
for (a, b, c, d) in data1:
    print("i:", d + 1, "( r:", a, "p:", b, "q:", c, ")")

count = 0
tmp_count = 0
sortedArray = []

while len(data1) > 0:
    popped = data1.pop()
    tmp_array = [popped]
    for item in data1:
        if popped[0] == item[0]:
            tmp_array.append(item)
            data1.remove(item)
    tmp_array.sort(key=lambda x: x[2])
    count += tmp_array[0][1]
    sortedArray.append(tmp_array.pop())
    if len(tmp_array) != 0:
        data1.extend(tmp_array)
    tmp_array=[]
    data1.sort(key=lambda x: x[2],reverse=True)
    for item2 in data1:
        if count >= item2[0]:
            tmp_array.append(item2)
    while tmp_array:
        popped=tmp_array.pop()
        tmp_count += popped[1]  # dodatkowe warunki
        sortedArray.append(popped)
        data1.remove(popped)
    count += tmp_count

end = timer()
# print("Cmax=", count)
print("Result")
for (a, b, c, d) in sortedArray:
    print("i:", d + 1, "( r:", a, "p:", b, "q:", c, ")")
print("Time elapsed:", end - start)
file.close()
