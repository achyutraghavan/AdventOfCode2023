with open("advent_code\day 2\input.txt", "r") as f:
    doc = f.read()

res = 0

for i in doc.split("\n"):
    sets = i.split(": ")[1].split("; ")
    d_max = {'red': 0, 'green': 0, 'blue': 0}
    for j in sets:
        d = {'red': 0, 'green': 0, 'blue': 0}
        for k in j.split(", "):
            d[k.split(" ")[1]] = k.split(" ")[0]
        d_max['red'] = max(d_max['red'], int(d['red']))
        d_max['green'] = max(d_max['green'], int(d['green']))
        d_max['blue'] = max(d_max['blue'], int(d['blue']))
    res += d_max['red']*d_max['blue']*d_max['green']

print(res)