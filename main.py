# !/usr/bin/env python
# -*-encoding:utf-8-*-
"""
@Author : {Jason}
@License : (c)Copyright 2020-
@Contact : {54027901@qq.com}
@software : ${保障处自动排班系统}"""

import datetime

# sequence_task = ['邹堪芳', '刘鹏辉', '王海涛', '苏伟健', '李琦学', '张旭辉', '钟晓东', '万海峰', '李泽杰']
# sequence_prepare = ['钟晓东', '刘鹏辉', '苏伟健', '王海涛', '邹堪芳', '张旭辉', '李琦学', '万海峰', '李泽杰']
week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
today = datetime.date.today()
monday = datetime.date.today()
sunday = datetime.date.today()
one_day = datetime.timedelta(days=1)
while monday.weekday() != 0:
    monday -= one_day
while sunday.weekday() != 6:
    sunday += one_day


def write_holiday(name_holiday):
    with open('holiday.txt', 'w', encoding='utf-8') as f:
        r_holiday = ','.join(name_holiday)
        f.write(r_holiday)


def read_holiday():
    with open('holiday.txt', 'r', encoding='utf-8') as f:
        name_holiday = f.readline().strip()
        name_holiday = name_holiday.split(',')
    return name_holiday


def remove_list(go_rest, name_nomal, name_weekend, name_holiday):
    name_nomal.remove(go_rest)
    name_weekend.remove(go_rest)
    name_holiday.append(go_rest)
    write_holiday(name_holiday)


