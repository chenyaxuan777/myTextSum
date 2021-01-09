import json
from collections import Counter
'''
主要是对数据集进行统计：平均句子数、平均长度等
'''



path = "E:\\paper\\数据集\\arxiv摘要\\arxiv-dataset\\processed_data\\del_train.txt"

# 工具函数：统计一句中单词数量
def count_word_nums(sentence):
    sentence_list = sentence.split(' ')
    return len(sentence_list)

# 统计数据集中的平均段落数
def count_section_nums(source):
    with open(source, 'r') as file:
        lines = file.readlines()
        article_total = len(lines)
        section_total = 0   # 数据集中的所有section数总和
        section_num_list = []   # 记录每条样本的section数量 eg:[3,5,6]表示三篇文章的章节数为3,5,6
        section_num_count = Counter()
        for line in lines:
            line_dict = json.loads(line)
            length = len(line_dict["section_names"])
            section_total += length
            # 统计section频率
            section_num_list.append(length)
        section_num_count += Counter(section_num_list)
    print("总数：" , article_total)
    print("总段落数： " , section_total)
    print("平均段落数： ", '%.2f'%(section_total/article_total))
    print("段落频率情况统计：\n", section_num_count)

# 统计数据集中的平均文章长度:1.全读入
def count_text_length1(source):
    sentence_total = 0
    word_total = 0
    article_total = 0
    with open(source, 'r') as file:
        lines = file.readlines()
        for line in lines:
            article_total += 1
            line_dict = json.loads(line)
            sections_list = line_dict["sections"]
            # 每个section是一个list,list中存的是该section中的句子
            for section in sections_list:
                # 算句子总数
                sentence_total += len(section)
                # 对列表中的每个句子用工具函数：统计该句中的单词数
                sentence_word_nums_list = list(map(count_word_nums, section))
                word_total += sum(sentence_word_nums_list)
    print("文章总数：", article_total)
    print("句子总数：", sentence_total)
    print("单词总数：", word_total)
    print("平均句子数：", '%0.2f'%(sentence_total/article_total))
    print("平均单词：", '%0.2f'%(word_total/article_total))
    print("平均句子长度：", '%0.2f'%(word_total/sentence_total))

# 统计数据集中的平均文章长度:2.逐行读
def count_text_length2(source):
    sentence_total = 0
    word_total = 0
    article_total = 0
    with open(source, 'r') as file:
        for line in file:
            article_total += 1
            line_dict = json.loads(line)
            sections_list = line_dict["sections"]
            # 每个section是一个list,list中存的是该section中的句子
            for section in sections_list:
                # 算句子总数
                sentence_total += len(section)
                # 对列表中的每个句子用工具函数：统计该句中的单词数
                sentence_word_nums_list = list(map(count_word_nums, section))
                word_total += sum(sentence_word_nums_list)
    print("文章总数：", article_total)
    print("句子总数：", sentence_total)
    print("单词总数：", word_total)
    print("平均句子数：", '%0.2f'%(sentence_total/article_total))
    print("平均单词：", '%0.2f'%(word_total/article_total))
    print("平均句子长度：", '%0.2f'%(word_total/sentence_total))

# 统计数据集中的摘要信息：平均长度、平均句数:1.全读入
def count_abstract_length1(source):
    sentence_total = 0
    word_total = 0
    article_total = 0
    with open(source, 'r') as file:
        for line in file.readlines():
            article_total += 1
            line_dict = json.loads(line)
            abstract_list = line_dict["abstract_text"]
            # 每个abstract是一个list,list中存的是该section中的句子

            # 算句子总数
            sentence_total += len(abstract_list)
            # 对列表中的每个句子用工具函数：统计该句中的单词数
            sentence_word_nums_list = list(map(count_word_nums, abstract_list))
            word_total += sum(sentence_word_nums_list)
        print("文章总数：", article_total)
        print("句子总数：", sentence_total)
        print("单词总数：", word_total)
        print("平均句子数：", '%0.2f' % (sentence_total / article_total))
        print("平均单词：", '%0.2f' % (word_total / article_total))
        print("平均句子长度：", '%0.2f' % (word_total / sentence_total))

# 统计数据集中的摘要信息：平均长度、平均句数:2.逐句读入
def count_abstract_length2(source):
    sentence_total = 0
    word_total = 0
    article_total = 0
    with open(source, 'r') as file:
        for line in file:
            article_total += 1
            line_dict = json.loads(line)
            abstract_list = line_dict["abstract_text"]
            # 每个abstract是一个list,list中存的是该section中的句子

            # 算句子总数
            sentence_total += len(abstract_list)
            # 对列表中的每个句子用工具函数：统计该句中的单词数
            sentence_word_nums_list = list(map(count_word_nums, abstract_list))
            word_total += sum(sentence_word_nums_list)
        print("文章总数：", article_total)
        print("句子总数：", sentence_total)
        print("单词总数：", word_total)
        print("平均句子数：", '%0.2f' % (sentence_total / article_total))
        print("平均单词：", '%0.2f' % (word_total / article_total))
        print("平均句子长度：", '%0.2f' % (word_total / sentence_total))

count_abstract_length2(path)