def trebuchet(doc):
    total = 0
    
    d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six': 6, 'seven':7, 'eight':8, 'nine':9}

    for line in doc.split("\n"):

        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if line[i:j+1] in d.keys():
                    line = line[:i] + str(d[line[i:j + 1]]) + line[j + 1:]
        rev = line[::-1]
        for char in line:
            if char.isdigit():
                first = int(char)
                break
        for char in rev:
            if char.isdigit():
                last = int(char)
                break

        val = 10*first + last
        total += val
        
    return total           

with open('advent_code\\day 1\\1_input.txt', 'r') as f:
    content = f.read()
    print(trebuchet(content))