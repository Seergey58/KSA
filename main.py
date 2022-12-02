print('Hello Alena Andreevna')  # антиплагиат
k = open('second.dat', 'r')  # открываем файл и читаем его
ko = k.readlines()  # сохраняе то, что прочитали и разбиваем его на строки
k.close()  # закрываем файл (зачем не знаю так как ничего не меняет, но выглядит логично)
vrema = []  # временный массив
for i in ko:
    vrema.append(i.split())
vrema = vrema[1:167] + vrema[168:172] + vrema[177:255] + vrema[257:267]  # даляем списки гдее названия  раздельны
ko = vrema
koz_obj = []  # делаем список только с объектами
s = 0
for j in range(0, (len(ko))):
    koz_obj.append(ko[j][s])
koz_filt = []  # делаем список только с фильтрами
e = 2
for k in range(0, (len(ko))):
    koz_filt.append(ko[k][e])
koz_obj_1 = set(koz_obj)
print(koz_obj_1)
koz_filt_1 = set(koz_filt)
print(koz_filt_1)
f = 1
koz_data = []  # список с датами
for l in range(0, (len(ko))):
    koz_data.append(ko[l][f])
w = 3
koz_mag = []  # список с магнитудами
for y in range(0, (len(ko))):
    koz_mag.append(ko[y][w])
#print(koz_data)
obj_and_filt = []
for o in koz_obj_1:  # делаем список с объуктами и их фильтрами
    filter = []
    for p in range(0, len(ko)):
        if ko[p][0] == o:
            filter.append(ko[p][2])
    filter_1 = set(filter)
    obj_and_filt.append([o, list(filter_1)])
print(obj_and_filt)

for i in range (0, len(koz_data)):  # подписываем 24..
    d = float(koz_data[i])
    d += 2400000
    koz_data[i] = str(d)

grigoriy = []
for i in range (0, len(ko)):
    HJD = float(koz_data[i]) + 0.5
    JD = int(HJD)
    DT = HJD - JD
    a = JD + 32044           # тётя вика помогла
    b = (4*a + 3) // 146097
    c = a - (146097*b // 4)
    d = (4*c + 3)//1461
    e = c - (1461*d)//4
    m = (5*e + 2)//153
    day = e - (153*m + 2)//5 + 1
    month = m + 3 - 12 * (m//10)
    year = 100*b + d - 4800 + (m//10)

    h = DT*24
    mins = (h-int(h))*60
    sec = (mins-int(mins))*60
    dAtA = f'{day}.{month}.{year} {int(h)}:{int(mins)}:{int(sec)}'
    grigoriy.append(dAtA)

inp_obj = input("Ввод названия объекта")
inp_filt = input("Ввод названия фильтра через один ПРОБЕЛ")
print(inp_obj)
print(inp_filt)
file_for_polzovatel = open(f'{"gopa"}.dat', 'w')
#file = open(r'{inp_obj}.dat', 'w')
# file_for_polzovatel = file.write()
# file_for_polzovatel.close()
infil = inp_filt.split( )
r0 = None
r1 = None
r2 = None
r3 = None
r4 = None
if len(infil) == 1:
    r0 = inp_filt
    file_for_polzovatel.write(f"Date\t\t\t\t HJD\t\t\t Magnitude in {r0}\n")
elif len(infil) == 2:
    r0, r1 = infil[1], infil[0]
    file_for_polzovatel.write(f"Date\t\t\t\t HJD\t\t\t Magnitude in {r0}\t Magnitude in {r1}\n")
elif len(infil) == 3:
    r0, r1, r2 = infil[0], infil[1], infil[2]
    file_for_polzovatel.write(f"Date\t\t\t\t HJD\t\t\t Magnitude in {r0}\t Magnitude in {r1}\t Magnitude in {r2}\n")
elif len(infil) == 4:
    r0, r1, r2, r3 = infil[0], infil[1], infil[2], infil[3]
    file_for_polzovatel.write(f"Date\t\t\t\t HJD\t\t\t Magnitude in {r0}\t Magnitude in {r1}\t Magnitude in {r2}\t Magnitude in {r3}\n")
elif len(infil) == 5:
    r0, r1, r2, r3, r4 = infil[0], infil[1], infil[2], infil[3], infil[4]
    file_for_polzovatel.write(f"Date\t\t\t\t HJD\t\t\t Magnitude in {r0}\t Magnitude in {r1}\t Magnitude in {r2}\t Magnitude in {r3}\t Magnitude in {r4}\n")
mag0, mag1, mag2, mag3, mag4, Hjd, Data = [], [], [], [], [], [], []
for i in range(0, len(ko)):
        if koz_obj[i] == str(inp_obj):
            if koz_filt[i] == r0:
                Hjd.append(koz_data[i])
                mag0.append(koz_mag[i])
                Data.append(grigoriy[i])
                mag1.append(f'\t\t\t\t')
                mag2.append(f'\t\t\t\t')
                mag3.append(f'\t\t\t\t')
                mag4.append(f'\t\t\t\t')
            elif koz_filt[i] == r1:
                Hjd.append(koz_data[i])
                mag0.append(f'\t\t\t\t')
                Data.append(grigoriy[i])
                mag1.append(koz_mag[i])
                mag2.append(f'\t\t\t\t')
                mag3.append(f'\t\t\t\t')
                mag4.append(f'\t\t\t\t')
            elif koz_filt[i] == r2:
                Hjd.append(koz_data[i])
                mag0.append(f'\t\t\t\t')
                Data.append(grigoriy[i])
                mag1.append(f'\t\t\t\t')
                mag2.append(koz_mag[i])
                mag3.append(f'\t\t\t\t')
                mag4.append(f'\t\t\t\t')
            elif koz_filt[i] == r3:
                Hjd.append(koz_data[i])
                mag0.append(f'\t\t\t\t')
                Data.append(grigoriy[i])
                mag1.append(f'\t\t\t\t')
                mag2.append(f'\t\t\t\t')
                mag3.append(koz_mag[i])
                mag4.append(f'\t\t\t\t')
            elif koz_filt[i] == r4:
                Hjd.append(koz_data[i])
                mag0.append(f'\t\t\t\t')
                Data.append(grigoriy[i])
                mag1.append(f'\t\t\t\t')
                mag2.append(f'\t\t\t\t')
                mag3.append(f'\t\t\t\t')
                mag4.append(koz_mag[i])

for k in range(0, len(Hjd)):
    min_Hjd = min(Hjd)
    indh = Hjd.index(min_Hjd)
    file_for_polzovatel.write(f"{Data[indh]}\t {min_Hjd}\t {mag0[indh]}\t {mag1[indh]}\t {mag2[indh]}\t {mag3[indh]}\t {mag4[indh]}\n")
    del Hjd[indh], Data[indh], mag0[indh], mag1[indh], mag2[indh], mag3[indh], mag4[indh]
file_for_polzovatel.close()




