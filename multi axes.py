import pyecharts.options as opts
from pyecharts.charts import Line, Bar, Timeline
from pyecharts.faker import Faker


def faker(number):
    ite = number // 7 + 1
    faker_list = []
    for i in range(ite):
        faker_list.extend(Faker.values())
    del faker_list[number:]
    return faker_list


x_axis = ['{}月'.format(i) for i in range(1, 13)]
tl = Timeline()
for i in range(2010, 2020):
    bar = (
        Bar(init_opts=opts.InitOpts(width="1200px", height="600px"))
        .add_xaxis(x_axis)
        .add_yaxis("出口",
                   faker(12),
                   yaxis_index=0,
                   color='orange')
        .add_yaxis("进口",
                   faker(12),
                   yaxis_index=1,
                   color='#5793f3')
        .extend_axis(yaxis=opts.AxisOpts(name="出口量",
                                         type_="value",
                                         min_=0,
                                         max_=200,
                                         position='right',
                                         axisline_opts=opts.AxisLineOpts(
                                             linestyle_opts=opts.LineStyleOpts(color='#5793f3')),
                                         axislabel_opts=opts.LabelOpts(formatter="{value} M$", font_size=10)))
        .extend_axis(yaxis=opts.AxisOpts(name="GDP总量",
                                         type_="value",
                                         min_=0,
                                         max_=150,
                                         position='left',
                                         axisline_opts=opts.AxisLineOpts(
                                             linestyle_opts=opts.LineStyleOpts(color='#675bba')),
                                         axislabel_opts=opts.LabelOpts(formatter="{value} M$", font_size=10)))
        .set_global_opts(yaxis_opts=opts.AxisOpts(name="进口量",
                                                  min_=0,
                                                  max_=200,
                                                  position='right',
                                                  offset=60,
                                                  axisline_opts=opts.AxisLineOpts(
                                                      linestyle_opts=opts.LineStyleOpts(color='orange')),
                                                  axislabel_opts=opts.LabelOpts(formatter="{value} M$", font_size=10)
                                                  ),
                         title_opts=opts.TitleOpts(title='A国进出口及GDP情况'),
                         tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'))
    )
    line = (
        Line()
        .add_xaxis(x_axis)
        .add_yaxis('GDP',
                   faker(12),
                   yaxis_index=2,
                   label_opts=opts.LabelOpts(is_show=False))
    )
    bar.overlap(line)
    tl.add(bar, "{}年".format(i))
tl.render('output/mission_4.html')
