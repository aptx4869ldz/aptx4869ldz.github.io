import jieba
import jieba.posseg as pseg
from pyecharts import options as opts
from pyecharts.charts import Graph


def conference_resolution(w):
    if w == '爱德蒙' or w == '唐太斯' or w == '基督山伯爵':
        return '爱德蒙·唐太斯'
    if w == '马尔塞夫':
        return '弗尔南多'
    if w == '马西米兰' or w == '莫雷尔':
        return '马西米兰·莫雷尔'
    if w == '罗吉' or w == '万帕':
        return '罗吉·万帕'
    return w


txt_file_name = './data/Le Comte de Monte-Cristo.txt'
node_file_name = './output/《基督山伯爵》人物节点.csv'
link_file_name = './output/《基督山伯爵》人物连接.csv'
out_file_name = './output/关系图-《基督山伯爵》人物.html'

txt_file = open(txt_file_name, 'r', encoding='GBK')
line_list = txt_file.readlines()
txt_file.close()

jieba.load_userdict('./data/userdict.txt')

line_name_list = []
name_cnt_dict = {}

ignore_list = ['马赛', '明白', '小姐', '封信', '伯爵', '神甫', '万法郎', '伯爵夫人', '艾曼纽', '尤莉', '子爵', '阿夫']

print('正在分段统计……')
print('已处理词数：')
progress = 0
for line in line_list:
    word_gen = pseg.cut(line)
    line_name_list.append([])

    for one in word_gen:
        word = one.word
        flag = one.flag

        if len(word) == 1 or word in ignore_list:
            continue

        if flag == 'nr':
            word = conference_resolution(word)
            line_name_list[-1].append(word)
            if word in name_cnt_dict.keys():
                name_cnt_dict[word] += 1
            else:
                name_cnt_dict[word] = 1
        progress += 1
        progress_quo = int(progress / 2000)
        progress_mod = progress % 2000
        if progress_mod == 0:
            print('\r' + '-' * progress_quo + '> ' + str(progress_quo * 2) + '千', end='')
print()
print('基础数据处理完成')

relation_dict = {}
name_cnt_limit = 80

for line_name in line_name_list:
    for name1 in line_name:
        if name1 in relation_dict.keys():
            pass
        elif name_cnt_dict[name1] >= name_cnt_limit:
            relation_dict[name1] = {}
        else:
            continue
        for name2 in line_name:
            if name2 == name1 or name_cnt_dict[name2] < name_cnt_limit:
                continue
            if name2 in relation_dict[name1].keys():
                relation_dict[name1][name2] += 1
            else:
                relation_dict[name1][name2] = 1
print('共现统计完成，仅统计出现次数达到' + str(name_cnt_limit) + '及以上的人物')

item_list = list(name_cnt_dict.items())
item_list.sort(key=lambda x: x[1], reverse=True)
node_file = open(node_file_name, 'w')
node_file.write('Name,Weight\n')
node_cnt = 0
node_line_list = []
for name, cnt in item_list:
    if cnt >= name_cnt_limit:
        name_info = name + ',' + str(cnt) + '\n'
        node_line_list.append(name_info)
        node_file.write(name_info)
        node_cnt += 1
node_file.close()
print('人物数量：' + str(node_cnt))
print('已写入文件：' + node_file_name)

link_cnt_limit = 10
print('只导出数量达到' + str(link_cnt_limit) + '及以上的连接')
link_file = open(link_file_name, 'w')
link_file.write('Source,Target,Weight\n')
link_cnt = 0
link_line_list = []
for name1, link_dict in relation_dict.items():
    for name2, link in link_dict.items():
        if link >= link_cnt_limit:
            link_info = name1 + ',' + name2 + ',' + str(link) + '\n'
            link_line_list.append(link_info)
            link_file.write(link_info)
            link_cnt += 1
link_file.close()
print('连接数量：' + str(link_cnt))
print('已写入文件：' + link_file_name)

node_in_graph = []
for one_line in node_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    node_in_graph.append(opts.GraphNode(name=one_line_list[0],
                                        value=int(one_line_list[1]),
                                        symbol_size=int(one_line_list[1]) / 20))

link_in_graph = []
for one_line in link_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    link_in_graph.append(opts.GraphLink(source=one_line_list[0],
                                        target=one_line_list[1],
                                        value=int(one_line_list[2])))

c = Graph(init_opts=opts.InitOpts(width='1200px', height='700px'))
c.add("",
      node_in_graph,
      link_in_graph,
      edge_length=[10, 30],
      repulsion=2500,
      layout='force')
c.set_global_opts(title_opts=opts.TitleOpts(title='关系图-《基督山伯爵》人物'))
c.render(out_file_name)
