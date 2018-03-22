#-*-coding:utf-8-*-
def viterbi(N, M, A, B, P, hidden, observed):
    sta = []
    LEN = len(observed)
    Q = [([0] * N) for i in range(LEN)]
    path = [([0] * N) for i in range(LEN)]
    # 第一天计算，状态的初始概率*隐藏状态到观察状态的条件概率
    for j in range(N):
        Q[0][j] = P[j] * B[j][observation.index(observed[0])]
        path[0][j] = -1
    # 第一天以后的计算
    # 前一天的每个状态转移到当前状态的概率最大值
    # *
    # 隐藏状态到观察状态的条件概率
    for i in range(1, LEN):
        for j in range(N):
            max = 0.0
            index = 0
            for k in range(N):
                if (Q[i - 1][k] * A[k][j] > max):
                    max = Q[i - 1][k] * A[k][j]
                    index = k
            Q[i][j] = max * B[j][observation.index(observed[i])]
            path[i][j] = index
    # 找到最后一天天气呈现哪种观察状态的概率最大
    max = 0.0
    idx = 0
    for i in range(N):
        if (Q[LEN - 1][i] > max):
            max = Q[LEN - 1][i]
            idx = i
    print "最可能隐藏序列的概率：" + str(max)
    sta.append(hidden[idx])
    # 逆推回去找到每天出现哪个隐藏状态的概率最大
    for i in range(LEN - 1, 0, -1):
        idx = path[i][idx]
        sta.append(hidden[idx])
    sta.reverse()
    return sta


# 3 种隐藏层状态:sun cloud rain
hidden = []
hidden.append('sun')
hidden.append('cloud')
hidden.append('rain')
N = len(hidden)
# 4 种观察层状态:dry dryish damp soggy
observation = []
observation.append('dry')
observation.append('dryish')
observation.append('damp')
observation.append('soggy')
M = len(observation)
# 初始状态矩阵（1*N第一天是sun，cloud，rain的概率）
P = (0.63, 0.17, 0.20)

# 状态转移矩阵A（N*N 隐藏层状态之间互相转变的概率）
A=((0.5, 0.375, 0.125),
   (0.25, 0.125, 0.625),
   (0.25, 0.375, 0.375))

# 混淆矩阵B（N*M 隐藏层状态对应的观察层状态的概率）
B=((0.6, 0.2, 0.15, 0.05),
   (0.25, 0.25, 0.25, 0.25),
   (0.05, 0.10, 0.35, 0.50))

# 假设观察到一组序列为observed，输出HMM模型（N，M，A，B，P）产生观察序列observed的概率
observed = ['dry', 'damp', 'soggy']
print viterbi(N, M, A, B, P, hidden, observed)
