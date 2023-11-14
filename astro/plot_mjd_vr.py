import matplotlib.pyplot as plt

file = open('Mon_v_radial.dat','r+').readlines()
mjd = []
vr = []
data = []
for i in range(len(file)):
    mjd.append(["empty"])
    vr.append(["empty"])
    data.append(["empty"]*2)

for i in range(len(file)):
    data[i] = file[i].split()

for i in range(1,len(file)):
    mjd[i] = float(data[i][0])
    vr[i] = float(data[i][1])

for i in range(len(file)-1):
    mjd[i] = mjd[i + 1]
    vr[i] = vr[i + 1]
mjd.pop(-1)
vr.pop(-1)

#print(data)
#print(mjd)
#print(vr)


plt.scatter(mjd, vr, marker = 'o', color = 'green')
plt.xlabel('MJD')
plt.ylabel('Vr')

plt.show()