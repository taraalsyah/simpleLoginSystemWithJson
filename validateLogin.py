import json
def write_json(data,filename="dictLatihan5.json"):
    with open(filename,"w") as f:
        json.dump(data,f,indent = 4)
with open ("dictLatihan5.json") as json_file:
    data = json.load(json_file)
    y = {"nama":"tara","password":"tara123"}
    data.append(y)
write_json(data)
u = 'tara'
p = 'tara123'
x=len(data)
s=[]
for i in range(len(data)):
    databaru = data[i].values()
    if u in databaru and p in databaru:
        print('benar')
        break
    x=x-1
if x == 0:
    print('salah')
