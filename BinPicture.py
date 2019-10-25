# coding =utf-8

import os
import matplotlib.pyplot as plt



plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



def draw(title,tup):

    fig, ax = plt.subplots(figsize=(10, 6))         #定义画图第类型与画布第尺寸（长，宽）
    size = 0.6                                      #定义甜甜圈饼图的空白大小
    sizes = []                                      #定义每个区域的大小
    labels = []
    explode = []


    for i in tup:
        labels.append(i[0] + ":" + str(i[1]))
        sizes.append(i[1])

    print(labels)
    colors = ['#C5D89A', '#ECA29E', '#94BFE0',
              "#FDE1A9", "#B3A4C0", "#CCCCCC", "#C2AD9E", "#FEC8D9"]    #定义饼图的颜色
    for i in range(len(labels)):
        explode.append(0.005)                                           #定义饼图中每块的间隙值


    ax.pie(sizes, radius=1, colors=colors,
                           labeldistance=1.07, wedgeprops=dict(width=size, edgecolor='w'),
                           counterclock=False,startangle=90, labels=labels, explode=explode,
                           textprops={'fontsize': 12, 'color': 'w'}, frame=1)


    plt.axis('equal')                                                   # 设置x，y轴刻度一致
    plt.legend(loc='upper right',frameon=False,fontsize='x-large')
    plt.title(title, fontsize=22)

    # 删除x轴和y轴的刻度
    plt.xticks(())
    plt.yticks(())

    nowpath = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(nowpath, "picture/%s.png"%title)
    try:
        os.remove(file)
    except:
        pass
    plt.savefig(file)
    plt.show()

