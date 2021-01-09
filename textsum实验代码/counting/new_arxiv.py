import json
from collections import Counter
# 判断这一章是否要被留下
# 做法：section_name章节名， need_section_list一些前缀，
# 遍历need_section_list，如果其中有一个匹配上就返回True，都无返回False
def judge_need(section_name, need_section_list):
    for need_section in need_section_list:
        if need_section in section_name:
            return True
    return False


# section_names_list: 章节名称列表
# need_section_list: 需要留下的章节
# return: 返回需要留下的idx
need_section_head_list = ["introd", "motiva", "backgro", "overvi", "observ", "highlig"]
need_section_tail_list = ["conclu", "summa", "discuss", "resul", "outlo", "analy", "meth"]
def def_sections(section_names_list, need_section_list):
    idx = []    # idx列表：需要留下的章节的索引
    length = len(section_names_list)
    # 长度 <= 2 的全要
    if len(section_names_list) <= 2:
        for i in range(length):
            idx.append(i)
    else:
        # idx_section_list = list(enumerate(section_names_list))
        idx.append(0)   #无论什么情况，第一章都保留
        for i in range(1, length):
            section_name = section_names_list[i]
            if judge_need(section_name, section_names_list):
                idx.append(i)
    return idx


# 从source中删除一些section，剩余的写入target中
def build_newArxiv(source, target):
    with open(source, 'r') as inputs:
        with open(target, 'a+') as output:
            for line in inputs:
                line_dict = json.loads(line)
                section_names_list = line_dict["section_names"]



                line_str = json.dumps(line_dict)
                output.writelines(line_str + '\n')