def jdtogd(i):
    jd = float(tab[i][0]) + 2400000
    jd += 0.5
    z = jd // 1
    f = (jd - 0.5) % 1
    alfa = int((z - 1867216.25) / 36524.25)
    a = z + 1 + alfa - int(alfa / 4)

    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)

    day = int(b - d - int(30.6001 * e))
    if e < 14:
        month = e - 1
    elif e == 14 or e == 15:
        month = e - 13
    if month > 2:
        year = c - 4716
    else:
        year = e - 4715

    hours = int(f * 24)
    if f < 0.5:
        hours += 12
    else:
        hours -= 12
    mins = int(((f * 24) % 1) * 60)
    secs = int(((((f * 24) % 1) * 60) % 1) * 60)
    tab[i][1] = str(year) + '.' + str(month) + '.' + str(day) + ' ' + str(hours) + ':' + str(mins) + ':' + str(secs)
    return(tab[i][1])

dat = open('task2_data_1.dat','r+').readlines()
cell = []
for i in range(len(dat)):
    cell.append(["empty"]*4)

lenn = len(dat)

# раскидываем элементы по ячейкам
for i in range(len(dat)):
    cell[i] = dat[i].split('    ')
    if len(cell[i]) == 0:
        lenn -= 1

for i in range(1,lenn):
    cell[i][3] = cell[i][3].rstrip()

# ввод данных
print('введите название объекта заглавными буквами, не используя специальные символы')
name = str(input())
print('введите количество фильтров')
n = int(input())
filts = []
for i in range(n):
    filts.append(input())

# обрабатываем вв имя и имена в файле
name = name.upper()
for i in range(n):
    filts[i] = filts[i].upper()

# делаем все заглавными
for i in range(lenn):
    cell[i][0] = cell[i][0].upper()
    cell[i][2] = cell[i][2].upper()

# удаляем спец.символы в названиях
j = 0
for i in range(lenn):
    while len(cell[i][0]) != j:
        if not cell[i][0][j].isalpha():
            cell[i][0] = cell[i][0][0:j] + cell[i][0][(j+1):]
            j -= 1
        j += 1
    j = 0

# удаляем пробелы в ост столбцах
for i in range(1,lenn):
    for k in range(1,4):
        while len(cell[i][k]) != j:
            if cell[i][k][j] == " ":
                cell[i][k] = cell[i][k][0:j] + cell[i][k][(j+1):]
                j -= 1
            j += 1
        j = 0

# создаём шапку таблицы
tab = []
for i in range(lenn):
    tab.append(["empty"]*4)
tab[0][0] = 'HJD 24...'
tab[0][1] = 'Greg. date'
tab[0][2] = 'Filter'
tab[0][3] = 'Magnitude'

# вносим данные в новую таблицу
for i in range(n):
    for j in range(1, lenn):
        if (cell[j][2] == filts[i]) and (cell[j][0] == name):
            tab[j][0] = cell[j][1]
            tab[j][2] = filts[i]
            tab[j][3] = cell[j][3]

# создаём список, отвечающий за кол-во отобранных строк для каждого фильтра
numfil = []
for i in range(n):
    numfil.append(0)
for j in range(n):
    for i in range(len(tab)):
        if tab[i][2] == filts[j]:
            numfil[j] += 1
print(numfil)

numstr = 0
for i in range(n):
    numstr += numfil[i]

# удаляем пустые строки
k = 0
for i in range(1,len(tab)):
    if tab[i-k][0] == 'empty':
        del tab[i-k]
        k += 1

# сортируем по фильтрам
for i in range(n):
    for j in range(1, numstr):
        for k in range(j + 1, numstr):
            if ((tab[j][2] != filts[i]) and (tab[k][2] == filts[i])) or (tab[j][2] == filts[i] and tab[k][2] != filts[i] and tab[j - 1][2] != filts[i]):
                tab[j][0], tab[k][0] = tab[k][0], tab[j][0]
                tab[j][1], tab[k][1] = tab[k][1], tab[j][1]
                tab[j][2], tab[k][2] = tab[k][2], tab[j][2]
                tab[j][3], tab[k][3] = tab[k][3], tab[j][3]


# перевод юлианской даты в григорианскую
for i in range(1, len(tab)):
    jdtogd(i)


# сортировка внутри каждого фильтра по возр даты набл



# сортируем новую таблицу, пробегая внутри каждого фильтра
q = 0
for i in range(n):
    if numfil[i] > 1:
        for j in range(q + 1, q + numfil[i]):
            for k in range(j + 1, q + numfil[i] + 1):
                if tab[j][0] > tab[k][0]:
                    tab[j][0], tab[k][0] = tab[k][0], tab[j][0]
                    tab[j][1], tab[k][1] = tab[k][1], tab[j][1]
                    tab[j][2], tab[k][2] = tab[k][2], tab[j][2]
                    tab[j][3], tab[k][3] = tab[k][3], tab[j][3]
        q += numfil[i]
    else:
        q += numfil[i]

# заносим в файл
head = tab[0][0] + '      ' + tab[0][1] + '      ' + tab[0][2] + '    ' + tab[0][3]
with open(name, "w") as file:
    file.write(head + '\n')
    for i in range(1,len(tab)):
        line = tab[i][0] + '    ' + tab[i][1] + '    ' + tab[i][2] + '    ' + tab[i][3]
        file.write(line + '\n')
file.close()
