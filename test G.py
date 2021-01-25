# by 猪哥，学习交流可关注微信公众号：裸睡的猪，回复：微信，加猪哥微信！
import string
import datetime


# 十一届省赛题，方案一
def get_max_count_letter(word):
    # 1、获取每个字母出现的次数
    counter = {}  # 用字典来存放结果，例如{'a':1, 'b'}
    for i in word:  # 遍历整个字符串
        counter.setdefault(i, 0)  # 如果第一次出现就设置次数为默认0
        counter[i] += 1
    # 2、找出次数最多的字母
    character = ""
    max_count = 0
    for k, v in counter.items():
        # 比次数
        if v > max_count:
            max_count = v
            character = k
        # 如果次数相同，谁小（ascii码）就选谁
        elif v == max_count:
            if k < character:
                character = k
    return character, max_count


# 方案二
def get_max_count_letter_2(word):
    # 1、遍历26个英文字母在word出现次数，再选择次数最大的一个
    character = max(string.ascii_lowercase, key=word.count)
    # 2、获取该字母出现的次数
    max_count = word.count(character)
    return character, max_count


if __name__ == '__main__':
    # 输入
    word = input("enter a lowercase word: ")

    # 统计程序时间-开始
    starttime = datetime.datetime.now().microsecond

    # 执行方法
    # letter = get_max_count_letter(word)
    letter = get_max_count_letter_2(word)

    # 统计程序时间-结束
    endtime = datetime.datetime.now().microsecond

    print(*letter, sep='\n')
    print('time：', (endtime - starttime), '微秒')
