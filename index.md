# 计算机科学与编程入门第二次作业
## 1800012990 李典泽
## 1. 作业1
    作业要求：对上一次作业中得到的词频数据进行可视化
    数据信息：来源于上次作业统计出的《基督山伯爵》主要人物出现频数，按章节分开
    作业实现：通过四种不同的图表类型对该数据进行可视化。
             第一幅图. 折线图，横轴代表章节，纵轴代表出现次数，不同主要人物用不同颜色的线表示，加入了datazoom和markpoint(max)效果，该图可以比较一个人在整篇小说中的出现频数变化，
             也可以比较多个人在同一章节的出现频数；
             第二幅图. 词云图，将不同人物出现总频数的多少通过词云表示出来；
             第三幅图. 柱状图，横轴表示不同人物，纵轴代表出现次数，主要可以比较不同人物在整篇小说或某一章节的出现次数，加入timeline以查看整篇小说总和或单个章节的情况；
             第四幅图. 玫瑰图，每个区域代表一个人，可以比较整篇小说各主要人物出现频数比例。
             
[作业1链接](https://aptx4869ldz.github.io/output/mission_1.html)

## 2. 作业2
    作业要求：设定情节，画一幅地理连线图
    数据信息：2019年与中国进出口外贸数额最大的国家
    作业实现：首先画出世界地图；
              然后将中国以及其主要贸易伙伴标点；
              之后进出口用两国对应的两点之间相连曲线表示：绿色的线表示从中国出口，箭头方向是出口国家；橙色的线表示向中国进口，箭头方向是中国。
              
[作业2链接](https://aptx4869ldz.github.io/output/mission_2.html)

## 3. 作业3
    作业要求：设定情节，画出中国地图或世界地图
    数据信息：截至2021/3/31世界各国及中国各省新冠肺炎累计确诊病例、累计死亡病例、累计治愈病例
    作业实现：首先画出世界地图/中国地图；
              然后根据各国/各省相应数据对国家/省色块进行上色，具体视觉映射效果因图而异。
              
[作业3链接_1](https://aptx4869ldz.github.io/output/mission_3/case_world.html)
[作业3链接_2](https://aptx4869ldz.github.io/output/mission_3/death_world.html)
[作业3链接_3](https://aptx4869ldz.github.io/output/mission_3/recovered_world.html)
[作业3链接_4](https://aptx4869ldz.github.io/output/mission_3/case_china.html)
[作业3链接_5](https://aptx4869ldz.github.io/output/mission_3/death_china.html)
[作业3链接_6](https://aptx4869ldz.github.io/output/mission_3/recovered_china.html)

## 4. 作业4
    作业要求：设定情节，画出组合图表
    数据信息：A国2010到2019年每个月进出口额度及GDP信息，通过pyecharts.faker.Faker.values()生成
    作业实现：采用多y轴柱形图和折线图堆叠的可视化方式，横轴表示每个月，出口额度用蓝色柱形表示，进口额度用橙色柱形表示，GDP用红色折线图表示；
              加入timeline以实现年度的变更。
              
[作业4链接](https://aptx4869ldz.github.io/output/mission_4.html)
