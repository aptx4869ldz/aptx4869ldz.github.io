import pandas
import pyecharts.options as opts
from pyecharts.charts import Line, WordCloud, Bar, Timeline, Pie, Tab, Page
import numpy as np

entity_list = ['腾格拉尔', '爱德蒙·唐太斯', '美塞苔丝', '弗尔南多', '维尔福', '法利亚', '阿尔贝', '马西米兰·莫雷尔',
               '瓦朗蒂娜', '卡德鲁斯', '罗吉·万帕', '海黛', '贝尼代托']
entity_dict = {}


def line_markpoint() -> Line:
    line = Line()
    x_axis = ['第' + str(i) + '章' for i in range(1, 118)]
    line.add_xaxis(xaxis_data=x_axis)
    for entity in entity_list:
        y_data = pandas.read_csv(
            'data/word_frequency.csv', usecols=[entity], encoding='GBK')
        y_data = np.array(y_data).reshape(-1).tolist()
        entity_dict[entity] = sum(y_data)
        line.add_yaxis(series_name=entity, y_axis=y_data, label_opts=opts.LabelOpts(is_show=False),
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
    line.set_global_opts(title_opts=opts.TitleOpts(title="《基督山伯爵》主要人物出现频数"),
                         datazoom_opts=[opts.DataZoomOpts()],
                         legend_opts=opts.LegendOpts(pos_top='5%', pos_left='10%'))
    return line


def wordcloud() -> WordCloud:
    cloud = WordCloud()
    wordfreq_list = [(entity, str(entity_dict[entity]))
                     for entity in entity_list]
    cloud.add('', wordfreq_list, shape='circle', word_size_range=[15, 50],
              textstyle_opts=opts.TextStyleOpts(font_family="华文行楷"))
    cloud.set_global_opts(title_opts=opts.TitleOpts(title='《基督山伯爵》主要人物词云'))
    return cloud


def bar_timeline() -> Timeline:
    x_axis = entity_list
    tl = Timeline()
    tot_data = pandas.read_csv('data/word_frequency.csv', encoding='GBK')
    tot_data = np.array(tot_data)
    for i in range(118):
        bar = Bar().add_xaxis(x_axis)
        if not i:
            y_axis = [entity_dict[entity] for entity in entity_list]
            bar.add_yaxis('', y_axis).set_global_opts(title_opts=opts.TitleOpts('《基督山伯爵》主要人物出现频数总和'),
                                                      xaxis_opts=opts.AxisOpts(name_rotate=60,
                                                                               axislabel_opts={"rotate": 45}))
            tl.add(bar, '总和')
        else:
            y_axis = tot_data[i - 1].tolist()
            bar.add_yaxis('', y_axis).set_global_opts(title_opts=opts.TitleOpts('《基督山伯爵》主要人物第{}章出现频数'.format(i)),
                                                      xaxis_opts=opts.AxisOpts(name_rotate=60,
                                                                               axislabel_opts={"rotate": 45}))
            tl.add(bar, '第{}章'.format(i))
    return tl


def pie_rosetype() -> Pie:
    v = list(entity_dict.values())
    pie = Pie().add('', [list(z) for z in zip(entity_list, v)],
                    radius=['30%', '75%'], center=['50%', '50%'],
                    rosetype='area')
    pie.set_global_opts(title_opts=opts.TitleOpts(title='《基督山伯爵》主要人物出现频数比较'),
                        legend_opts=opts.LegendOpts(pos_top='5%', pos_left='0%', orient='vertical'))
    return pie


def page():
    p = Page(layout=Page.SimplePageLayout)
    p.add(
        line_markpoint(),
        wordcloud(),
        bar_timeline(),
        pie_rosetype()
    )
    p.render('output/mission_1.html')


if __name__ == "__main__":
    page()