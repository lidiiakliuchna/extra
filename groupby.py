from itertools import groupby

a = input()
x = groupby(a)

for key, grp in x:

    c = 0
    for i in list(grp):

        if key == i:
            c += 1
    print((c, int(key)), end=" ")

#1222311