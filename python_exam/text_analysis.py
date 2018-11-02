# -*- coding:UTF-8 -*-

# 1.用空白字符替换文章中出现的非英文特殊字符
def sp_alpha_rep(file):
    re_line_list = list()
    # en_alphabet = re.compile(u'[a-zA-Z\s\n]')
    # 英文字母表
    alpha_bet = "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP\'"
    # 按行查找特殊字符，查到相同类型的特殊字符用空格替换
    for line in file:
        for i in range(len(line)):
            if line[i] in alpha_bet:
                pass
            else:
                line = line.replace(line[i], ' ')
        re_line_list.append(line+'\n')
    # 将行列表转换为文本字符
    sp_rep_str = ''.join(re_line_list)

    return sp_rep_str


# 2.统计文章中每个单词出现的次数并输出到文件result.txt中：
def word_count(word_text):
    import re

    word_num = list()
    # 分解出所有的单词
    word_list = word_text.split()
    # 合并相同的单词
    word_rebase_list = list(set(word_list))

    # 对英文文章中出现相同的单词进行统计
    for i in range(len(word_rebase_list)):
        num = 0
        for j in range(len(word_list)):
            # 比较原数组与融合数组中的单词是否相等，是则进行加1计数
            if word_rebase_list[i] == word_list[j]:
                num += 1
        # 储存对应序号的单词的单词数
        word_num.append(num)

    # for i in range(len(word_list_rebase)):
    #     search_list = re.findall(u'{}'.format(word_list_rebase[i]), word_text)
    #     print(search_list)
    #     word_num.append(len(search_list))

    # 将结果写入result.txt文件中
    result_file = open('result.txt', 'w')
    for i in range(len(word_rebase_list)):
        result_file.write("%s:\t%d\n" % (word_rebase_list[i], word_num[i]))
    result_file.close()

    word_info = (word_rebase_list, word_num)
    return word_info


# 3.把出现次数最多的10个单词和对应的频次绘制成表格
def word_chart(word_info):
    import matplotlib.pyplot as plt
    import numpy as np

    # 提取单词统计信息
    word_list = word_info[0]
    word_num = word_info[1]

    # 创建前10个出现次数最多单词的数量列表和字符列表
    max_words = list()
    max_nums = list()

    # 获得单词数由小到大排序后的对应原单词列表的元素序号
    idx = np.argsort(word_num)
    # 有小到大排序好的单词列表的元素序号
    max_id = idx[len(idx) - 10::]
    for i in range(10):
        max_nums.append(word_num[max_id[i]])
        max_words.append(word_list[max_id[i]])
    x = np.arange(len(max_nums))
    # 画单词-单词数折线图，出现次数最多的10个单词
    plt.plot(x, max_nums)
    plt.xticks(x, max_words)
    plt.xlabel('word')
    plt.ylabel('number of word')
    plt.show()


def main():

    f = open('English.txt')
    word_text = sp_alpha_rep(f)
    print(word_text)
    word_info = word_count(word_text)
    word_chart(word_info)
    # print(re_str)


if __name__ == "__main__":
    main()
