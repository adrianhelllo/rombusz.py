def rombusz(szelesseg):
    k = 0
    while k < szelesseg:
        empty = szelesseg - k - 2
        print(f"{' '*round((empty/2))}*{k*'-'}{'*' if szelesseg % 2 == 0 else '' if k == 0 else '*'}")
        if k == 0 and szelesseg % 2 == 1:
            k = 1
        else:
            k += 2

    k -= 2

    while k >= 0:
        empty = szelesseg - k - 2
        print(f"{' '*round((empty/2))}*{k*'-'}{'*' if szelesseg % 2 == 0 else '' if k == 0 else '*'}")
        if k == 1 and szelesseg % 2 == 1:
            k = 0
        else:
            k -= 2

romb_szel = int(input("Milyen széles rombuszt szeretnél?: "))
rombusz(romb_szel)