# sequence_nomal = ['张旭辉', '钟晓东', '邹堪芳', '刘鹏辉', '王海涛', '苏伟健', '李琦学', '万海峰', '李泽杰']
# sequence_weekend = ['刘鹏辉', '王海涛', '钟晓东', '张旭辉', '邹堪芳', '苏伟健', '李琦学', '万海峰', '李泽杰']
def add_list(re_back, name_nomal, name_weekend, name_holiday):
    name_holiday.remove(re_back)
    write_holiday(name_holiday)
    if re_back == '张旭辉':
        if '钟晓东' not in name_holiday:
            index1 = name_nomal.index('钟晓东')
            name_nomal.insert(index1, re_back)
        elif '邹堪芳' not in name_holiday:
            index1 = name_nomal.index('邹堪芳')
            name_nomal.insert(index1, re_back)
        elif '刘鹏辉' not in name_holiday:
            index1 = name_nomal.index('刘鹏辉')
            name_nomal.insert(index1, re_back)
        if '邹堪芳' not in name_holiday:
            index2 = name_weekend.index('邹堪芳')
            name_weekend.insert(index2, re_back)
        elif '苏伟健' not in name_holiday:
            index2 = name_weekend.index('苏伟健')
            name_weekend.insert(index2, re_back)
        elif '李琦学' not in name_holiday:
            index2 = name_weekend.index('李琦学')
            name_weekend.insert(index2, re_back)
    elif re_back == '钟晓东':
        if '邹堪芳' not in name_holiday:
            index1 = name_nomal.index('邹堪芳')
            name_nomal.insert(index1, re_back)
        elif '刘鹏辉' not in name_holiday:
            index1 = name_nomal.index('刘鹏辉')
            name_nomal.insert(index1, re_back)
        elif '王海涛' not in name_holiday:
            index1 = name_nomal.index('刘鹏辉')
            name_nomal.insert(index1, re_back)
        if '张旭辉' not in name_holiday:
            index2 = name_weekend.index('张旭辉')
            name_weekend.insert(index2, re_back)
        elif '邹堪芳' not in name_holiday:
            index2 = name_weekend.index('邹堪芳')
            name_weekend.insert(index2, re_back)
        elif '苏伟健' not in name_holiday:
            index2 = name_weekend.index('苏伟健')
            name_weekend.insert(index2, re_back)
    elif re_back == '邹堪芳':
        if '刘鹏辉' not in name_holiday:
            index1 = name_nomal.index('刘鹏辉')
            name_nomal.insert(index1, re_back)
        elif '王海涛' not in name_holiday:
            index1 = name_nomal.index('王海涛')
            name_nomal.insert(index1, re_back)
        elif '苏伟健' not in name_holiday:
            index1 = name_nomal.index('苏伟健')
            name_nomal.insert(index1, re_back)
        if '苏伟健' not in name_holiday:
            index2 = name_weekend.index('苏伟健')
            name_weekend.insert(index2, re_back)
        elif '李琦学' not in name_holiday:
            index2 = name_weekend.index('李琦学')
            name_weekend.insert(index2, re_back)
        elif '弯海风' not in name_holiday:
            index2 = name_weekend.index('弯海风')
            name_weekend.insert(index2, re_back)
    elif re_back == '刘鹏辉':
        if '王海涛' not in name_holiday:
            index1 = name_nomal.index('王海涛')
            name_nomal.insert(index1, re_back)
        elif '苏伟健' not in name_holiday:
            index1 = name_nomal.index('苏伟健')
            name_nomal.insert(index1, re_back)
        elif '李琦学' not in name_holiday:
            index1 = name_nomal.index('李琦学')
            name_nomal.insert(index1, re_back)
        if '王海涛' not in name_holiday:
            index2 = name_weekend.index('王海涛')
            name_weekend.insert(index2, re_back)
        elif '钟晓东' not in name_holiday:
            index2 = name_weekend.index('钟晓东')
            name_weekend.insert(index2, re_back)
        elif '张旭辉' not in name_holiday:
            index2 = name_weekend.index('张旭辉')
            name_weekend.insert(index2, re_back)
    elif re_back == '王海涛':
        if '苏伟健' not in name_holiday:
            index1 = name_nomal.index('苏伟健')
            name_nomal.insert(index1, re_back)
        elif '李琦学' not in name_holiday:
            index1 = name_nomal.index('李琦学')
            name_nomal.insert(index1, re_back)
        elif '弯海峰' not in name_holiday:
            index1 = name_nomal.index('弯海峰')
            name_nomal.insert(index1, re_back)
        if '钟晓东' not in name_holiday:
            index2 = name_weekend.index('钟晓东')
            name_weekend.insert(index2, re_back)
        elif '张旭辉' not in name_holiday:
            index2 = name_weekend.index('张旭辉')
            name_weekend.insert(index2, re_back)
        elif '邹堪芳' not in name_holiday:
            index2 = name_weekend.index('邹堪芳')
            name_weekend.insert(index2, re_back)
    elif re_back == '苏伟健':
        if '李琦学' not in name_holiday:
            index1 = name_nomal.index('李琦学')
            name_nomal.insert(index1, re_back)
        elif '弯海峰' not in name_holiday:
            index1 = name_nomal.index('弯海峰')
            name_nomal.insert(index1, re_back)
        elif '李泽杰' not in name_holiday:
            index1 = name_nomal.index('李泽杰')
            name_nomal.insert(index1, re_back)
        if '李琦学' not in name_holiday:
            index2 = name_weekend.index('李琦学')
            name_weekend.insert(index2, re_back)
        elif '弯海峰' not in name_holiday:
            index2 = name_weekend.index('弯海峰')
            name_weekend.insert(index2, re_back)
        elif '李泽杰' not in name_holiday:
            index2 = name_weekend.index('李泽杰')
            name_weekend.insert(index2, re_back)
    elif re_back == '李琦学':
        if '弯海峰' not in name_holiday:
            index1 = name_nomal.index('弯海峰')
            name_nomal.insert(index1, re_back)
        elif '李泽杰' not in name_holiday:
            index1 = name_nomal.index('李泽杰')
            name_nomal.insert(index1, re_back)
        elif '张旭辉' not in name_holiday:
            index1 = name_nomal.index('张旭辉')
            name_nomal.insert(index1, re_back)
        if '弯海峰' not in name_holiday:
            index2 = name_weekend.index('弯海峰')
            name_weekend.insert(index2, re_back)
        elif '李泽杰' not in name_holiday:
            index2 = name_weekend.index('李泽杰')
            name_weekend.insert(index2, re_back)
        elif '刘鹏辉' not in name_holiday:
            index2 = name_weekend.index('刘鹏辉')
            name_weekend.insert(index2, re_back)
    elif re_back == '弯海峰':
        if '李泽杰' not in name_holiday:
            index1 = name_nomal.index('李泽杰')
            name_nomal.insert(index1, re_back)
        elif '张旭辉' not in name_holiday:
            index1 = name_nomal.index('张旭辉')
            name_nomal.insert(index1, re_back)
        elif '钟晓东' not in name_holiday:
            index1 = name_nomal.index('钟晓东')
            name_nomal.insert(index1, re_back)
        if '李泽杰' not in name_holiday:
            index2 = name_weekend.index('李泽杰')
            name_weekend.insert(index2, re_back)
        elif '刘鹏辉' not in name_holiday:
            index2 = name_weekend.index('刘鹏辉')
            name_weekend.insert(index2, re_back)
        elif '王海涛' not in name_holiday:
            index2 = name_weekend.index('王海涛')
            name_weekend.insert(index2, re_back)
    elif re_back == '李泽杰':
        if '张旭辉' not in name_holiday:
            index1 = name_nomal.index('张旭辉')
            name_nomal.insert(index1, re_back)
        elif '钟晓东' not in name_holiday:
            index1 = name_nomal.index('钟晓东')
            name_nomal.insert(index1, re_back)
        elif '邹堪芳' not in name_holiday:
            index1 = name_weekend.index('刘鹏辉')
            name_weekend.insert(index1, re_back)
        if '刘鹏辉' not in name_holiday:
            index2 = name_weekend.index('刘鹏辉')
            name_weekend.insert(index2, re_back)
        elif '王海涛' not in name_holiday:
            index2 = name_weekend.index('王海涛')
            name_weekend.insert(index2, re_back)
        elif '钟晓东' not in name_holiday:
            index2 = name_weekend.index('钟晓东')
            name_weekend.insert(index2, re_back)


