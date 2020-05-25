import json
m=0
n=0

with open("typing-data.json", "r") as j:
    data=json.load(j)
    for i in data:
        for r in i['histogram']:
            if r['missCount']>5:
                m+=1
            else:
                n+=1

print(m)
print(n)