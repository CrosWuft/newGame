import random,time

ver='2022.6.21/1.0'
while True:
    print('''距骨骰模式选择:
1   player vs computer模式
2   player vs player模式
3   线下模拟掷骰子模式
4   玩法说明
#Create by CrosWuft#''')
    MOD = input('请选择你要进行的游戏模式')
    if MOD == '1':
        def m():
            ####firah1(fir类第一列计算）
            if firh1[0]==firh2[0]==firh3[0]:
                firah1 = int(firh1[0])*9
            elif firh1[0]==firh2[0] :
                if firh1[0]==firh2[0]=='0':
                    firah1=int(firh3[0])
                else:
                    firah1 = int(firh1[0]) * 4 + int(firh3[0])
            elif firh1[0]==firh3[0]:
                if firh1[0] == firh3[0] == '0':
                    firah1=int(firh2[0])
                else:
                    firah1 = int(firh1[0]) * 4 + int(firh2[0])
            elif firh2[0]==firh3[0]:
                if firh2[0]==firh3[0]=='0':
                    firah1 = int(firh1[0])
                else:
                    firah1 = int(firh1[0]) + int(firh2[0])*4
            else:
                firah1 = int(firh1[0]) + int(firh2[0]) + int(firh3[0])
            ####firah2(fir类第二列计算）
            if firh1[1]==firh2[1]==firh3[1]:
                firah2 = int(firh1[1])*9
            elif firh1[1]==firh2[1] :
                if firh1[1]==firh2[1]=='0':
                    firah2=int(firh3[1])
                else:
                    firah2 = int(firh1[1]) * 4 + int(firh3[1])
            elif firh1[1]==firh3[1]:
                if firh1[1] == firh3[1] == '0':
                    firah2=int(firh2[1])
                else:
                    firah2 = int(firh1[1]) * 4 + int(firh2[1])
            elif firh2[1]==firh3[1]:
                if firh2[1]==firh3[1]=='0':
                    firah2 = int(firh1[1])
                else:
                    firah2 = int(firh1[1]) + int(firh2[1])*4
            else:
                firah2 = int(firh1[1]) + int(firh2[1]) + int(firh3[1])
            ####firah3(fir类第三列计算）
            if firh1[2] == firh2[2] == firh3[2]:
                firah3 = int(firh1[2]) * 9
            elif firh1[2] == firh2[2]:
                if firh1[2] == firh2[2] == '0':
                    firah3 = int(firh3[2])
                else:
                    firah3 = int(firh1[2]) * 4 + int(firh3[2])
            elif firh1[2] == firh3[2]:
                if firh1[2] == firh3[2] == '0':
                    firah3 = int(firh2[2])
                else:
                    firah3 = int(firh1[2]) * 4 + int(firh2[2])
            elif firh2[2] == firh3[2]:
                if firh2[2] == firh3[2] == '0':
                    firah3 = int(firh1[2])
                else:
                    firah3 = int(firh1[2]) + int(firh2[2]) * 4
            else:
                firah3 = int(firh1[2]) + int(firh2[2]) + int(firh3[2])
            ####sirah1(sir类第一列计算）
            if sirh1[0] == sirh2[0] == sirh3[0]:
                sirah1 = int(sirh1[0]) * 9
            elif sirh1[0] == sirh2[0]:
                if sirh1[0] == sirh2[0] == '0':
                    sirah1 = int(sirh3[0])
                else:
                    sirah1 = int(sirh1[0]) * 4 + int(sirh3[0])
            elif sirh1[0] == sirh3[0]:
                if sirh1[0] == sirh3[0] == '0':
                    sirah1 = int(sirh2[0])
                else:
                    sirah1 = int(sirh1[0]) * 4 + int(sirh2[0])
            elif sirh2[0] == sirh3[0]:
                if sirh2[0] == sirh3[0] == '0':
                    sirah1 = int(sirh1[0])
                else:
                    sirah1 = int(sirh1[0]) + int(sirh2[0]) * 4
            else:
                sirah1 = int(sirh1[0]) + int(sirh2[0]) + int(sirh3[0])
            ####sirah2(sir类第二列计算）
            if sirh1[1] == sirh2[1] == sirh3[1]:
                sirah2 = int(sirh1[1]) * 9
            elif sirh1[1] == sirh2[1]:
                if sirh1[1] == sirh2[1] == '0':
                    sirah2 = int(sirh3[1])
                else:
                    sirah2 = int(sirh1[1]) * 4 + int(sirh3[1])
            elif sirh1[1] == sirh3[1]:
                if sirh1[1] == sirh3[1] == '0':
                    sirah2 = int(sirh2[1])
                else:
                    sirah2 = int(sirh1[1]) * 4 + int(sirh2[1])
            elif sirh2[1] == sirh3[1]:
                if sirh2[1] == sirh3[1] == '0':
                    sirah2 = int(sirh1[1])
                else:
                    sirah2 = int(sirh1[1]) + int(sirh2[1]) * 4
            else:
                sirah2 = int(sirh1[1]) + int(sirh2[1]) + int(sirh3[1])
            ####sirah3(sir类第三列计算）
            if sirh1[2] == sirh2[2] == sirh3[2]:
                sirah3 = int(sirh1[2]) * 9
            elif sirh1[2] == sirh2[2]:
                if sirh1[2] == sirh2[2] == '0':
                    sirah3 = int(sirh3[2])
                else:
                    sirah3 = int(sirh1[2]) * 4 + int(sirh3[2])
            elif sirh1[2] == sirh3[2]:
                if sirh1[2] == sirh3[2] == '0':
                    sirah3 = int(sirh2[2])
                else:
                    sirah3 = int(sirh1[2]) * 4 + int(sirh2[2])
            elif sirh2[2] == sirh3[2]:
                if sirh2[2] == sirh3[2] == '0':
                    sirah3 = int(sirh1[2])
                else:
                    sirah3 = int(sirh1[2]) + int(sirh2[2]) * 4
            else:
                sirah3 = int(sirh1[2]) + int(sirh2[2]) + int(sirh3[2])
            ####总分计算
            global sirall, firall
            firall = firah1 + firah2 + firah3
            sirall = sirah1 + sirah2 + sirah3
            print(f'[{fir}]:{firall}分')
            print(firh3)
            print(firh2)
            print(firh1)
            print(f"[{sir}]:{sirall}分")
            print(sirh1)
            print(sirh2)
            print(sirh3)
        print("...........player vs computer模式...........")
        firc=0
        sirc=0
        firh1 = ['0', '0', '0']
        firh2 = ['0', '0', '0']
        firh3 = ['0', '0', '0']
        ##########################
        sirh1 = ['0', '0', '0']
        sirh2 = ['0', '0', '0']
        sirh3 = ['0', '0', '0']
        print("[CrosWuft]正在决定谁先掷骰....")
        time.sleep(1)
        dir = random.randint(1, 2)
        if dir == 1:
            print('[CrosWuft]player先掷骰')
            fir = 'player'
            sir = 'computer'
        if dir == 2:
            print('[CrosWuft]computer先掷骰')
            fir = 'computer'
            sir = 'player'
        # noinspection PyUnboundLocalVariable
        if fir == 'player':
            while firc < 9 or sirc < 9:
                k = input(f'[{fir}]按下任意键开始掷骰')
                t = random.randint(1, 6)
                time.sleep(0.4)
                print(f'[{fir}]掷出的点数是: {t} ')
                firc = firc + 1
                while True:
                    line = input(f"[{fir}]请选择你要放在的列数(1-3)")
                    if line == '1':
                        if firh1[0] == '0':
                            firh1[0] = str(t)
                        elif firh2[0] == '0':
                            firh2[0] = str(t)
                        elif firh3[0] == '0':
                            firh3[0] = str(t)
                        else:
                            print('本列已满,请放在其他列!')
                            continue
                        if str(t) == sirh1[0]:
                            sirh1[0] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh2[0]:
                            sirh2[0] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh3[0]:
                            sirh3[0] = '0'
                            sirc = sirc - 1
                        command = m()
                        break
                    elif line == '2':
                        if firh1[1] == '0':
                            firh1[1] = str(t)
                        elif firh2[1] == '0':
                            firh2[1] = str(t)
                        elif firh3[1] == '0':
                            firh3[1] = str(t)
                        else:
                            print('本列已满,请放在其他列!')
                            continue
                        if str(t) == sirh1[1]:
                            sirh1[1] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh2[1]:
                            sirh2[1] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh3[1]:
                            sirh3[1] = '0'
                            sirc = sirc - 1
                        command = m()
                        break
                    elif line == '3':
                        if firh1[2] == '0':
                            firh1[2] = str(t)
                        elif firh2[2] == '0':
                            firh2[2] = str(t)
                        elif firh3[2] == '0':
                            firh3[2] = str(t)
                        else:
                            print('本列已满,请放在其他列!')
                            continue
                        if str(t) == sirh1[2]:
                            sirh1[2] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh2[2]:
                            sirh2[2] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh3[2]:
                            sirh3[2] = '0'
                            sirc = sirc - 1
                        command = m()
                        break
                    else:
                        print("错误的数值!")
                if firc > 8 or sirc > 8:
                    break
                print("")
                t = random.randint(1, 6)
                # noinspection PyUnboundLocalVariable
                print(f'[{sir}]掷出的点数是: {t} ')
                sirc = sirc + 1
                while True:
                    line = str(random.randint(1, 3))
                    if line == '1':
                        if sirh1[0] == '0':
                            sirh1[0] = str(t)
                        elif sirh2[0] == '0':
                            sirh2[0] = str(t)
                        elif sirh3[0] == '0':
                            sirh3[0] = str(t)
                        else:
                            continue
                        if str(t) == firh1[0]:
                            firh1[0] = '0'
                            firc = firc - 1
                        if str(t) == firh2[0]:
                            firh2[0] = '0'
                            firc = firc - 1
                        if str(t) == firh3[0]:
                            firh3[0] = '0'
                            firc = firc - 1
                        command = m()
                        break
                    elif line == '2':
                        if sirh1[1] == '0':
                            sirh1[1] = str(t)
                        elif sirh2[1] == '0':
                            sirh2[1] = str(t)
                        elif sirh3[1] == '0':
                            sirh3[1] = str(t)
                        else:
                            continue
                        if str(t) == firh1[1]:
                            firh1[1] = '0'
                            firc = firc - 1
                        if str(t) == firh2[1]:
                            firh2[1] = '0'
                            firc = firc - 1
                        if str(t) == firh3[1]:
                            firh3[1] = '0'
                            firc = firc - 1
                        command = m()
                        break
                    elif line == '3':
                        if sirh1[2] == '0':
                            sirh1[2] = str(t)
                        elif sirh2[2] == '0':
                            sirh2[2] = str(t)
                        elif sirh3[2] == '0':
                            sirh3[2] = str(t)
                        else:
                            continue
                        if str(t) == firh1[2]:
                            firh1[2] = '0'
                            firc = firc - 1
                        if str(t) == firh2[2]:
                            firh2[2] = '0'
                            firc = firc - 1
                        if str(t) == firh3[2]:
                            firh3[2] = '0'
                            firc = firc - 1
                        command = m()
                        break
                    else:
                        print("错误的数值!")
                print(f'[{sir}]将点数{t}放在了第{line}行')
                print("")
            print("游戏结束")
            # noinspection PyUnboundLocalVariable
            if firall > sirall:
                print(f'恭喜‘{fir}’获胜,{firall}:{sirall}!')
            elif firall < sirall:
                print(f'恭喜‘{sir}’获胜,{firall}:{sirall}!')
            else:
                print(f"平局!{firall}:{sirall}!")
            print("")
            time.sleep(3)
        if fir == 'computer':
            while firc < 9 or sirc < 9:
                t = random.randint(1, 6)
                print(f'[{fir}]掷出的点数是: {t} ')
                firc = firc + 1
                while True:
                    line = str(random.randint(1,3))
                    if line == '1':
                        if firh1[0] == '0':
                            firh1[0] = str(t)
                        elif firh2[0] == '0':
                            firh2[0] = str(t)
                        elif firh3[0] == '0':
                            firh3[0] = str(t)
                        else:
                            continue
                        if str(t) == sirh1[0]:
                            sirh1[0] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh2[0]:
                            sirh2[0] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh3[0]:
                            sirh3[0] = '0'
                            sirc = sirc - 1
                        command = m()
                        break
                    elif line == '2':
                        if firh1[1] == '0':
                            firh1[1] = str(t)
                        elif firh2[1] == '0':
                            firh2[1] = str(t)
                        elif firh3[1] == '0':
                            firh3[1] = str(t)
                        else:
                            continue
                        if str(t) == sirh1[1]:
                            sirh1[1] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh2[1]:
                            sirh2[1] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh3[1]:
                            sirh3[1] = '0'
                            sirc = sirc - 1
                        command = m()
                        break
                    elif line == '3':
                        if firh1[2] == '0':
                            firh1[2] = str(t)
                        elif firh2[2] == '0':
                            firh2[2] = str(t)
                        elif firh3[2] == '0':
                            firh3[2] = str(t)
                        else:
                            continue
                        if str(t) == sirh1[2]:
                            sirh1[2] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh2[2]:
                            sirh2[2] = '0'
                            sirc = sirc - 1
                        if str(t) == sirh3[2]:
                            sirh3[2] = '0'
                            sirc = sirc - 1
                        command = m()
                        break
                    else:
                        print("错误的数值!")
                print(f'[{sir}]将点数{t}放在了第{line}行')
                print("")
                if firc > 8 or sirc > 8:
                    break
                k = input(f'[{sir}]按下任意键开始掷骰')
                t = random.randint(1, 6)
                time.sleep(0.4)
                print(f'[{sir}]掷出的点数是: {t} ')
                sirc = sirc + 1
                while True:
                    line = input(f"[{sir}]请选择你要放在的列数(1-3)")
                    if line == '1':
                        if sirh1[0] == '0':
                            sirh1[0] = str(t)
                        elif sirh2[0] == '0':
                            sirh2[0] = str(t)
                        elif sirh3[0] == '0':
                            sirh3[0] = str(t)
                        else:
                            print('本列已满,请放在其他列!')
                            continue
                        if str(t) == firh1[0]:
                            firh1[0] = '0'
                            firc = firc - 1
                        if str(t) == firh2[0]:
                            firh2[0] = '0'
                            firc = firc - 1
                        if str(t) == firh3[0]:
                            firh3[0] = '0'
                            firc = firc - 1
                        command = m()
                        break
                    elif line == '2':
                        if sirh1[1] == '0':
                            sirh1[1] = str(t)
                        elif sirh2[1] == '0':
                            sirh2[1] = str(t)
                        elif sirh3[1] == '0':
                            sirh3[1] = str(t)
                        else:
                            print('本列已满,请放在其他列!')
                            continue
                        if str(t) == firh1[1]:
                            firh1[1] = '0'
                            firc = firc - 1
                        if str(t) == firh2[1]:
                            firh2[1] = '0'
                            firc = firc - 1
                        if str(t) == firh3[1]:
                            firh3[1] = '0'
                            firc = firc - 1
                        command = m()
                        break
                    elif line == '3':
                        if sirh1[2] == '0':
                            sirh1[2] = str(t)
                        elif sirh2[2] == '0':
                            sirh2[2] = str(t)
                        elif sirh3[2] == '0':
                            sirh3[2] = str(t)
                        else:
                            print('本列已满,请放在其他列!')
                            continue
                        if str(t) == firh1[2]:
                            firh1[2] = '0'
                            firc = firc - 1
                        if str(t) == firh2[2]:
                            firh2[2] = '0'
                            firc = firc - 1
                        if str(t) == firh3[2]:
                            firh3[2] = '0'
                            firc = firc - 1
                        command = m()
                        break
                    else:
                        print("错误的数值!")
                print("")
            print("游戏结束")
            # noinspection PyUnboundLocalVariable
            if firall > sirall:
                print(f'恭喜‘{fir}’获胜,{firall}:{sirall}!')
            elif firall < sirall:
                print(f'恭喜‘{sir}’获胜,{firall}:{sirall}!')
            else:
                print(f"平局!{firall}:{sirall}!")
            print("")
            time.sleep(3)
    elif MOD == '2':
        def m():
            ####firah1(fir类第一列计算）
            if firh1[0]==firh2[0]==firh3[0]:
                firah1 = int(firh1[0])*9
            elif firh1[0]==firh2[0] :
                if firh1[0]==firh2[0]=='0':
                    firah1=int(firh3[0])
                else:
                    firah1 = int(firh1[0]) * 4 + int(firh3[0])
            elif firh1[0]==firh3[0]:
                if firh1[0] == firh3[0] == '0':
                    firah1=int(firh2[0])
                else:
                    firah1 = int(firh1[0]) * 4 + int(firh2[0])
            elif firh2[0]==firh3[0]:
                if firh2[0]==firh3[0]=='0':
                    firah1 = int(firh1[0])
                else:
                    firah1 = int(firh1[0]) + int(firh2[0])*4
            else:
                firah1 = int(firh1[0]) + int(firh2[0]) + int(firh3[0])
            ####firah2(fir类第二列计算）
            if firh1[1]==firh2[1]==firh3[1]:
                firah2 = int(firh1[1])*9
            elif firh1[1]==firh2[1] :
                if firh1[1]==firh2[1]=='0':
                    firah2=int(firh3[1])
                else:
                    firah2 = int(firh1[1]) * 4 + int(firh3[1])
            elif firh1[1]==firh3[1]:
                if firh1[1] == firh3[1] == '0':
                    firah2=int(firh2[1])
                else:
                    firah2 = int(firh1[1]) * 4 + int(firh2[1])
            elif firh2[1]==firh3[1]:
                if firh2[1]==firh3[1]=='0':
                    firah2 = int(firh1[1])
                else:
                    firah2 = int(firh1[1]) + int(firh2[1])*4
            else:
                firah2 = int(firh1[1]) + int(firh2[1]) + int(firh3[1])
            ####firah3(fir类第三列计算）
            if firh1[2] == firh2[2] == firh3[2]:
                firah3 = int(firh1[2]) * 9
            elif firh1[2] == firh2[2]:
                if firh1[2] == firh2[2] == '0':
                    firah3 = int(firh3[2])
                else:
                    firah3 = int(firh1[2]) * 4 + int(firh3[2])
            elif firh1[2] == firh3[2]:
                if firh1[2] == firh3[2] == '0':
                    firah3 = int(firh2[2])
                else:
                    firah3 = int(firh1[2]) * 4 + int(firh2[2])
            elif firh2[2] == firh3[2]:
                if firh2[2] == firh3[2] == '0':
                    firah3 = int(firh1[2])
                else:
                    firah3 = int(firh1[2]) + int(firh2[2]) * 4
            else:
                firah3 = int(firh1[2]) + int(firh2[2]) + int(firh3[2])
            ####sirah1(sir类第一列计算）
            if sirh1[0] == sirh2[0] == sirh3[0]:
                sirah1 = int(sirh1[0]) * 9
            elif sirh1[0] == sirh2[0]:
                if sirh1[0] == sirh2[0] == '0':
                    sirah1 = int(sirh3[0])
                else:
                    sirah1 = int(sirh1[0]) * 4 + int(sirh3[0])
            elif sirh1[0] == sirh3[0]:
                if sirh1[0] == sirh3[0] == '0':
                    sirah1 = int(sirh2[0])
                else:
                    sirah1 = int(sirh1[0]) * 4 + int(sirh2[0])
            elif sirh2[0] == sirh3[0]:
                if sirh2[0] == sirh3[0] == '0':
                    sirah1 = int(sirh1[0])
                else:
                    sirah1 = int(sirh1[0]) + int(sirh2[0]) * 4
            else:
                sirah1 = int(sirh1[0]) + int(sirh2[0]) + int(sirh3[0])
            ####sirah2(sir类第二列计算）
            if sirh1[1] == sirh2[1] == sirh3[1]:
                sirah2 = int(sirh1[1]) * 9
            elif sirh1[1] == sirh2[1]:
                if sirh1[1] == sirh2[1] == '0':
                    sirah2 = int(sirh3[1])
                else:
                    sirah2 = int(sirh1[1]) * 4 + int(sirh3[1])
            elif sirh1[1] == sirh3[1]:
                if sirh1[1] == sirh3[1] == '0':
                    sirah2 = int(sirh2[1])
                else:
                    sirah2 = int(sirh1[1]) * 4 + int(sirh2[1])
            elif sirh2[1] == sirh3[1]:
                if sirh2[1] == sirh3[1] == '0':
                    sirah2 = int(sirh1[1])
                else:
                    sirah2 = int(sirh1[1]) + int(sirh2[1]) * 4
            else:
                sirah2 = int(sirh1[1]) + int(sirh2[1]) + int(sirh3[1])
            ####sirah3(sir类第三列计算）
            if sirh1[2] == sirh2[2] == sirh3[2]:
                sirah3 = int(sirh1[2]) * 9
            elif sirh1[2] == sirh2[2]:
                if sirh1[2] == sirh2[2] == '0':
                    sirah3 = int(sirh3[2])
                else:
                    sirah3 = int(sirh1[2]) * 4 + int(sirh3[2])
            elif sirh1[2] == sirh3[2]:
                if sirh1[2] == sirh3[2] == '0':
                    sirah3 = int(sirh2[2])
                else:
                    sirah3 = int(sirh1[2]) * 4 + int(sirh2[2])
            elif sirh2[2] == sirh3[2]:
                if sirh2[2] == sirh3[2] == '0':
                    sirah3 = int(sirh1[2])
                else:
                    sirah3 = int(sirh1[2]) + int(sirh2[2]) * 4
            else:
                sirah3 = int(sirh1[2]) + int(sirh2[2]) + int(sirh3[2])
            ####总分计算
            global sirall, firall
            firall = firah1 + firah2 + firah3
            sirall = sirah1 + sirah2 + sirah3
            print(f'[{fir}]:{firall}分')
            print(firh3)
            print(firh2)
            print(firh1)
            print(f"[{sir}]:{sirall}分")
            print(sirh1)
            print(sirh2)
            print(sirh3)
        firc=0
        sirc=0
        firh1 = ['0', '0', '0']
        firh2 = ['0', '0', '0']
        firh3 = ['0', '0', '0']
        ##########################
        sirh1 = ['0', '0', '0']
        sirh2 = ['0', '0', '0']
        sirh3 = ['0', '0', '0']
        print("...........player vs player模式...........")
        a=input("[CrosWuft]请玩家自行决定谁是1,2号")
        print("[CrosWuft]正在决定谁先掷骰....")
        time.sleep(1)
        dir=random.randint(1,2)
        if dir==1:
            print('[CrosWuft]player1先掷骰')
            fir='player1'
            sir='player2'
        if dir==2:
            print('[CrosWuft]player2先掷骰')
            fir='player2'
            sir = 'player1'
        while firc<9 or sirc<9:
            # noinspection PyUnboundLocalVariable
            k = input(f'[{fir}]按下任意键开始掷骰')
            t = random.randint(1, 6)
            time.sleep(0.4)
            print(f'[{fir}]掷出的点数是: {t} ')
            firc = firc + 1
            while True:
                line = input(f"[{fir}]请选择你要放在的列数(1-3)")
                if line == '1':
                    if firh1[0]=='0':
                        firh1[0] = str(t)
                    elif firh2[0]=='0':
                        firh2[0]=str(t)
                    elif firh3[0]=='0':
                        firh3[0] = str(t)
                    else:
                        print('本列已满,请放在其他列!')
                        continue
                    if str(t) == sirh1[0]:
                        sirh1[0]='0'
                        sirc=sirc-1
                    if str(t) == sirh2[0]:
                        sirh2[0] = '0'
                        sirc = sirc - 1
                    if str(t) == sirh3[0]:
                        sirh3[0]='0'
                        sirc=sirc-1
                    command=m()
                    break
                elif line == '2':
                    if firh1[1] == '0':
                        firh1[1] = str(t)
                    elif firh2[1] == '0':
                        firh2[1] = str(t)
                    elif firh3[1] == '0':
                        firh3[1] = str(t)
                    else:
                        print('本列已满,请放在其他列!')
                        continue
                    if str(t) == sirh1[1]:
                        sirh1[1]='0'
                        sirc=sirc-1
                    if str(t) == sirh2[1]:
                        sirh2[1] = '0'
                        sirc = sirc - 1
                    if str(t) == sirh3[1]:
                        sirh3[1]='0'
                        sirc=sirc-1
                    command = m()
                    break
                elif line == '3':
                    if firh1[2] == '0':
                        firh1[2] = str(t)
                    elif firh2[2] == '0':
                        firh2[2] = str(t)
                    elif firh3[2] == '0':
                        firh3[2] = str(t)
                    else:
                        print('本列已满,请放在其他列!')
                        continue
                    if str(t) == sirh1[2]:
                        sirh1[2] = '0'
                        sirc = sirc - 1
                    if str(t) == sirh2[2]:
                        sirh2[2] = '0'
                        sirc = sirc - 1
                    if str(t) == sirh3[2]:
                        sirh3[2] = '0'
                        sirc = sirc - 1
                    command = m()
                    break
                else:
                    print("错误的数值!")
            if firc>8 or sirc>8:
                break
            print("")
            # noinspection PyUnboundLocalVariable
            k = input(f'[{sir}]按下任意键开始掷骰')
            t = random.randint(1, 6)
            time.sleep(0.4)
            print(f'[{sir}]掷出的点数是: {t} ')
            sirc=sirc+1
            while True:
                line = input(f"[{sir}]请选择你要放在的列数(1-3)")
                if line == '1':
                    if sirh1[0]=='0':
                        sirh1[0] = str(t)
                    elif sirh2[0]=='0':
                        sirh2[0]=str(t)
                    elif sirh3[0]=='0':
                        sirh3[0] = str(t)
                    else:
                        print('本列已满,请放在其他列!')
                        continue
                    if str(t) == firh1[0]:
                        firh1[0] = '0'
                        firc = firc - 1
                    if str(t) == firh2[0]:
                        firh2[0] = '0'
                        firc = firc - 1
                    if str(t) == firh3[0]:
                        firh3[0] = '0'
                        firc = firc - 1
                    command = m()
                    break
                elif line == '2':
                    if sirh1[1] == '0':
                        sirh1[1] = str(t)
                    elif sirh2[1] == '0':
                        sirh2[1] = str(t)
                    elif sirh3[1] == '0':
                        sirh3[1] = str(t)
                    else:
                        print('本列已满,请放在其他列!')
                        continue
                    if str(t) == firh1[1]:
                        firh1[1] = '0'
                        firc = firc - 1
                    if str(t) == firh2[1]:
                        firh2[1] = '0'
                        firc = firc - 1
                    if str(t) == firh3[1]:
                        firh3[1] = '0'
                        firc = firc - 1
                    command = m()
                    break
                elif line == '3':
                    if sirh1[2] == '0':
                        sirh1[2] = str(t)
                    elif sirh2[2] == '0':
                        sirh2[2] = str(t)
                    elif sirh3[2] == '0':
                        sirh3[2] = str(t)
                    else:
                        print('本列已满,请放在其他列!')
                        continue
                    if str(t) == firh1[2]:
                        firh1[2] = '0'
                        firc = firc - 1
                    if str(t) == firh2[2]:
                        firh2[2] = '0'
                        firc = firc - 1
                    if str(t) == firh3[2]:
                        firh3[2] = '0'
                        firc = firc - 1
                    command = m()
                    break
                else:
                    print("错误的数值!")
            print("")
        print("游戏结束")
        # noinspection PyUnboundLocalVariable
        if firall>sirall:
            print(f'恭喜‘{fir}’获胜,{firall}:{sirall}!')
        elif firall<sirall:
            print(f'恭喜‘{sir}’获胜,{firall}:{sirall}!')
        else:
            print(f"平局!{firall}:{sirall}!")
        print("")
        time.sleep(3)
    elif MOD == '3':
        r=False
        while True:
            k = input('按下任意键开始掷骰，输入“exit”退出')
            if k == 'exit' or k == 'exit ' or k == 'exitexit' or k == 'exitexit ':
                r=True
                print("退出中...")
                print('')
                time.sleep(1)
                break
            if r==False:
                t = random.randint(1, 6)
                time.sleep(0.4)
                print(f'掷出的点数是: {t} ')
    elif MOD == '4':
        print('''游戏规则:
1.将点数相同的骰子放在同一列时，总点数会变得更多;
2.骰子的点数与同一列对手骰子点数相同时，即可摧毁对手的骰子；
3.计算分数的方式是加总所有骰子点数，在同一列且点数相同的骰子，点数会变得越大；
4.当有一方棋局铺满时，将比较两方骰子总点数大小，骰子总点数大的一方获胜；
5.放置骰子时，只有列数之分，即可放在第1列，第2列，第3列，已经放置过骰子的地方，不能再放置骰子，除非被对手摧毁；
6.谁先掷骰子的开始顺序由机器决定；
####Create by CrosWuft,in 2022,8,20####''')
        time.sleep(1)
        input("我已了解!")
        print("")
    else:
        print("错误！")
        print("")
        time.sleep(1.8)
#version=1.0,line in 828 CrosWuft,2022,8,21,s1 TM