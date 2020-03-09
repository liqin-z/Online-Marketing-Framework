## Task 2 解题思路

### A. Most Informative data to track - 金哲健

综合考虑rating和review分数（情感分数）

将其组合定义一个user-based分数—>部分comprehensive score->$f(S,R)$



### B. 分析产品（某一种）的时间序列模型 - 张立勤

定义Product's reputation -> review -> 找到 Boom/Bust Point(分别是快速上升和快速下降)

- 比同期全类产品增加快->$\alpha$

- 爆款效应，特定事件（购物节）影响->M



### C. 综合Sentiment+Star rating和其他因素给出综合分数模型 - 金哲健

在A的基础上用b问的M和$\alpha$， 考虑d问的特定分影响力 -> 扩展成C的模型

严谨数学定义+证明



###D. 分析某时间特定rating和review的关系 - 张立勤

- 某个分段rating的review - 数量变化趋势 - 情感得分变化趋势
- 特定分数的影响力模型I



### E. 特定review内容和rating的相关性

- 对相同rating的review做entity analysis 
- 相关度分析
- 确定specific的word