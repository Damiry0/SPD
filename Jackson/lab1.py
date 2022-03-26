file = open("Data/JACK1.DAT", "r")
n = file.readline()
lines = file.readlines()
data = [tuple(int(x) for x in line.strip().split()) for line in lines]
data1 = []
for i in range(0, len(data)):
    data1.append((data[i][0], data[i][1], i))
data1.sort(key=lambda x: x[0])
count = 0
sortedArray = []
while len(data1) > 0:
    popped = data1.pop(0)
    tmp_array = [popped]
    for item in data1:
        if popped[0] == item[0]:
            tmp_array.append(item)
            data1.remove(item)
    tmp_array.sort(key=lambda x: x[1], reverse=True)
    while len(tmp_array) > 0:
        popped = tmp_array.pop()
        if count == 0:
            count = count + popped[0]
        if count < popped[0]:
            tmp = popped[0] - count
            count = count + tmp
        count = count + popped[1]
        sortedArray.append(popped)
print("Cmax=", count)
for (a, b, c) in sortedArray:
    print("i:", c, "( r:", a, "p:", b, ")")

file.close()
