mass = input().split(" ")
n = 0
inf = 1
sup = 1
# n = кол-во пробегов по строке, inf = нижняя граница поднимается, sup = веерхняя опускается
while inf <= len(mass)/2:
    if n % 2 == 0:
        for i in range(inf-1, len(mass)-sup):
            if int(mass[i]) > int(mass[i+1]):
                mass[i],mass[i+1] = mass[i+1],mass[i]
        n += 1
        sup += 1
    else:
        for i in range(len(mass)-sup, inf-2, -1):
            if int(mass[i]) > int(mass[i+1]):
                mass[i],mass[i+1] = mass[i+1],mass[i]
        n += 1
        inf += 1

print(mass)