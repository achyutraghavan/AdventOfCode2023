def trebuchet(doc):
    total = 0

    for line in doc.split("\n"):
       
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