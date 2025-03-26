def rombusz(szelesseg):
    k = 0
    while k != szelesseg:
        empty = szelesseg - k - 2
        print(f"{' '*round((empty/2))}*{k*'-'}{'*' if szelesseg % 2 == 0 else ''}")
        k += 2

    k -= 2

    while k >= 0:
        empty = szelesseg - k - 2
        print(f"{' '*round((empty/2))}*{k*'-'}{'*' if szelesseg % 2 == 0 else ''}")
        k -= 2

rombusz(100)