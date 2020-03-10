## Task 2 解题思路

### A. Most Informative data to track -> jzj

- 综合考虑rating和review分数（情感分数）

- 组合定义user-based model—>之后推到comprehensive score


### B. 分析产品（某一种）的时间序列模 -> zlq

- 定义Product reputation -> review -> 找到 Boom/Bust Point(分别是快速上升和快速下降)

- 相比比同期全类产品增加速率->$\alpha$

- 爆款效应，特定事件（购物节）影响-> Self-Influence Factor

- 两极分化的评论影响->方差乘一个decay函数

### C. 综合Sentiment+Star rating和其他因素给出综合分数模型 -> jzj

- 结合考虑的I和$\alpha$， 考虑d问的特定分影响力 -> 扩展成Comprehensive Score
- 定义总影响力矩阵


### D. 分析某时间特定rating和review的关系 - msy

- 点过程

- 特定分数的影响力模型I



### E. 特定review内容和rating的相关性

- 对相同rating的review做entity analysis 
- 相关度分析
- 确定specific的word
