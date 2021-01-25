# by 猪哥，学习交流可关注微信公众号：裸睡的猪，回复：微信，加猪哥微信！

# 十一届国赛题，空间优化方案：
if __name__ == '__main__':
    # 输入 k p l，空格分隔
    k, p, L = map(int, input("input k p L separated by one spaces:").split())
    # 1、生成二维数组，0层存 第一步小于p的方案数，1层存 总方案数
    # 最小数组长度
    len = k + 1
    dp = [[0 for e1 in range(2)] for e in range(len)]
    # 赋值 L=0 的情况
    dp[0][0] = 1
    dp[0][1] = 1
    i = 0  # 定义循环写入的角标
    # L为总距离数
    for l in range(1, L + 1):  # l无用
        # 循环改变数组列角标，取模
        i = (i + 1) % len
        # 临时值，用于将 第一步小于p的方案数 与
        # 第一步大于等于p的方案数相加
        sum = 0
        # 2、开始计算 第一步小于p的方案数，存储在二维数组的0层
        for j in range(1, p):
            sum += (dp[(i - j) % len][1]) % 20201114
        dp[i][0] = sum  # 记录 第一步小于p的方案数
        # 3、开始计算 第一步大于等于p的方案数
        for o in range(p, k + 1):
            # 之前sum已经是 第一步小于p的方案数
            # 这里直接相加就等于总方案数啦
            sum += dp[(i - o) % len][0] % 20201114
        dp[i][1] = sum  # 4、记录总方案数，存储在二维数组的1层
    # 5、循环结束，直接获取对应角标的1层即是 总方案数
    print((dp[i][1]) % 20201114)
