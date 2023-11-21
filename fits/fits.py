import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
# x0 = 632 y0 = 1118 val = 17481

hdulist = pyfits.open("v523cas60s-001(1).fit")

# вв координаты центра
x0 = int(input())
y0 = int(input())

scidata = hdulist[0].data # обращение к изобр

# горизонтальный срез
x1 = []
val1 = []
for i in range(30):
    val1.append(["empty"])

for i in range(x0-15,x0+15):
    val1[i-(x0-15)] = scidata[y0-1][i-1]
    x1.append(i)

# вертикальный срез
x2 = []
val2 = []
for i in range(30):
    val2.append(["empty"])

for i in range(y0-15,y0+15):
    val2[i-(y0-15)] = scidata[i-1][x0-1]
    x2.append(i)
print(x2)
print(val2)
print(val1)
hdulist.close()

plt.subplot(2,1, 1)
plt.plot(x1, val1, color = 'green')
plt.xlabel('X')
plt.ylabel('Value')
plt.title("Горизонтальный профиль")

plt.subplot(2,1, 2)
plt.plot(x2, val2, color = 'green')
plt.xlabel('Y')
plt.ylabel('Value')
plt.title("Вертикальный профиль")
plt.show()




