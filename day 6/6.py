def day_6(t, d):
    count = 0
    t = int(t)
    d = int(d)

    for i in range(t):
        if i * (t - i) > d:
            count += 1

    return count

input = '''Time:        50     74     86     85
Distance:   242   1017   1691   1252'''

input = input.split("\n")

time = input[0][input[0].find('Time:') + 5:]
distance = input[1][input[1].find('Distance:') + 10:]
time = time.split(" ")
time = list(filter(None, time))
distance = distance.split(" ")
distance = list(filter(None, distance))

res_list = []
res = 1

for i in range(len(time)):
    res_list.append(day_6(time[i], distance[i]))

for i in res_list:
    res *= i

print(res)
