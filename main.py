import numpy as np
import pandas as pd
from pypinyin import pinyin as py

try:
    df = pd.read_csv(r'..\Chinese\words.csv')
except:
    df = pd.read_csv(r'Chinese\words.csv')
# df.loc[0] = ["告罄", 5]
# df.loc[1] = ["1", 2]
# print(df)


def add(ch, star):
    df.loc[df._stat_axis.values.tolist()[-1]+1] = (ch, int(star))
    # print(df)


def test():
    p = np.array(df['star'])
    l = np.random.choice(range(len(p)), 3, p=p/p.sum())
    # print(l)
    for i in l:
        # print(df['words'][i])
        pin = py(df['words'][i])
        # print(pin)
        for j in pin:
            print(j[0], end=' ')
        print()

        yn = input(df['words'][i]+", 是否正确?(t0, f1): ")
        if yn == '1':
            df.loc[i, 'star'] += 1
        elif yn == '0' and df.loc[i, 'star'] >= 1:
            df.loc[i, 'star'] -= 1
    # print(df)


while True:
    pyin = input(">>>")
    if pyin == 'q' or pyin == "exit":
        try:
            df.to_csv(r"..\Chinese\words.csv", index=False)
        except:
            df.to_csv(r"Chinese\words.csv", index=False)
        break
    elif pyin == 'add':
        add(input("ch: "), input("star: "))
    elif pyin == 'test':
        test()
    elif pyin == 'print':
        print(df)
