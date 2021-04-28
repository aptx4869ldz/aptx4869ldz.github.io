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

## 5、作业5
    作业要求：选择一部文学作品，分析人物“共现”，生成关系图
    数据信息：分析文本为《基督山伯爵》全书，总计约95w字
    作业实现：第一步，通过jieba中文分词库中的posseg.cut函数对每个段落进行分词，得到分词结果以及每个词的词性，选取其中词性为人名('nr')的词，从而生成每个段落出现的人物列表（格式为[[第一段出现的人物], [第二段出现的人物], ...]line_name_list以及人物出现的总次数name_cnt_dict
    第二步，建立一个字典relation_dict用于存储人物共现的关系，relation_dict的key（记为k1）为人名，value（记为v1）同样是字典，v1中的key（记为k2）对应的value（记为v2）代表k1和k2共现的次数为v2；对line_name_list中每个元素即每一段的人物做遍历，对某一个人物，遍历本段其他所有人物，统计共现次数并加到relation_dict中
    第三步，通过pyecharts的Graph图绘制力导向图实现《基督山伯爵》人物共现可视化

[作业5链接](https://aptx4869ldz.github.io/word_co-occurrence/output/关系图-《基督山伯爵》人物.html)

## 6、作业6
    作业要求：用html设计一个网页，包含输入框和按钮，实现搜索引擎功能
    作业实现：通过html中的<input>标签实现输入框和按钮，type分别为'text'和'submit'，同时通过设置style调整其大小使其更加美观；通过<form>标签实现与服务器的通话，发送表单数据的对象地址为https://www.baidu.com/s, 即百度搜索引擎；在输入框和按钮上方加入一张百度的logo使得页面更加逼真；插入背景图，是页面更加具有观赏性
    
[作业6链接](https://aptx4869ldz.github.io/mybaidu/mybaidu.html)

## 7、作业7
    作业要求：设计一个网页，用CSS美化
    作业实现：网页内容是世界各地的一些风景，共6张。下面按照页面元素介绍CSS内容。首先是标题，本页面只使用了一级标题h1，因此在CSS中对h1进行了设置：绿色字、居中、加粗、大小50px、字体Arial；接下来是三个大的div，在CSS中定义为row-div类，宽度为100%，从上往下排列；在每个row-div中，又一左一右包含两个div：left-div和right-div，在CSS中高度都为50%，宽度都为45%，一个排列在左(float=left)，一个排列在右，设置left和right调整其在row-div的位置使其分布对称；每个小的div中包含一张图片以及一句对图片的描述，其中左边的图片对应的描述是英文，格式为蓝色字、居中、斜体、加粗、大小15px、字体Zapfino，而Zapfino并非CSS自带语言，因此在网上下载后通过@font-face导入CSS中；右边的图片对应的描述是中文，格式为红色字、居中、斜体、加粗、字体大小25px、字体华为行楷(STXingkai)
    
[作业7链接](https://aptx4869ldz.github.io/css-design/mywebsite_AS.html)
