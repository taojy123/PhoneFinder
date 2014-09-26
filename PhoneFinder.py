#coding=gbk

import os
import time

print "请将要导入的数据文件放置在input文件夹中."
mode = raw_input("请选择导入模式(1/2):")


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
print "成功导入 %d 条记录" % len(lines)
print "重复号码 %d 条记录" % n
print "结果已经导出至文件 %d_%d.txt (测试版本将隐藏最后三位数字)" % (len(lines), n)
print "==========================================="


open("%d_%d.txt"%(len(lines), n), "w").write(s)


raw_input("完成!按下回车键退出...")



















