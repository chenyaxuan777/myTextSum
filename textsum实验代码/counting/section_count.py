import json
from collections import Counter

'''
主要是对section进行数据分析，考虑删除哪些section，精简原来的数据集
'''

path = "E:\\paper\\数据集\\arxiv摘要\\arxiv-dataset\\processed_data\\section_names_val.txt"

# 完全读入统计
def count_section_names1(source):
    counts_all = Counter()
    counts_head = Counter()
    counts_tail = Counter()
    head_list = []
    tail_list = []
    with open(source, 'r') as file:
        for line in file.readlines():
            line_dict = json.loads(line)
            # 统计全部
            section_names_list = line_dict["section_names"]
            counts_all += Counter(section_names_list)
            # 头、尾放进一个list中
            head_list.append(section_names_list[0])
            tail_list.append(section_names_list[-1])
        counts_head += Counter(head_list)
        counts_tail += Counter(tail_list)
    print("总数据：\n", counts_all)
    print("头数据：\n", counts_head)
    print("尾数据：\n", counts_tail)

count_section_names1(path)