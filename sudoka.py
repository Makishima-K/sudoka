a = open('sud.txt', 'r',encoding='UTF-8')
b = 0
stroka = []
d = []
e = 0
j = 0
stolbik = []
cubik = []
g = []
tt = 0
tt2 = 0
for i in a:
    j = i
    e = i[0:17]
    print(e)
    d = e.split(' ')
    stroka.append(d)
    b+=1

a.close()







#print(stroka[0])
# def hub():
#     print()
# while tt2<9:
#     for i in range(9):
#         print('III')
#         g.append(stroka[i][tt2]) 
#     tt2 +=1
#     stolbik.append(g)
#     g = []
# #print(stolbik)
# gg2 = []
# jj = 0
# jjj = 0
# jjjj = 0
# while tt<9:
#     for i in range(9):
#         if jjj > 2:
#             jj +=1
#             jjj = 0
#             #print('12122')jjj+jjjj jj
#         gg2.append(stroka[jjj+jjjj][jj])

#         #print(gg2)
#         jjj +=1
    
#     tt+=1
#     #print(gg2)
#     if tt == 3:
#         jj = -1
#         jjjj =3
#     if tt == 6:
#         jj = -1
#         jjjj =6



 #   cubik.append(gg2)
#    gg2=[]
#------------------------------------------
def generate_columns(stroka):
    stolbik = []  # Список для хранения столбцов
    tt2 = 0       # Начальная позиция для tt2 (индекса столбцов)

    # Создаем столбцы
    while tt2 < 9:
        g = []  # Временный список для текущего столбца
        for i in range(9):
            g.append(stroka[i][tt2]) 
        stolbik.append(g)
        tt2 += 1

    return stolbik

def generate_squares(stroka):
    gg2 = []     # Список для хранения квадратов
    tt = 0       # Начальная позиция для tt (индекса квадратов)
    jj = 0       # Начальная позиция для горизонтального сдвига квадрата
    jjj = 0      # Счетчик для сдвига внутри строки
    jjjj = 0     # Переменная для вертикального сдвига

    # Создаем квадраты 3x3
    while tt < 9:
        square = []  # Временный список для текущего квадрата
        for i in range(9):
            if jjj > 2:
                jj += 1
                jjj = 0
            square.append(stroka[jjj + jjjj][jj])
            jjj += 1

        gg2.append(square)
        tt += 1

        if tt == 3:
            jj = -1
            jjjj = 3
        elif tt == 6:
            jj = -1
            jjjj = 6

    return gg2

# Пример вызова функций
# столбцы = generate_columns(stroka)
# квадраты = generate_squares(stroka)
# print("Столбцы:", столбцы)
# print("Квадраты:", квадраты)




stolbik = generate_columns(stroka)
cubik = generate_squares(stroka)

#----------------------------------------

print(cubik)
print('_________________________________________')
print(stolbik)
print('_________________________________________')
print(stroka)
#----------------------------------------------#
print('________________________________________')
ttttttt = True
cubikNum=0
op = 0
bob =0
bob1=0
lulu = 0
trtrt = 0
lululu = 0
while ttttttt:
    cubikNum=0
    op = 0
    bob =0
    bob1=0
    stroka1 = 0
    trtrt = 0
    lululu +=1
    for i in stroka:
        stroka1 += 1
        for r in i:
            lulu +=1
            numnum = ['1','2','3','4','5','6','7','8','9']
            numnum2 = ['1','2','3','4','5','6','7','8','9']
            #print(r)
            op +=1
            if op < 4:
                cubikNum = 1 + bob
            elif op < 7:
                cubikNum = 2 + bob
            elif op < 10:
                cubikNum = 3 + bob

            #print(cubikNum,'--',op,'--',r)
            
            
            #print(stolbik[op-1],op-1,'=',lulu)
            #print(i,'op pop')
            #print(cubik[cubikNum-1],'op oppo')
            if r == '0':
                trtrt = 52
                for y in numnum2:
                    for cub in cubik[cubikNum-1]:
                        if cub == y:
                            if y in numnum:
                                numnum.remove(y)
                                #print(numnum)
                    for stroka5 in i:
                        if stroka5 == y:
                            if y in numnum:
                                numnum.remove(y)
                                #print(numnum)
                    for stolb in stolbik[op-1]:
                        if stolb == y:
                            if y in numnum:
                                numnum.remove(y)
                                #print(numnum)
            if 1 == len(numnum):
                #print(stroka1-1)
                #print(op-1)
                #print(stroka)
                #print(stroka[stroka1-1])
                #print('!!!!!!',stroka[stroka1-1],numnum[0])
                stroka[stroka1-1][op-1] = numnum[0]
                stolbik = generate_columns(stroka)
                cubik = generate_squares(stroka)
                #print('!!!!!!',stroka[stroka1-1],numnum[0])



            if op == 9:
                bob1 +=1
                op = 0

            if bob1 == 3:
                bob1 =0
                bob +=3
    
    #print()
    #print(stroka)
    #print()
    if trtrt == 0 or lululu == 14:
        v = open('sudokakaka.txt','w',encoding='UTF-8')
        for i in stroka:
            for a in range(len(i)):
                v.write(str(i[a]))
                v.write(' ')
                #print(i[a])
            v.write('\n')
        v.close()
        print(cubik)
        print(stolbik)
        break







