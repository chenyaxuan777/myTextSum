import json
import time

import pandas
from collections import Counter

src = "E:\\paper\\数据集\\arxiv摘要\\arxiv-dataset\\"
tar = "E:\\paper\\数据集\\arxiv摘要\\arxiv-dataset\\processed_data\\"
sources = ["val.txt", "test.txt", "train.txt"]
targets_txt = ["del_val.txt", "del_test.txt", "del_train.txt"]
targets_json = ["del_val.json", "del_test.json", "del_train.json"]
targets_section_names = ["section_names_val.txt", "section_names_test.txt", "section_names_train.txt"]

# 读取每篇文章，删除其中的article_text，再写出到新文件中
def delArticleText(source, target):
    with open(source, 'r') as inputs:
        with open(target, 'a+') as output:
            for line in inputs:
                line_dict = json.loads(line)
                del line_dict["article_text"]
                line_str = json.dumps(line_dict)
                output.writelines(line_str+'\n')

# 只要每篇文章的article_id 和 section_names,写出到新文件中
def getSectionNames(source, target):
    with open(source, 'r') as inputs:
        with open(target, 'a+') as output:
            for line in inputs:
                line_dict = json.loads(line)
                del line_dict["abstract_text"]
                del line_dict["labels"]
                del line_dict["sections"]
                line_str = json.dumps(line_dict)
                output.writelines(line_str+'\n')

# # 统计section_name信息
# def countSection_ames(source):
#     counts = {}
#     counts_head = {}
#     counts_tail = {}
#     with open(source, 'r') as inputs:
#         for line in inputs:
#             line_dict = json.loads(line)
#             line["section_names"]

# start = time.time()
# for i in range(3):
#     source = tar + targets_txt[i]
#     target = tar + targets_section_names[i]
#     getSectionNames(source, target)
#     end = time.time()
#     cost = end - start
#     print("完成了第: %d 个, 花费时间: %f"%(i, cost))
#     start = time.time()