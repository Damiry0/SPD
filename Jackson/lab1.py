file = open("Data/JACK8.DAT", "r")
n = file.readline()
lines = file.readlines()
data = [tuple(int(x) for x in line.strip().split()) for line in lines]
data.sort(key=lambda x: x[0])
count = 0
while len(data) > 0:
    popped = data.pop(0)
    tmp_array = [popped]
    for item in data:
        if popped[0] == item[0]:
            tmp_array.append(item)
            data.remove(item)
    tmp_array.sort(key=lambda x: x[1], reverse=True)
    while len(tmp_array) > 0:
        popped = tmp_array.pop()
        if count == 0:
            count = count + popped[0]
        if count < popped[0]:
            tmp = popped[0] - count
            count = count + tmp
        count = count + popped[1]

print(count)
file.close()
