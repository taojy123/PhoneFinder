#coding=gbk

import os

print "�뽫Ҫ����������ļ�������input�ļ�����"
raw_input("���»س�����ʼ����...")


fns = os.listdir("./input")

lines = []
names = []
phones = []

for fn in fns:
    filename = "./input/" + fn
    for line in open(filename).readlines():
        line = line.strip()
        if len(line) > 10:
            lines.append(line)
            items = line.split()
            name = items[0]
            phone = items[1]
            names.append(name)
            phones.append(phone)


s = ""
n = 0
for i in range(len(phones)):
    phone = phones[i]
    if phones.count(phone) > 1:
        name = names[i]
        s += "%s %s\n" % (name, phone)
        n += 1
        print name, phone


print "==========================================="
print "�ɹ����� %d ����¼" % len(lines)
print "�ظ����� %d ����¼" % n
print "==========================================="


open("%d_%d.txt"%(len(lines), n), "w").write(s)


raw_input("���!���»س����˳�...")



















