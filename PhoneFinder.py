#coding=gbk

import os
import time

print "�뽫Ҫ����������ļ�������input�ļ�����."
mode = raw_input("��ѡ����ģʽ(1/2):")


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
        if mode == "2":
            if phone not in phones[i+1:]:
                # time.sleep(0.1)
                continue
        name = names[i]
        s += "%s %s\n" % (name, phone)
        n += 1
        print name, phone


print "==========================================="
print "�ɹ����� %d ����¼" % len(lines)
print "�ظ����� %d ����¼" % n
print "����Ѿ��������ļ� %d_%d.txt (���԰汾�����������λ����)" % (len(lines), n)
print "==========================================="


open("%d_%d.txt"%(len(lines), n), "w").write(s)


raw_input("���!���»س����˳�...")



















