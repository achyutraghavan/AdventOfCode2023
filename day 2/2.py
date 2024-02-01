with open("advent_code\day 2\input.txt", "r") as f:
    doc = f.read()

res = []

for i in doc.split("\n"):
    sets = i.split(": ")[1].split("; ")
    for j in sets:
        d = {'red': 0, 'green': 0, 'blue': 0}
        for k in j.split(", "):
            d[k.split(" ")[1]] = k.split(" ")[0]
        # print(i.split(": ")[0], d)
        if int(d['red'])>12 or int(d['green'])>13 or int(d['blue'])>14:
            break
    else:
        res.append(i.split(": ")[0])

sum = 0

for i in res:
    sum += int(i.split(" ")[1])

print(sum)