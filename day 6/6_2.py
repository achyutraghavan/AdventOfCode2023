def day_6(t, d):
    count = 0

    for i in range(t):
        if i * (t - i) > d:
            count += 1

    return count

input = '''Time:        50     74     86     85
Distance:   242   1017   1691   1252'''

time = input[input.find("Time:")+5:input.find("Distance")]
time = int(time.replace(" ", ""))

distance = input[input.find("Distance:")+10:]
distance = int(distance.replace(" ", ""))

print(day_6(time, distance))


