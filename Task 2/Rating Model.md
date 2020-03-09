## Rating Model



A challenge in modeling the relationship between sales and ratings is the highly plausible endogenous relationship between the two. That is, a product may show higher sales not necessarily because of better ratings but rather due to a higher appeal to consumers, which is also reflected in higher ratings. This relationship between ratings and sales needs to be carefully addressed before any attributions can be made.



最终目的是建立销量的公式



一些事实：

方差越大，相对销量 $\dfrac{P_{i\tau}}{P\tau}$会更低 



$\tau$ = time index in the rating period, from 1 to 20

【07&之前，0809，10， 11，12q1q2， 12q3q4, 13q1, 13q2, 13q3, 13q4，14m1m2, 14m3m4, 14m5m6, 14m7m8, 14m9m10, 14m11m12, 15m1m2, 15m3m4, 15m5m6, 15m7m8】

$i$ = index of product

$j$ = index of comments of a certain product 
$$
P_{\tau } =  \text{indicates the product sales of all product within time perild $\tau$}
$$

$$
P_{i\tau } =  \text{indicates the product sales of product $i$ within time perild $\tau$}
$$

$$
S_{i \tau } = \text{indicates the overall star ratings score of the product $i$ within time peroid $\tau$}
$$

$$
S_{i j \tau } = \text{indicates the $j^{th}$ star rating score of the product $i$ during time peroid $\tau$}
$$

$$
R_{i \tau } = \text{indicates the overall sentiment score of the product reviews $i$ within time peroid $\tau$}
$$


$$
R_{i j \tau } = \text{indicates the the $j^{th}$ sentiment score of the product reviews $i$ during time peroid $\tau$}
$$

$$
N_{i\tau} = \text{indicates the numbers of comments of product iduring time peroid $\tau$}
$$


$$
M{\tau} = \tau 时间段本身的放大效应， 考虑到黑五等购物季
$$

$$
\gamma_{i\tau} = 产品i对比其他同期产品的放大效应
$$

$$
\alpha_{i\tau} = \dfrac{N_{i\tau} - N_{i(\tau-1)}}{N_{i(\tau-1)}}  - \dfrac{N_{\tau} - N_{\tau-1}}{N_{\tau-1}} \qquad 相对收益率，反映的是某产品i相对于整个市场的表现情况
$$

$$
\beta{i\tau} = 产品i在\tau时间段的beta系数 
$$

$$
S_\tau = 市场在\tau时间段内销量的方差
$$

$$
\sigma_\tau = 市场在\tau时间段内销量的标准差
$$



具体公式：
$$
S_{i\tau} = \dfrac{\sum {}(S_{ij\tau} - 0.5)}{N_{j\tau}} \qquad \text{ 结果区间位于（-1,1）}
$$

$$
R_{i\tau} = \dfrac{\sum {}R_{ij\tau} }{N_{j\tau}}\qquad \text{ 结果区间位于（-1,1）}
$$



最终Comprehensive Score:
$$
C_{i\tau} = M(\tau) * \alpha_{i\tau} * f(S_{i(\tau-1)}, R_{i(\tau-1)})
$$
