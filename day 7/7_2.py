def check_fullhouse(str):
    return True if len(set(str)) == 2 else False

def check_2pair(str):
    return True if len(set(str)) == 3 else False

def rank(str):
    print(str)
    res = 1

    joker = 0
    for i in range(len(str)):
        if str[i] == 'J':
            joker += 1

    for i in range(len(str)-1):
        count = 1
        for j in range(i+1, len(str)):
            if str[i] == str[j]: 
                count += 1   
        res = max(count, res) 
 
    if joker == 0:
        if res == 1:
            ranks[1].append(str)
        elif res == 2:
            if check_2pair(str):
                ranks[3].append(str)
            else:
                ranks[2].append(str)
        if res == 3:
            if check_fullhouse(str):
                ranks[5].append(str)
            else:
                ranks[4].append(str)
        elif res == 4:
            ranks[6].append(str)
    
        elif res == 5:
            ranks[7].append(str)

    elif joker == 5 or joker == 4:
        ranks[7].append(str)

    elif joker == 3: 
        if len(set(str)) == 3: ranks[6].append(str)
        else: ranks[7].append(str)
        
    elif joker == 2:
        if len(set(str)) == 2: ranks[7].append(str)
        elif len(set(str)) == 3: ranks[6].append(str)
        elif len(set(str)) == 4: ranks[4].append(str)  

    elif joker == 1:
        if len(set(str)) == 5: ranks[2].append(str)      
        elif len(set(str)) == 4: ranks[4].append(str)
        elif len(set(str)) == 3: 
            d = {i:0 for i in str}
            for i in str:
                d[i]+=1
            if (max(d.values())) == 2:
                ranks[5].append(str)
            else:
                ranks[6].append(str)
        elif len(set(str)) == 2: ranks[7].append(str)
        

with open("advent_code\\day 7\\7_input.txt", "r") as f:
    input = f.read()

d = {}
res = []
ranks = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
'''1- distinct, 2- one pair, 3- two pair, 4- three kind, 5- full house, 6- four kind, 7- 5 kind'''
total_winnnings = 0
 
for i in input.split("\n"):
    d[i.split(" ")[0]] = i.split(" ")[1]

for i in d.keys():
    rank(i)

print(ranks)

def custom_sort(card):
    strength_order = 'AKQT98765432J'
    return [strength_order.index(char) for char in card]

for i in ranks.keys():
    sorted_cards = sorted(ranks[i], key=custom_sort, reverse=True)
    ranks[i] = (sorted_cards)
 
for i in range(1,8):
    if ranks[i]:
        for i in ranks[i]:
            res.append(i)

for i in range(len(res)):
    total_winnnings += (i+1)*int(d[res[i]])

print(total_winnnings)
