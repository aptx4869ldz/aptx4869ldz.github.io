from pyecharts import options as opts
from pyecharts.charts import Map, Tab
import os
import pandas


def data_prep(data_name, data_type):
    file_name = os.path.join('data', data_name + '.csv')
    encode = 'utf-8' if data_name == 'COVID world' else 'gbk'
    data = pandas.read_csv(file_name, usecols=['Name', data_type], encoding=encode)
    data = data.set_index('Name').T.to_dict('records')[0]
    if data_name == 'COVID world':
        for country in data:
            try:
                data[country] = int(data[country].replace(',', ''))
            except:
                data[country] = 0
    return list(data.items())


def case_map_w():
    c_map = (
        Map()
        .add("累计确诊",
             case_data_w,
             maptype="world",
             is_map_symbol_show=False,
             layout_center=['30%', '30%'])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=(opts.TitleOpts(title='全球新冠肺炎累计确诊情况')),
                         visualmap_opts=opts.VisualMapOpts(max_=5e6))
        .render('output/mission_2/case_world.html')
    )


def case_map_c():
    c_map = (
        Map()
        .add("累计确诊",
             case_data_c,
             maptype="china",
             is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=(opts.TitleOpts(title='中国新冠肺炎累计确诊情况')),
                         visualmap_opts=opts.VisualMapOpts(max_=5e3))
        .render('output/mission_2/case_china.html')
    )


def death_map_w():
    d_map = (
        Map()
        .add("累计死亡",
             death_data_w,
             maptype="world",
             is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=(opts.TitleOpts(title='全球新冠肺炎累计死亡情况')),
                         visualmap_opts=opts.VisualMapOpts(max_=1e5))
        .render('output/mission_2/death_world.html')
    )


def death_map_c():
    d_map = (
        Map()
        .add("累计死亡",
             death_data_c,
             maptype="china",
             is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=(opts.TitleOpts(title='中国新冠肺炎累计死亡情况')),
                         visualmap_opts=opts.VisualMapOpts(max_=50))
        .render('output/mission_2/death_china.html')
    )


def recovered_map_w():
    r_map = (
        Map()
        .add("累计治愈",
             recovered_data_w,
             maptype="world",
             is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=(opts.TitleOpts(title='全球新冠肺炎累计治愈情况')),
                         visualmap_opts=opts.VisualMapOpts(max_=1e6))
        .render('output/mission_2/recovered_world.html')
    )


def recovered_map_c():
    r_map = (
        Map()
        .add("累计治愈",
             recovered_data_c,
             maptype="china",
             is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=(opts.TitleOpts(title='中国新冠肺炎累计治愈情况')),
                         visualmap_opts=opts.VisualMapOpts(max_=3e3))
        .render('output/mission_2/recovered_china.html')
    )


if __name__ == "__main__":
    case_data_w = data_prep('COVID world', 'Total Cases')
    death_data_w = data_prep('COVID world', 'Total Deaths')
    recovered_data_w = data_prep('COVID world', 'Total Recovered')
    case_data_c = data_prep('COVID China', 'Total Cases')
    death_data_c = data_prep('COVID China', 'Total Deaths')
    recovered_data_c = data_prep('COVID China', 'Total Recovered')
    case_map_w()
    case_map_c()
    death_map_w()
    death_map_c()
    recovered_map_w()
    recovered_map_c()
