from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType

export_list = ['United States', 'Hong Kong', 'Japan', 'Korea', 'Vietnam',
               'Germany', 'India', 'Netherlands', 'United Kingdom', 'Taiwan']
import_list = ['Korea', 'Taiwan', 'Japan', 'United States', 'Australia',
               'Germany', 'Brazil', 'Malaysia', 'Vietnam', 'Russia']
trade = Geo(init_opts=opts.InitOpts(width='1200px', height='800px'))
trade.add_coordinate_json(json_file='data/world_country.json')
trade.add_schema(maptype='world',
                 layout_center=['100%', '100%'],
                 itemstyle_opts=opts.ItemStyleOpts(color='grey', border_color='black'))
trade.add('', [('China', 10)], type_=ChartType.EFFECT_SCATTER, color='orange',
          label_opts=opts.LabelOpts(is_show=False))
trade.add('', [(ex_coun, 10) for ex_coun in export_list], type_=ChartType.SCATTER, color='yellow',
          tooltip_opts=opts.TooltipOpts(is_show=False))
trade.add('出口', [('China', ex_coun) for ex_coun in export_list],
          type_=ChartType.LINES, color='green',
          effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=6, color='white'),
          linestyle_opts=opts.LineStyleOpts(curve=0.2))
trade.add('', [(im_coun, 10) for im_coun in import_list], type_=ChartType.SCATTER, color='yellow',
          tooltip_opts=opts.TooltipOpts(is_show=False))
trade.add('进口', [(im_coun, 'China') for im_coun in import_list],
          type_=ChartType.LINES, color='red',
          effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=6, color='white'),
          linestyle_opts=opts.LineStyleOpts(curve=0.2))
trade.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
trade.set_global_opts(title_opts=opts.TitleOpts(title="中国进出口贸易情况"),
                      legend_opts=opts.LegendOpts(orient='vertical'))
trade.render('./output/mission_2.html')
