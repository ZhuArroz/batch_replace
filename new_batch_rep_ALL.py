import sys
import re
import os

# 使用方法：python 输入文件 配置文件（被替换项→替换项）


def ireplace(old, new, text):  # case insensitive replacement
    idx = 0
    while idx < len(text):
        index_l = text.lower().find(old.lower(), idx)
        if index_l == -1:
            return text
        text = text[:index_l] + new + text[index_l + len(old):]
        idx = index_l + len(new)
    return text


def main():
    source_file = open(sys.argv[1], 'r', encoding="utf-8")
    cfg = open(sys.argv[2], 'r', encoding="utf-8")
    out_file = open(
        sys.argv[1] +
        "_ALL_AFTER_REPLACEMENT",
        'w',
        encoding="utf-8")

    rep_list = []

    for line in cfg.readlines():  # 读取配置文件
        if line.strip("\n") == "":
            continue
        new_line = line.strip("\n")
        new_line_list = new_line.split("\t")
        if len(new_line_list) != 4:
            print("The replacement cfg is illegal, and each line should be in accordance with such format: on	source_string	target_string	CR")
            sys.exit(0)
        if new_line_list[0] != "on" and new_line_list[0] != "off":
            print("The first argument can only be \"on\" or \"off\"!")
            sys.exit(0)
        for j in new_line_list[3]:
            if j != "C" and j != "R":
                print("The fourth argument can only be \"C\" , \"R\" or null!")
                sys.exit(0)

        if new_line_list[0] == "off":
            continue
        else:
            rep_list.append(new_line_list)  # list的元素也是list

    ######################

    all_text = source_file.read()
    rep_str = ""
    rep_str = all_text

    for each_rep_pair in rep_list:
        if each_rep_pair[3] == "":  # 不区分大小写
            rep_str = ireplace(each_rep_pair[1], each_rep_pair[2], rep_str)
        elif each_rep_pair[3] == "C":  # 区分大小写
            rep_str = rep_str.replace(each_rep_pair[1], each_rep_pair[2])
        elif each_rep_pair[3] == "R":  # 不区分大小写，并且按正则表达式替换
            source_string = re.compile(
                each_rep_pair[1],
                re.IGNORECASE | re.MULTILINE)  # 一定要用re.MULTILINE
            rep_str = re.sub(source_string, each_rep_pair[2], rep_str)
        else:  # new_line_list[3]等于"CR"或"RC"，区分大小写，并且按正则表达式替换
            source_string = re.compile(each_rep_pair[1], re.MULTILINE)
            rep_str = re.sub(source_string, each_rep_pair[2], rep_str)

        #print rep_str
    out_file.write((rep_str + "\n"))


if __name__ == "__main__":
    main()
    print("test")
    print("test2,test3")
    print("test4")
    print("test5")
    print("1")
    print("14:20")
    print("14:12")
    print("14:28")
    print("14:47")

