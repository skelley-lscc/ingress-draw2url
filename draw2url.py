#/bin/python
# program to convert from drawtools to ingress link thing
# each line is defined by two lat,lng points

f = open("testdraw.txt","r")
url = "https://ingress.com/intel?"

latA = []
lngA = []
# count = 4
data = f.readline()
while len(data) > 0:
    print(data)
    nxt = data.find("\"lat\"", 0)
    while nxt > 0:
        nxt = nxt + 6
        end = data.find(",",nxt)
        print(data[nxt:end])
        lat = float(data[nxt:end])
        nxt = end + 7
        end = data.find("}",nxt)
        print(data[nxt:end])
        lng = float(data[nxt:end])

        latA.append(lat)
        lngA.append(lng)

        nxt = data.find("\"lat\"", end)
        # count = count - 1
    
    data = f.readline()

f.close()

url += "ll="+str(latA[0])+","+str(lngA[0])+"&z=14&pls="
for z in range(len(latA)):
    if (z % 2 == 0) and (z > 0):
        url += "_"
    elif (z > 0):
        url += ","
    url += str(latA[z])+","+str(lngA[z])
print(url)
