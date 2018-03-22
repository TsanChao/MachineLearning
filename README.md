

# A typical HMM model

#0.隐马尔可夫模型的三个基本问题

* 给定一个模型，如何计算某个特定的输出序列的概率?

  **Forward-Backward算法**

* 给定一个模型和某个特定的输出序列，如何找到最可能产生这个输出的状态序列?

  **Viterbi算法**

* 给定足够量的观测数据，如何估计隐马尔可夫模型的参数?

  **Baum-Welch算法**

# 1.问题描述

#### 假设连续观察3天的海藻湿度为(Dry, Damp, Soggy),求这三天最可能的天气情况。

# 2. 已知信息

**（1）天气只有三类(Sunny, Cloudy, Rainy)，海藻湿度有四类{Dry, Dryish, Damp, Soggy }，而且海藻湿度和天气有一定的关系。**

**（2）隐藏的状态：Sunny, Cloudy, Rainy;**

**（3）观察状态序列：{Dry, Damp, Soggy}**

**（4）初始状态序列(P)：**

| Sunny | Cloudy | Rainy |
| :---: | :----: | :---: |
| 0.63  |  0.17  | 0.20  |

**（5）状态转移矩阵(A)**

|            | SUNNY | cloudy | rainy |
| :--------: | :---: | :----: | :---: |
| **SUNNY**  |  0.5  | 0.375  | 0.125 |
| **CLOUDY** | 0.25  | 0.125  | 0.625 |
| **RAINY**  | 0.25  | 0.375  | 0.375 |

**（6）混淆矩阵(B)**

|            | DRY  | dryish | damp | soggy |
| :--------: | :--: | :----: | :--: | :---: |
| **SUNNY**  | 0.6  |  0.2   | 0.15 | 0.05  |
| **CLOUDY** | 0.25 |  0.25  | 0.25 | 0.25  |
| **RAINY**  | 0.05 |  0.10  | 0.35 |  0.5  |

# 3.分析

#### 由一阶HMM可知，Day2的天气仅取决于Day1；Day3的天气又只取决于Day2的天气。

# 4.计算过程

####（1）Day1由于是初始状态，我们分别求

* P(Day1-Sunny)=0.63*0.6;
* P(Day1-Cloudy)=0.17*0.25;
* P(Day1-Rain)=0.20*0.05;

> Choose max{ P(Day1-Sunny) , P(Day1-Cloudy),P(Day1-Rainy)}, 得到  P(Day1-Sunny)最大，得出第1天Sunny的概率最大。

#### （2）Day2的天气又取决于Day1的天气状况，同时也受Day2观察的海藻情况影响。

* P(Day2-Sunny)= max{ P(Day1-Sunny)*0.5, P(Day1-Cloudy)*0.25,  P(Day1-					Rainy)*0.25} *0.15;
* P(Day2-Cloudy)= max{ P(Day1-Sunny)*0.375,  P(Day1-Cloudy)*0.125, P(Day1-Rainy)*0.625} *0.25;
* P(Day2-Rainy)= max{ P(Day1-Sunny)*0.125,  P(Day1-Cloudy)*0.625 , P(Day1-Rainy)*0.375} *0.35;

> Choosemax{ P(Day2-Sunny) , P(Day2-Cloudy), P(Day2-Rainy)},得到P(Day2-Rainy)最大，得出第2天Rainy的概率最大。故{Sunny,Rainy}是前两天最大可能的天气序列。

####（3）Day3的天气又取决于Day2的天气状况，同时也受Day3观察的海藻情况影响。

* P(Day3-Sunny)= max{ P(Day2-Sunny)*0.5, P(Day2-Cloudy)*0.25,  P(Day2-Rainy)*0.25} *0.05;
* P(Day3-Cloudy)= max{ P(Day2-Sunny)*0.375,  P(Day2-Cloudy)*0.125, P(Day2-Rainy)*0.625} *0.25;
* P(Day3-Rainy)= max{ P(Day2-Sunny)*0.125,  P(Day2-Cloudy)*0.625, P(Day2-Rainy)*0.375} *0. 05;

> Choosemax{ P(Day3-Sunny) , P(Day3-Cloudy), P(Day3-Rainy)},得到P(Day3-Rainy)最大，得出第3天Rainy的概率最大。故{Sunny,Rainy,Rainy}是这三天最可能的天气序列。