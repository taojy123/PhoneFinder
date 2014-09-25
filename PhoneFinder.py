#coding=gbk

import os

print "请将要导入的数据文件放置在input文件夹中"
raw_input("按下回车键开始加载...")


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
print "成功导入 %d 条记录" % len(lines)
print "重复号码 %d 条记录" % n
print "==========================================="


open("%d_%d.txt"%(len(lines), n), "w").write(s)


raw_input("完成!按下回车键退出...")



















