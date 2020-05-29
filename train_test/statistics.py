#!/usr/bin/env python


def stats(filename):
    d = {}
    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            src, dst, sign = line.split()
            d.setdefault(src, 0)
            d.setdefault(dst, 0)
            d[src] += 1
            d[dst] += 1
    records = []
    for i in sorted(d.items(), key=lambda x:x[1], reverse=False):
        records.append(i)
    count = 0
    num = 0
    threshold = 100
    for i in records[-1000:]: 
        print(i)
        if i[1]>threshold:
            count += 1
            num += i[1]
    print(count, num, num - count * threshold)



dataset = "bitcoinAlpha"
dataset = "bitcoinOTC"
dataset = "slashdot_truncated"
dataset = "epinions_truncated"
filename="./{0}/{0}_train0.edgelist".format(dataset)
stats(filename)