def change_name(re_back, go_rest, name_nomal, name_weekend, name_holiday):
    if len(go_rest) != 0 and len(re_back) == 0:
        remove_list(go_rest, name_nomal, name_weekend, name_holiday)
    elif len(go_rest) == 0 and len(re_back) != 0:
        add_list(re_back, name_nomal, name_weekend, name_holiday)
    elif len(go_rest) != 0 and len(re_back) != 0:
        remove_list(go_rest, name_nomal, name_weekend, name_holiday)
        add_list(re_back, name_nomal, name_weekend, name_holiday)
    print("当前休假人员更改为为：%s" % name_holiday)
    print("当前可值班人员更改为：%s" % name_nomal)


def update_date():
    with open('date_file.txt', 'w') as f:
        f.write(str(sunday))


def read_last():
    with open('last_nomal.txt', 'r', encoding='UTF-8') as fi:
        name_nomal = fi.readline().strip()
        name_weekend = fi.readline().strip()
        name_nomal = name_nomal.split(',')
        name_weekend = name_weekend.split(',')
        return name_nomal, name_weekend


def read_curent():
    with open('curent.txt', 'r', encoding='UTF-8') as f:
        name_nomal = f.readline().strip()
        name_weekend = f.readline().strip()
        name_nomal = name_nomal.split(',')
        name_weekend = name_weekend.split(',')
    return name_nomal, name_weekend


def get_curent_week(name_nomal, name_weekend):
    for i in range(5):
        day = monday + datetime.timedelta(days=i)
        duty = name_nomal.pop(0)
        # if day == today:
        #     today_duty = duty
        day = str(day) + "-" + week[i] + " ---- 值班人员为：" + duty
        name_nomal.append(duty)
        print(day)
    for i in range(5, 7):
        day = monday + datetime.timedelta(days=i)
        duty = name_weekend.pop(0)
        day = str(day) + "-" + week[i] + " ---- 值班人员为：" + duty
        name_weekend.append(duty)
        print(day)
    # return today_duty


def get_next_week(name_nomal, name_weekend):
    for i in range(7, 12):
        day = monday + datetime.timedelta(days=i)
        duty = name_nomal.pop(0)
        day = str(day) + "-" + week[i - 7] + " ---- 值班人员为：" + duty
        name_nomal.append(duty)
        print(day)
    for i in range(12, 14):
        day = monday + datetime.timedelta(days=i)
        duty = name_weekend.pop(0)
        day = str(day) + "-" + week[i - 7] + " ---- 值班人员为：" + duty
        name_weekend.append(duty)
        print(day)


def write_last(name_nomal, name_weekend):
    r_nomal = ','.join(name_nomal) + "\n"
    r_weekend = ','.join(name_weekend)
    with open('last_nomal.txt', 'w', encoding='utf-8') as f:
        f.write(r_nomal)
        f.write(r_weekend)


def write_curent(name_nomal, name_weekend):
    r_n = ','.join(name_nomal) + "\n"
    r_w = ','.join(name_weekend)
    # print(r_n)
    with open('curent.txt', 'w', encoding='utf-8') as f:
        f.write(r_n)
        f.write(r_w)


def just_name(name_nomal, name_weekend):
    name_holiday = read_holiday()
    print("当前休假人员: %s" % name_holiday)
    print("当前可值班人员：%s" % name_nomal)
    re_back = input("请输入休假返回人员（输入人员将加入到本周值班，如果无直接回车。）：")
    while True:
        if re_back == "":
            break
        elif re_back not in name_holiday:
            re_back = input("您输入的名称错误或其不在休假中，请输重新入正确的返回人员：")
        elif re_back in name_holiday:
            break
    go_rest = input("请输入即将休假人员（输入人员将从当前值班人员中剔除，如果无直接回车。）：")
    while True:
        if go_rest == "":
            break
        elif go_rest not in name_nomal:
            go_rest = input("您输入的名称错误或其已经在休假中，请重新输入正确的即将休假人员：")
        elif go_rest in name_nomal:
            break
    if re_back != "" or go_rest != "":
        change_name(re_back, go_rest, name_nomal, name_weekend, name_holiday)
    write_curent(name_nomal, name_weekend)
    print("*" * 50)
    print("本周值班：")
    get_curent_week(name_nomal, name_weekend)
    print("*" * 50)
    print("下周值班：")


def main():
    with open('date_file.txt', 'r') as f:
        date = f.read()
        date = datetime.date(*map(int, date.split('-')))
    today_ch = today.strftime("%Y{y}%m{m}%d{d}").format(y="年", m='月', d='日')
    print("今天是：%s" % str(today_ch))

    if today > date:
        # 调用上周值班表
        name_nomal, name_weekend = read_last()
        just_name(name_nomal, name_weekend)
        get_next_week(name_nomal, name_weekend)
        # 更新date为本周sunday
        update_date()

    elif today <= date:
        # 读取本周值班表
        name_nomal, name_weekend = read_curent()
        just_name(name_nomal, name_weekend)
        write_last(name_nomal, name_weekend)
        get_next_week(name_nomal, name_weekend)
        input("《按回车退出》")


if __name__ == "__main__":
    main()
